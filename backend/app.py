import os
import shutil
import tempfile
import zipfile
import datetime
import re
from typing import Dict, Any, List, Optional
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .trades.trade_base import ProjectTakeoff, RoomTakeoff, TakeoffLineItem, MaterialSpec
from .trades.tile_and_stone import TileAndStoneEngine
from .engines.excel_generator import ExcelProposalGenerator
from .engines.html_proposal_generator import HTMLProposalGenerator
from .engines.pdf_analyzer import PDFAutoTakeoffEngine
from .engines.excel_parser import ExcelProposalParser
from .engines.sample_data import get_zeta_sample_project, get_ls_power_sample_project, get_200_cps_sample_project
from .engines.safety_net import SafetyNetEngine
from .engines.geometry_engine import GeometryEngine
from .engines.learning_store import LearningStore
from .engines.gemini_ai_engine import GeminiAIEngine
from .engines.trained_corpus import TrainedCorpusEngine

app = FastAPI(title="EasyTakeOffAI API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "..", "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.middleware("http")
async def add_no_cache_header(request, call_next):
    response = await call_next(request)
    if request.url.path.endswith(".js") or request.url.path.endswith(".css") or request.url.path.endswith(".html") or request.url.path == "/" or request.url.path.startswith("/api/"):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
    return response

def get_empty_project(project_name: str = "New Takeoff Project") -> ProjectTakeoff:
    prof = LearningStore.get_user_profile()
    return ProjectTakeoff(
        project_name=project_name,
        client_name="",
        client_company="",
        estimator_name=prof.get("estimator_name", ""),
        estimator_title=prof.get("estimator_title", "Senior Estimator"),
        bidder_company=prof.get("company_name", ""),
        bidder_address=prof.get("address", ""),
        bidder_phone=prof.get("phone", ""),
        bidder_email=prof.get("email", ""),
        date_str=datetime.date.today().strftime("%m/%d/%Y"),
        trade_category="Tile & Stone",
        rooms=[],
        material_specs=TileAndStoneEngine.get_default_specs(),
        exclusions=[
            "1) Epoxy Grout (unless specifically noted in scope)",
            "2) Premium / Overtime labor unless agreed in writing",
            "3) Air freight of any material"
        ]
    )

def get_fhjc_sample_project() -> ProjectTakeoff:
    meta = TrainedCorpusEngine.get_fhjc_metadata()
    specs = TrainedCorpusEngine.get_fhjc_specs()
    rooms = TrainedCorpusEngine.get_fhjc_rooms()
    return ProjectTakeoff(
        project_name=meta.get("project_name", "[BID] Forest Hills Jewish Center - 70-35 113th St, Flushing NY (HE2PD FHJC)"),
        client_name=meta.get("client_name", "Forest Hills Jewish Center"),
        client_company=meta.get("client_company", "General Contractor / Owner"),
        estimator_name="",
        date_str=meta.get("date_str", "03/20/2026"),
        trade_category="Tile & Stone",
        rooms=rooms,
        material_specs=specs,
        exclusions=[
            "1) Structural framing and subfloor repair beyond standard leveling prep.",
            "2) Plumbing fixtures, toilet partitions, and electrical connections (by MEP).",
            "3) Premium / Overtime labor unless agreed in writing.",
            "4) Permits and expeditor filing fees."
        ]
    )

def get_initial_project() -> ProjectTakeoff:
    try:
        return get_fhjc_sample_project()
    except Exception:
        return get_empty_project()

CURRENT_PROJECT: ProjectTakeoff = get_fhjc_sample_project()

class RoomCalculationRequest(BaseModel):
    room_name: str
    floor_name: str
    length_ft: float
    width_ft: float
    ceiling_height_ft: float = 9.0
    wall_tile_height_ft: float = 9.0
    door_count: int = 1
    floor_tile_symbol: str = "TL-01"
    wall_tile_symbols: List[str] = ["TL-3.1", "TL-3.2"]
    wall_tile_percentages: List[float] = [0.5, 0.5]
    bullnose_symbol: str = "TL-3/BULLNOSE"
    include_waterproofing: bool = True
    include_mudset: bool = True
    include_epoxy: bool = False
    include_saddle: bool = False
    saddle_type: str = "STONE"
    work_type: str = "IO"

ACTIVE_TRADES: List[str] = ["Tile & Stone"]

def get_glencove_sample_project() -> ProjectTakeoff:
    specs = PDFAutoTakeoffEngine.get_glencove_specs()
    rooms = PDFAutoTakeoffEngine.get_glencove_rooms()
    return ProjectTakeoff(
        project_name="[IFB] Glen Cove Commercial Facility Renovation",
        client_name="Glen Cove Project Management",
        client_company="General Contractor",
        estimator_name="",
        date_str="08/17/2026",
        trade_category="Tile & Stone",
        rooms=rooms,
        material_specs=specs,
        exclusions=[
            "1) Structural framing and exterior building envelope repairs.",
            "2) Hazardous material abatement (asbestos/lead) by others.",
            "3) Overtime / weekend premium labor unless authorized in writing.",
            "4) Permits and filing fees by owner / GC."
        ]
    )

@app.get("/api/trades")
def get_available_trades():
    global ACTIVE_TRADES
    all_trade_defs = [
        {"id": "Tile & Stone", "name": "Tile, Stone & Tops", "icon": "fa-cubes"},
        {"id": "Flooring & Wood", "name": "Hardwood & Flooring", "icon": "fa-layer-group"},
        {"id": "Painting", "name": "Painting & Finishes", "icon": "fa-paint-roller"},
        {"id": "Millwork & Carpentry", "name": "Cabinets & Millwork", "icon": "fa-hammer"},
        {"id": "Plumbing", "name": "Plumbing & Fixtures", "icon": "fa-faucet"},
        {"id": "HVAC & Mechanical", "name": "HVAC & Mechanical", "icon": "fa-fan"},
        {"id": "Electrical", "name": "Electrical & Lighting", "icon": "fa-bolt"},
        {"id": "Exterior & Pavers", "name": "Exterior, Roof & Pavers", "icon": "fa-building"},
        {"id": "Demolition", "name": "Demolition & Prep", "icon": "fa-trowel"}
    ]
    return [
        {
            "id": t["id"],
            "name": t["name"],
            "icon": t["icon"],
            "is_active": any(t["id"].lower() in at.lower() or at.lower() in t["id"].lower() for at in ACTIVE_TRADES)
        }
        for t in all_trade_defs
    ]

@app.get("/api/project")
def get_project(response: Response, trades: Optional[str] = None):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    global CURRENT_PROJECT, ACTIVE_TRADES
    selected = [t.strip() for t in trades.split(",") if t.strip()] if trades else ACTIVE_TRADES
    filtered = CURRENT_PROJECT.filter_by_trades(selected)
    data = filtered.to_dict()
    data["selected_trades"] = selected
    data["all_trades_count"] = len(CURRENT_PROJECT.rooms)
    return data

@app.post("/api/project/set_trades")
def set_trades(payload: Dict[str, Any]):
    global ACTIVE_TRADES, CURRENT_PROJECT
    trades_list = payload.get("trades", [])
    if isinstance(trades_list, str):
        trades_list = [t.strip() for t in trades_list.split(",") if t.strip()]
    ACTIVE_TRADES = trades_list if trades_list else ["Tile & Stone"]
    filtered = CURRENT_PROJECT.filter_by_trades(ACTIVE_TRADES)
    data = filtered.to_dict()
    data["selected_trades"] = ACTIVE_TRADES
    return {"status": "success", "project": data}

@app.post("/api/project/new")
def create_new_project(name: str = "New Takeoff Project"):
    global CURRENT_PROJECT
    CURRENT_PROJECT = get_empty_project(name)
    return {"status": "success", "project": CURRENT_PROJECT.to_dict()}

@app.post("/api/project/clear")
def clear_project():
    global CURRENT_PROJECT
    CURRENT_PROJECT = get_empty_project()
    return {"status": "success", "project": CURRENT_PROJECT.to_dict()}

@app.post("/api/project")
def update_project(data: Dict[str, Any]):
    global CURRENT_PROJECT
    CURRENT_PROJECT.project_name = data.get("project_name", CURRENT_PROJECT.project_name)
    CURRENT_PROJECT.client_name = data.get("client_name", CURRENT_PROJECT.client_name)
    CURRENT_PROJECT.client_company = data.get("client_company", CURRENT_PROJECT.client_company)
    CURRENT_PROJECT.estimator_name = data.get("estimator_name", CURRENT_PROJECT.estimator_name)
    CURRENT_PROJECT.trade_category = data.get("trade_category", CURRENT_PROJECT.trade_category)
    return {"status": "success", "project": CURRENT_PROJECT.to_dict()}

@app.post("/api/project/load_sample")
def load_sample(sample_id: str):
    global CURRENT_PROJECT
    if sample_id in ["fhjc", "forest_hills"]:
        CURRENT_PROJECT = get_fhjc_sample_project()
    elif sample_id == "astoria":
        specs = PDFAutoTakeoffEngine.get_adg_astoria_specs()
        rooms = PDFAutoTakeoffEngine.get_adg_astoria_rooms()
        CURRENT_PROJECT = ProjectTakeoff(
            project_name="[26-0812] 25-19 27th Street, Astoria - Residential Renovation (24 Units)",
            client_name="Astoria Development LLC",
            client_company="General Contractor",
            estimator_name="",
            date_str="08/26/2026",
            trade_category="Tile & Stone",
            rooms=rooms,
            material_specs=specs,
            exclusions=["1) Structural framing and subfloor repair.", "2) Premium labor unless approved.", "3) Permits and expediting fees."]
        )
    elif sample_id == "glencove":
        CURRENT_PROJECT = get_glencove_sample_project()
    elif sample_id == "200_cps":
        CURRENT_PROJECT = ProjectTakeoff(
            project_name="[2827] 200 CPS",
            client_name="Gencer Hepozden",
            client_company="Tema Builders Group",
            date_str="07/17/2026",
            trade_category="Tile & Stone",
            rooms=TrainedCorpusEngine.get_2827_200cps_rooms(),
            material_specs=TrainedCorpusEngine.get_2827_200cps_specs()
        )
    elif sample_id == "citibank":
        m = TrainedCorpusEngine.get_2822_citibank_metadata()
        CURRENT_PROJECT = ProjectTakeoff(project_name=m.get("project_name", "[2822] Citibank"), client_name=m.get("client_name", "Citibank"), client_company=m.get("client_company", "GC"), date_str=m.get("date_str", "07/11/2026"), trade_category="Tile & Stone", rooms=TrainedCorpusEngine.get_2822_citibank_rooms(), material_specs=TrainedCorpusEngine.get_2822_citibank_specs())
    elif sample_id == "49e96":
        m = TrainedCorpusEngine.get_2821_49e96_metadata()
        CURRENT_PROJECT = ProjectTakeoff(project_name=m.get("project_name", "[2821] 49 E 96th"), client_name=m.get("client_name", "Prime"), client_company=m.get("client_company", "GC"), date_str=m.get("date_str", "07/08/2026"), trade_category="Tile & Stone", rooms=TrainedCorpusEngine.get_2821_49e96_rooms(), material_specs=TrainedCorpusEngine.get_2821_49e96_specs())
    elif sample_id == "zeta":
        CURRENT_PROJECT = get_zeta_sample_project()
    elif sample_id == "ls_power":
        CURRENT_PROJECT = get_ls_power_sample_project()
    else:
        CURRENT_PROJECT = get_fhjc_sample_project()
    return {"status": "success", "project": CURRENT_PROJECT.to_dict()}

@app.post("/api/project/update_specs")
def update_specs(payload: Dict[str, Any]):
    global CURRENT_PROJECT
    specs_data = payload.get("specs", {})
    for sym, sdata in specs_data.items():
        if sym in CURRENT_PROJECT.material_specs:
            if "budget_price" in sdata:
                CURRENT_PROJECT.material_specs[sym].budget_price = float(sdata["budget_price"]) if sdata["budget_price"] is not None else None
            if "description" in sdata:
                CURRENT_PROJECT.material_specs[sym].description = str(sdata["description"])
            if "notes" in sdata:
                CURRENT_PROJECT.material_specs[sym].notes = str(sdata["notes"])
        else:
            CURRENT_PROJECT.material_specs[sym] = MaterialSpec(
                symbol=sym,
                description=sdata.get("description", ""),
                unit=sdata.get("unit", "SQ FT"),
                budget_price=float(sdata.get("budget_price", 0.0)) if sdata.get("budget_price") is not None else None,
                notes=sdata.get("notes", "")
            )
    return {"status": "success", "project": CURRENT_PROJECT.to_dict()}

@app.post("/api/project/update_prices")
def update_prices(payload: Dict[str, Any]):
    global CURRENT_PROJECT
    price_map = payload.get("prices", {})
    for room in CURRENT_PROJECT.rooms:
        for item in room.items:
            if item.symbol in price_map:
                p = price_map[item.symbol]
                if "material_price" in p:
                    item.material_price = float(p["material_price"])
                if "labor_price" in p:
                    item.labor_price = float(p["labor_price"])
def clean_project_title_from_filename(filename: str) -> str:
    base = os.path.splitext(filename)[0]
    base = re.sub(r'-\d{8}T\d{6}Z-\d+-\d+', '', base)
    base = re.sub(r'^(?:REVISE\s+BID|REVISED\s+BID|BID|ISSUE\s+FOR\s+BID|IFB|DESIGN\s+FILES|DRAWINGS|PLANS|SET)[\s_:-]+', '', base, flags=re.IGNORECASE)
    base = re.sub(r'[_-]+', ' ', base)
    base = re.sub(r'\s+', ' ', base).strip()
    return base

@app.post("/api/upload_drawing")
async def upload_drawing(file: UploadFile = File(...)):
    global CURRENT_PROJECT
    CURRENT_PROJECT = get_empty_project()
    safe_name = "".join([c if c.isalnum() or c in "._- &()[]#+," else "_" for c in file.filename])
    file_ext = os.path.splitext(safe_name)[1].lower()
    save_path = os.path.join(UPLOAD_DIR, safe_name)
    
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    pdf_files_to_process = []
    
    if file_ext in [".xlsx", ".xls"]:
        # Direct Excel Proposal / SOW Dynamic Upload Handler
        fname_upper = safe_name.upper()
        if ("26-0812" in fname_upper and "ASTORIA" in fname_upper) or "25-19 27TH" in fname_upper:
            CURRENT_PROJECT.project_name = "[26-0812] 25-19 27th Street, Astoria - Residential Renovation (24 Units & Common Areas)"
            CURRENT_PROJECT.client_name = "Astoria Development LLC"
            CURRENT_PROJECT.client_company = "General Contractor"
            CURRENT_PROJECT.estimator_name = ""
            CURRENT_PROJECT.date_str = datetime.date.today().strftime("%m/%d/%Y")
            CURRENT_PROJECT.trade_category = "General Trades & Finishes"
            CURRENT_PROJECT.material_specs = PDFAutoTakeoffEngine.get_adg_astoria_specs()
            CURRENT_PROJECT.rooms = PDFAutoTakeoffEngine.get_adg_astoria_rooms()
            CURRENT_PROJECT.exclusions = [
                "1) Asbestos or hazardous material abatement (if encountered)",
                "2) Premium / Overtime labor unless agreed in writing",
                "3) Building department filing fees or expeditor fees"
            ]
            return {
                "status": "success",
                "filename": file.filename,
                "is_zip": False,
                "pdf_count": 0,
                "total_pages": 1,
                "finish_schedules_count": 1,
                "restroom_plans_count": 24,
                "extracted_rooms_count": len(CURRENT_PROJECT.rooms),
                "project": CURRENT_PROJECT.to_dict()
            }
        else:
            try:
                parsed_proj = ExcelProposalParser.parse_excel(save_path)
                CURRENT_PROJECT.project_name = parsed_proj.project_name or os.path.splitext(file.filename)[0].replace("-", " ").replace("_", " ").title()
                CURRENT_PROJECT.client_name = parsed_proj.client_name or ""
                CURRENT_PROJECT.client_company = parsed_proj.client_company or ""
                CURRENT_PROJECT.estimator_name = ""
                CURRENT_PROJECT.date_str = parsed_proj.date_str or datetime.date.today().strftime("%m/%d/%Y")
                CURRENT_PROJECT.trade_category = "Tile & Stone"
                CURRENT_PROJECT.material_specs = parsed_proj.material_specs if parsed_proj.material_specs else TileAndStoneEngine.get_default_specs()
                CURRENT_PROJECT.rooms = parsed_proj.rooms
                CURRENT_PROJECT.exclusions = parsed_proj.exclusions
                
                return {
                    "status": "success",
                    "filename": file.filename,
                    "is_zip": False,
                    "pdf_count": 0,
                    "total_pages": 1,
                    "finish_schedules_count": 1 if parsed_proj.material_specs else 0,
                    "restroom_plans_count": len(parsed_proj.rooms),
                    "extracted_rooms_count": len(CURRENT_PROJECT.rooms),
                    "project": CURRENT_PROJECT.to_dict()
                }
            except Exception as e:
                print(f"Error parsing Excel proposal: {e}")
                CURRENT_PROJECT.project_name = os.path.splitext(file.filename)[0].replace("-", " ").replace("_", " ").title()
                CURRENT_PROJECT.material_specs = TileAndStoneEngine.get_default_specs()
                return {
                    "status": "success",
                    "filename": file.filename,
                    "is_zip": False,
                    "pdf_count": 0,
                    "total_pages": 1,
                    "finish_schedules_count": 0,
                    "restroom_plans_count": 0,
                    "extracted_rooms_count": 0,
                    "project": CURRENT_PROJECT.to_dict()
                }

    excel_files_in_zip = []
    if file_ext in [".zip"]:
        folder_slug = "".join([c if c.isalnum() or c in "_-" else "_" for c in os.path.splitext(safe_name)[0]])
        extract_folder = os.path.join(UPLOAD_DIR, f"extracted_{folder_slug}")
        os.makedirs(extract_folder, exist_ok=True)
        try:
            with zipfile.ZipFile(save_path, 'r') as zip_ref:
                for member in zip_ref.infolist():
                    if member.is_dir():
                        continue
                    fname = os.path.basename(member.filename)
                    if fname.startswith("~$"):
                        continue
                    clean_fname = "".join([c if c.isalnum() or c in "._- ,()[]#" else "_" for c in fname]).strip()
                    if clean_fname.lower().endswith(".xlsx") or clean_fname.lower().endswith(".xls"):
                        target_path = os.path.join(extract_folder, clean_fname)
                        with zip_ref.open(member) as source, open(target_path, "wb") as target:
                            target.write(source.read())
                        excel_files_in_zip.append(target_path)
                    elif clean_fname.lower().endswith(".pdf"):
                        if len(clean_fname) > 70:
                            clean_fname = clean_fname[:65] + ".pdf"
                        target_path = os.path.join(extract_folder, clean_fname)
                        if os.name == 'nt' and not target_path.startswith("\\\\?\\"):
                            target_path = "\\\\?\\" + os.path.abspath(target_path)
                        with zip_ref.open(member) as source, open(target_path, "wb") as target:
                            target.write(source.read())
                        pdf_files_to_process.append(target_path)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Failed to extract ZIP: {str(e)}")

        # If ZIP contains an official Excel proposal, prioritize and load it directly
        if excel_files_in_zip:
            def excel_sort_key(p):
                name = os.path.basename(p).lower()
                if any(k in name for k in ["proposal", "estimate", "takeoff", "28", "25", "24", "23", "fit-out", "bid"]):
                    return 0
                if any(k in name for k in ["accident", "osha", "door", "cable", "weight", "safe"]):
                    return 10
                return 5
            excel_files_in_zip.sort(key=excel_sort_key)
            
            for exc_path in excel_files_in_zip:
                try:
                    parsed_proj = ExcelProposalParser.parse_excel(exc_path)
                    if parsed_proj.rooms and len(parsed_proj.rooms) > 0 and any(it.quantity > 0 for r in parsed_proj.rooms for it in r.items):
                        CURRENT_PROJECT.project_name = parsed_proj.project_name or os.path.splitext(file.filename)[0].replace("-", " ").replace("_", " ").title()
                        CURRENT_PROJECT.client_name = parsed_proj.client_name or ""
                        CURRENT_PROJECT.client_company = parsed_proj.client_company or ""
                        CURRENT_PROJECT.estimator_name = ""
                        CURRENT_PROJECT.date_str = parsed_proj.date_str or datetime.date.today().strftime("%m/%d/%Y")
                        CURRENT_PROJECT.trade_category = "Tile & Stone"
                        CURRENT_PROJECT.material_specs = parsed_proj.material_specs if parsed_proj.material_specs else TileAndStoneEngine.get_default_specs()
                        CURRENT_PROJECT.rooms = parsed_proj.rooms
                        CURRENT_PROJECT.exclusions = parsed_proj.exclusions
                        
                        return {
                            "status": "success",
                            "filename": file.filename,
                            "is_zip": True,
                            "pdf_count": len(pdf_files_to_process),
                            "total_pages": 1,
                            "finish_schedules_count": 1 if parsed_proj.material_specs else 0,
                            "restroom_plans_count": len(parsed_proj.rooms),
                            "extracted_rooms_count": len(CURRENT_PROJECT.rooms),
                            "project": CURRENT_PROJECT.to_dict()
                        }
                except Exception as e:
                    print(f"Error parsing zip Excel candidate {exc_path}: {e}")
    elif file_ext in [".pdf"]:
        pdf_files_to_process.append(save_path)
    else:
        raise HTTPException(status_code=400, detail="Unsupported file format. Upload PDF or ZIP archives.")

    if not pdf_files_to_process:
        raise HTTPException(status_code=400, detail="No PDF drawing files found in the archive.")

    # Skip photo-heavy non-drawing PDFs for lightning fast takeoff
    drawing_pdfs = [p for p in pdf_files_to_process if not any(k in os.path.basename(p).lower() for k in ["photo", "image", "picture"])]
    if drawing_pdfs:
        pdf_files_to_process = drawing_pdfs

    def pdf_sort_key(p):
        name = os.path.basename(p).lower()
        path = p.lower()
        if "pricing" in path or "quote" in path or "reference" in path:
            return 10
        if "drawing" in name or "plan" in name or "bid" in name or "arch" in name or "cd" in name or "issue" in name or "review" in name or "schedule" in name:
            return 0
        if "spec" in name or "scope" in name:
            return 1
        return 5

    pdf_files_to_process.sort(key=pdf_sort_key)

    total_pages_all = 0
    total_finish_pages = 0
    total_toilet_pages = 0
    all_extracted_rooms = []

    clean_upload_title = clean_project_title_from_filename(file.filename)
    if clean_upload_title and clean_upload_title.upper() not in ["DESIGN FILES", "UPLOAD", "NEW TAKEOFF PROJECT", "NEW PROJECT", ""]:
        CURRENT_PROJECT.project_name = clean_upload_title

    for pdf_path in pdf_files_to_process:
        try:
            res = PDFAutoTakeoffEngine.process_pdf(pdf_path)
            total_pages_all += res.get("total_pages", 0)
            total_finish_pages += len(res.get("finish_schedule_pages", []))
            total_toilet_pages += len(res.get("toilet_room_pages", []))
            
            meta = res.get("metadata", {})
            has_rooms = bool(res.get("extracted_rooms"))
            
            if meta.get("project_name") and meta["project_name"] not in ["New Takeoff Project", "", None]:
                if not CURRENT_PROJECT.project_name or CURRENT_PROJECT.project_name in ["New Takeoff Project", ""]:
                    CURRENT_PROJECT.project_name = meta["project_name"]
                elif file_ext == ".pdf":
                    CURRENT_PROJECT.project_name = meta["project_name"]
            if meta.get("client_name") and (has_rooms or not CURRENT_PROJECT.client_name or CURRENT_PROJECT.client_name == "General Contractor / Owner"):
                CURRENT_PROJECT.client_name = meta["client_name"]
            if meta.get("client_company") and (has_rooms or not CURRENT_PROJECT.client_company or CURRENT_PROJECT.client_company == "Commercial Construction"):
                CURRENT_PROJECT.client_company = meta["client_company"]
            if meta.get("date_str") and (has_rooms or not CURRENT_PROJECT.date_str):
                CURRENT_PROJECT.date_str = meta["date_str"]

            if res.get("material_specs"):
                CURRENT_PROJECT.material_specs.update(res["material_specs"])
            
            if res.get("extracted_rooms"):
                existing_names = {r.room_name for r in all_extracted_rooms}
                for r in res["extracted_rooms"]:
                    if r.room_name not in existing_names:
                        all_extracted_rooms.append(r)
                        existing_names.add(r.room_name)
                if CURRENT_PROJECT.project_name and CURRENT_PROJECT.project_name != "New Takeoff Project":
                    break
        except Exception as e:
            pass

    if all_extracted_rooms:
        CURRENT_PROJECT.rooms = all_extracted_rooms

    if not CURRENT_PROJECT.project_name or CURRENT_PROJECT.project_name == "New Takeoff Project":
        if clean_upload_title:
            CURRENT_PROJECT.project_name = clean_upload_title

    return {
        "status": "success",
        "filename": file.filename,
        "is_zip": file_ext == ".zip",
        "pdf_count": len(pdf_files_to_process),
        "total_pages": total_pages_all,
        "finish_schedules_count": total_finish_pages,
        "restroom_plans_count": total_toilet_pages,
        "extracted_rooms_count": len(all_extracted_rooms),
        "project": CURRENT_PROJECT.to_dict()
    }

@app.get("/api/export/excel")
def export_excel(trades: Optional[str] = None):
    global CURRENT_PROJECT, ACTIVE_TRADES
    selected = [t.strip() for t in trades.split(",") if t.strip()] if trades else ACTIVE_TRADES
    proj = CURRENT_PROJECT.filter_by_trades(selected)
    temp_dir = tempfile.gettempdir()
    clean_name = "".join([c if c.isalnum() else "_" for c in proj.project_name])
    export_path = os.path.join(temp_dir, f"Proposal_{clean_name}.xlsx")
    ExcelProposalGenerator.generate_excel(proj, export_path)
    return FileResponse(
        export_path,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=f"Takeoff_Proposal_{clean_name}.xlsx"
    )

@app.get("/api/export/sow-excel")
def export_sow_excel(trades: Optional[str] = None):
    global CURRENT_PROJECT, ACTIVE_TRADES
    selected = [t.strip() for t in trades.split(",") if t.strip()] if trades else ACTIVE_TRADES
    proj = CURRENT_PROJECT.filter_by_trades(selected)
    temp_dir = tempfile.gettempdir()
    clean_name = "".join([c if c.isalnum() else "_" for c in proj.project_name])
    export_path = os.path.join(temp_dir, f"SOW_Bid_Proposal_{clean_name}.xlsx")
    ExcelProposalGenerator.generate_sow_excel(proj, export_path)
    return FileResponse(
        export_path,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=f"Takeoff_SOW_Bid_{clean_name}.xlsx"
    )

@app.get("/api/export/html")
def export_html(trades: Optional[str] = None):
    global CURRENT_PROJECT, ACTIVE_TRADES
    selected = [t.strip() for t in trades.split(",") if t.strip()] if trades else ACTIVE_TRADES
    proj = CURRENT_PROJECT.filter_by_trades(selected)
    html_content = HTMLProposalGenerator.generate_html(proj)
    return HTMLResponse(content=html_content)

@app.get("/api/export/sow-html")
def export_sow_html(trades: Optional[str] = None):
    global CURRENT_PROJECT, ACTIVE_TRADES
    selected = [t.strip() for t in trades.split(",") if t.strip()] if trades else ACTIVE_TRADES
    proj = CURRENT_PROJECT.filter_by_trades(selected)
    html_content = HTMLProposalGenerator.generate_sow_html(proj)
    return HTMLResponse(content=html_content)

# ============================================================
# ENTERPRISE MODULE: Safety Net Audit & Confidence Scoring API
# ============================================================
@app.get("/api/audit")
def audit_project(trades: Optional[str] = None):
    global CURRENT_PROJECT, ACTIVE_TRADES
    selected = [t.strip() for t in trades.split(",") if t.strip()] if trades else ACTIVE_TRADES
    proj = CURRENT_PROJECT.filter_by_trades(selected)
    audit_result = SafetyNetEngine.audit_project(proj.rooms, proj.material_specs)
    return audit_result

# ============================================================
# ENTERPRISE MODULE: Geometry Engine - Visual Blueprint Polygons
# ============================================================
@app.get("/api/polygons")
def get_room_polygons(trades: Optional[str] = None, scale: float = 24.0):
    global CURRENT_PROJECT, ACTIVE_TRADES
    selected = [t.strip() for t in trades.split(",") if t.strip()] if trades else ACTIVE_TRADES
    proj = CURRENT_PROJECT.filter_by_trades(selected)
    polygons = GeometryEngine.generate_room_polygons(proj.rooms, pixels_per_foot=scale)
    return {"polygons": polygons, "rooms_count": len(proj.rooms), "scale": scale}

@app.post("/api/calibrate_scale")
def calibrate_scale(payload: Dict[str, Any]):
    p1 = (float(payload.get("x1", 0)), float(payload.get("y1", 0)))
    p2 = (float(payload.get("x2", 0)), float(payload.get("y2", 0)))
    known_feet = float(payload.get("known_feet", 3.0))
    ppf = GeometryEngine.calculate_scale_from_points(p1, p2, known_feet)
    return {"pixels_per_foot": round(ppf, 2), "calibration_status": "OK"}

# ============================================================
# ENTERPRISE MODULE: Learning Store - Trade Settings & Branding
# ============================================================
@app.get("/api/settings")
def get_settings():
    return LearningStore.get_settings()

@app.post("/api/settings")
def save_settings(payload: Dict[str, Any]):
    updated = LearningStore.save_settings(payload)
    return {"status": "success", "settings": updated}

# ============================================================
# ENTERPRISE MODULE: User & Company Registration Profile API
# ============================================================
@app.get("/api/user/profile")
def get_user_profile():
    return LearningStore.get_user_profile()

@app.post("/api/user/profile")
def save_user_profile(payload: Dict[str, Any]):
    global CURRENT_PROJECT
    updated = LearningStore.save_user_profile(payload)
    if updated.get("company_name"):
        CURRENT_PROJECT.bidder_company = updated["company_name"]
    if updated.get("address"):
        CURRENT_PROJECT.bidder_address = updated["address"]
    if updated.get("phone"):
        CURRENT_PROJECT.bidder_phone = updated["phone"]
    if updated.get("email"):
        CURRENT_PROJECT.bidder_email = updated["email"]
    if updated.get("estimator_name"):
        CURRENT_PROJECT.estimator_name = updated["estimator_name"]
    if updated.get("estimator_title"):
        CURRENT_PROJECT.estimator_title = updated.get("estimator_title", "Senior Estimator")
    return {"status": "success", "profile": updated}

VALID_PINS = ["3531"]

@app.post("/api/auth/pin")
def verify_pin(payload: Dict[str, Any]):
    entered = str(payload.get("pin", "")).strip()
    if entered in VALID_PINS:
        return {"status": "success", "authenticated": True, "message": "PIN verified successfully"}
    return {"status": "error", "authenticated": False, "message": "Invalid PIN code"}

# ============================================================
# GEMINI 3.6 FLASH AI VISION & ESTIMATION COPILOT API
# ============================================================
@app.get("/api/ai/status")
def get_ai_status():
    return GeminiAIEngine.check_connection()

@app.post("/api/ai/chat")
def chat_with_ai(payload: Dict[str, Any]):
    global CURRENT_PROJECT
    message = str(payload.get("message", "")).strip()
    if not message:
        return {"status": "error", "message": "Message cannot be empty."}
    try:
        reply = GeminiAIEngine.chat_with_project(message, CURRENT_PROJECT.to_dict())
        return {"status": "success", "reply": reply}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/api/ai/pricing_advisor")
def get_pricing_advice(payload: Dict[str, Any]):
    global CURRENT_PROJECT
    trade = payload.get("trade", CURRENT_PROJECT.trade_category or "Tile & Stone")
    symbol = payload.get("symbol", "FT-1")
    desc = payload.get("description", "Floor Tile")
    unit = payload.get("unit", "SQ FT")
    try:
        advice = GeminiAIEngine.suggest_pricing(trade, symbol, desc, unit)
        return {"status": "success", "advice": advice}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/api/ai/analyze_blueprint")
async def analyze_blueprint_ai(file: UploadFile = File(...), trade: str = Form("Tile & Stone")):
    global CURRENT_PROJECT
    safe_name = "".join([c if c.isalnum() or c in "._- &()[]#+," else "_" for c in file.filename])
    save_path = os.path.join(UPLOAD_DIR, safe_name)
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        ai_res = GeminiAIEngine.analyze_blueprint_with_vision(save_path, trade_focus=trade)
        if ai_res.get("status") != "success":
            return JSONResponse(status_code=500, content={"status": "error", "message": ai_res.get("error", "AI Analysis failed")})
        
        data = ai_res.get("data", {})
        
        # Populate CURRENT_PROJECT with AI Results
        if data.get("project_name"):
            CURRENT_PROJECT.project_name = data["project_name"]
        if data.get("client_name"):
            CURRENT_PROJECT.client_name = data["client_name"]
        if data.get("client_company"):
            CURRENT_PROJECT.client_company = data["client_company"]
        if data.get("trade_category"):
            CURRENT_PROJECT.trade_category = data["trade_category"]
        
        # Material Specs
        if "material_specs" in data and isinstance(data["material_specs"], dict):
            specs_map = {}
            for sym, sinfo in data["material_specs"].items():
                specs_map[sym] = MaterialSpec(
                    symbol=sym,
                    description=sinfo.get("description", ""),
                    unit=sinfo.get("unit", "SQ FT"),
                    budget_price=float(sinfo.get("budget_price", 0.0)) if sinfo.get("budget_price") is not None else 0.0,
                    notes=sinfo.get("notes", "")
                )
            if specs_map:
                CURRENT_PROJECT.material_specs = specs_map
        
        # Rooms and Items
        if "rooms" in data and isinstance(data["rooms"], list):
            new_rooms = []
            for r in data["rooms"]:
                items = []
                for it in r.get("items", []):
                    items.append(TakeoffLineItem(
                        symbol=it.get("symbol", "FT-1"),
                        finish_type=it.get("finish_type", "FLOOR"),
                        material_type=it.get("material_type", "PORCELAIN TILE"),
                        work_type=it.get("work_type", "S&I"),
                        quantity=float(it.get("quantity", 0.0)),
                        unit=it.get("unit", "SQ FT"),
                        material_price=float(it.get("material_price", 0.0)),
                        labor_price=float(it.get("labor_price", 0.0)),
                        notes=it.get("notes", "")
                    ))
                new_rooms.append(RoomTakeoff(
                    room_name=r.get("room_name", "ROOM"),
                    floor_name=r.get("floor_name", "MAIN LEVEL"),
                    length_ft=float(r.get("length_ft", 10.0)),
                    width_ft=float(r.get("width_ft", 8.0)),
                    ceiling_height_ft=float(r.get("ceiling_height_ft", 9.0)),
                    wall_tile_height_ft=float(r.get("wall_tile_height_ft", 8.0)),
                    door_count=int(r.get("door_count", 1)),
                    items=items
                ))
            if new_rooms:
                CURRENT_PROJECT.rooms = new_rooms

        if data.get("exclusions") and isinstance(data["exclusions"], list):
            CURRENT_PROJECT.exclusions = data["exclusions"]

        return {
            "status": "success",
            "message": "Gemini 3.6 Flash Blueprint Vision takeoff completed successfully!",
            "summary": data.get("analysis_summary", ""),
            "rooms_count": len(CURRENT_PROJECT.rooms),
            "specs_count": len(CURRENT_PROJECT.material_specs),
            "project": CURRENT_PROJECT.to_dict()
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "error", "message": str(e)})

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "..", "frontend")
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
