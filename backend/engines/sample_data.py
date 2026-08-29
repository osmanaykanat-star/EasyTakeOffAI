from ..trades.trade_base import ProjectTakeoff, RoomTakeoff, MaterialSpec, TakeoffLineItem
from ..trades.tile_and_stone import TileAndStoneEngine

def get_zeta_sample_project() -> ProjectTakeoff:
    specs = TileAndStoneEngine.get_default_specs()
    specs.update({
        "TILE-1": MaterialSpec(symbol="TILE-1", description="GENERIC TILE", unit="SQ FT", notes="NO SPEC PROVIDED PLEASE GIVE BUDGET PRICE"),
        "TILE-2": MaterialSpec(symbol="TILE-2", description="GENERIC TILE", unit="SQ FT", notes="NO SPEC PROVIDED PLEASE GIVE BUDGET PRICE"),
        "TILE/BULLNOSE": MaterialSpec(symbol="TILE/BULLNOSE", description="GENERIC BULLNOSE TRIM", unit="LNFT", notes="NO SPEC PROVIDED PLEASE GIVE BUDGET PRICE"),
        "TL-4.1": MaterialSpec(symbol="TL-4.1", description='DALTILE- COLOR WHEEL-MOSAIC SHEET- 2"X2"-ORANGE BURST-FINISH TYPE:SEMI-GLOSS', budget_price=3.06, unit="SQ FT"),
        "TL-4.2": MaterialSpec(symbol="TL-4.2", description='DALTILE- COLOR WHEEL-MOSAIC SHEET- 2"X2"-ARTIC WHITE-FINISH TYPE:SEMI-GLOSS', budget_price=3.06, unit="SQ FT"),
        "TL-4/BULLNOSE": MaterialSpec(symbol="TL-4/BULLNOSE", description='DALTILE- COLOR WHEEL-JOLLY TRIM- 1.5"X12"-DESERT GREY-FINISH TYPE:SEMI-GLOSS', budget_price=1.79, unit="LNFT")
    })

    r1 = RoomTakeoff(
        room_name="WC 122A",
        floor_name="1ST FLOOR",
        length_ft=7.5,
        width_ft=6.6,
        ceiling_height_ft=9.0,
        door_count=1,
        items=[
            TakeoffLineItem(symbol="TL-5", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=49.47, unit="SQ FT", material_price=0.0, labor_price=0.0),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="STONE", work_type="S&I", quantity=1.0, unit="PCS", material_price=0.0, labor_price=0.0),
            TakeoffLineItem(symbol="TILE-1", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=86.45, unit="SQ FT", material_price=0.0, labor_price=0.0),
            TakeoffLineItem(symbol="TILE-2", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=86.45, unit="SQ FT", material_price=0.0, labor_price=0.0),
            TakeoffLineItem(symbol="TILE/BULLNOSE", finish_type="TRIM/BULLNOSE", material_type="BULLNOSE", work_type="S&I", quantity=24.69, unit="LNFT", material_price=0.0, labor_price=0.0),
            TakeoffLineItem(symbol="EPOXY", finish_type="FLOOR & WALL", material_type="PREP MATERIAL", work_type="S&I", quantity=222.37, unit="SQ FT", material_price=0.0, labor_price=0.0),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR & WALL", material_type="PREP MATERIAL", work_type="S&I", quantity=49.47, unit="SQ FT", material_price=0.0, labor_price=0.0),
            TakeoffLineItem(symbol="MUDSET", finish_type="FLOOR", material_type="PREP MATERIAL", work_type="S&I", quantity=49.47, unit="SQ FT", material_price=0.0, labor_price=0.0)
        ]
    )

    r2 = RoomTakeoff(
        room_name="BOYS BATH 711",
        floor_name="7TH FLOOR",
        length_ft=12.0,
        width_ft=10.0,
        door_count=1,
        items=[
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="STONE", work_type="S&I", quantity=1.0, unit="PCS", material_price=0.0, labor_price=0.0),
            TakeoffLineItem(symbol="TL-3.1", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=49.45, unit="SQ FT", material_price=3.06, labor_price=0.0),
            TakeoffLineItem(symbol="TL-3.2", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=115.31, unit="SQ FT", material_price=3.06, labor_price=0.0),
            TakeoffLineItem(symbol="TL-3.3", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=59.30, unit="SQ FT", material_price=3.06, labor_price=0.0),
            TakeoffLineItem(symbol="TL-3.4", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=59.30, unit="SQ FT", material_price=3.06, labor_price=0.0),
            TakeoffLineItem(symbol="TL-3.5", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=46.10, unit="SQ FT", material_price=3.06, labor_price=0.0),
            TakeoffLineItem(symbol="TL-3/BULLNOSE", finish_type="TRIM/BULLNOSE", material_type="BULLNOSE", work_type="S&I", quantity=49.17, unit="LNFT", material_price=1.79, labor_price=0.0),
            TakeoffLineItem(symbol="EPOXY", finish_type="FLOOR & WALL", material_type="PREP MATERIAL", work_type="S&I", quantity=329.46, unit="SQ FT", material_price=0.0, labor_price=0.0)
        ]
    )

    r3 = RoomTakeoff(
        room_name="GIRLS BATH 712",
        floor_name="7TH FLOOR",
        length_ft=12.0,
        width_ft=12.0,
        door_count=1,
        items=[
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="STONE", work_type="S&I", quantity=1.0, unit="PCS", material_price=0.0, labor_price=0.0),
            TakeoffLineItem(symbol="TL-4.1", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=55.88, unit="SQ FT", material_price=3.06, labor_price=0.0),
            TakeoffLineItem(symbol="TL-4.2", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=207.63, unit="SQ FT", material_price=3.06, labor_price=0.0),
            TakeoffLineItem(symbol="TL-4/BULLNOSE", finish_type="TRIM/BULLNOSE", material_type="BULLNOSE", work_type="S&I", quantity=65.40, unit="LNFT", material_price=1.79, labor_price=0.0),
            TakeoffLineItem(symbol="EPOXY", finish_type="FLOOR & WALL", material_type="PREP MATERIAL", work_type="S&I", quantity=328.91, unit="SQ FT", material_price=0.0, labor_price=0.0)
        ]
    )

    return ProjectTakeoff(
        project_name="Zeta Charter Schools - South Bronx Middle School Renovation",
        client_name="Romina Rodriguez",
        client_company="SPK/Lewis Construction",
        estimator_name="",
        trade_category="Tile & Stone",
        rooms=[r1, r2, r3],
        material_specs=specs
    )

def get_ls_power_sample_project() -> ProjectTakeoff:
    specs = {
        "OPT1/TILE-1/SHOWER": MaterialSpec(symbol="OPT1/TILE-1/SHOWER", description='NEMO- GLOW-2"X10"-VANILLA- FINISH TYPE:MATTE', budget_price=12.2, unit="SQ FT"),
        "OPT1/WATERPROOF": MaterialSpec(symbol="OPT1/WATERPROOF", description="GENERIC WATERPROOF", unit="SQ FT"),
        "OPT2/METAL TRIMS/SADDLE": MaterialSpec(symbol="OPT2/METAL TRIMS/SADDLE", description="GENERIC METAL SADDLE (SCHLUTER RENO-T)", budget_price=6.34, unit="LNFT"),
        "OPT2/TILE-1/SHOWER": MaterialSpec(symbol="OPT2/TILE-1/SHOWER", description='NEMO- GLOW-2"X10"-VANILLA- FINISH TYPE:MATTE', budget_price=12.2, unit="SQ FT"),
        "OPT2/TILE-2/SHOWER": MaterialSpec(symbol="OPT2/TILE-2/SHOWER", description="STONEPEAK-HIGHLAND COLLECTION-WHITE-FINISH TYPE:MATTE", budget_price=7.15, unit="SQ FT"),
        "OPT3/SADDLE": MaterialSpec(symbol="OPT3/SADDLE", description="GENERIC STONE SADDLE", budget_price=100.0, unit="PCS"),
        "OPT3/TILE-3": MaterialSpec(symbol="OPT3/TILE-3", description='NEMO-CASABLANCA 2.0- 5"X5"-SOLID COLOR-FINISH TYPE: MATTE', budget_price=7.82, unit="SQ FT")
    }

    r1 = RoomTakeoff(
        room_name="RESTROOM",
        floor_name="MAIN FLOOR/OPT 1",
        items=[
            TakeoffLineItem(symbol="OPT1/TILE-1/SHOWER", finish_type="WALL", material_type="TILE", quantity=154.56, unit="SQ FT", material_price=12.2),
            TakeoffLineItem(symbol="OPT1/WATERPROOF", finish_type="WALL", material_type="PREP MATERIAL", quantity=154.56, unit="SQ FT")
        ]
    )

    r2 = RoomTakeoff(
        room_name="RESTROOM",
        floor_name="MAIN FLOOR/OPT 2",
        items=[
            TakeoffLineItem(symbol="OPT2/METAL TRIMS/SADDLE", finish_type="FLOOR", material_type="METAL TRIM", quantity=2.91, unit="LNFT", material_price=6.34),
            TakeoffLineItem(symbol="OPT2/TILE-1/SHOWER", finish_type="WALL", material_type="TILE", quantity=154.56, unit="SQ FT", material_price=12.2),
            TakeoffLineItem(symbol="OPT2/TILE-2/SHOWER", finish_type="FLOOR", material_type="TILE", quantity=20.1, unit="SQ FT", material_price=7.15),
            TakeoffLineItem(symbol="OPT2/WATERPROOF", finish_type="WALL&FLOOR", material_type="PREP MATERIAL", quantity=174.66, unit="SQ FT"),
            TakeoffLineItem(symbol="OPT2/MUDSET", finish_type="FLOOR", material_type="PREP MATERIAL", quantity=20.1, unit="SQ FT")
        ]
    )

    return ProjectTakeoff(
        project_name="LS Power - Tile Work",
        client_name="Luke Greco",
        client_company="SPK LEWIS",
        estimator_name="",
        trade_category="Tile & Stone",
        rooms=[r1, r2],
        material_specs=specs
    )


def get_200_cps_sample_project() -> ProjectTakeoff:
    res = PDFAutoTakeoffEngine.process_pdf(r"C:\Users\azran\.gemini\antigravity\scratch\EasyTakeOffAI\uploads\extracted_DESIGN FILES-20260825T184239Z-1-001\DESIGN FILES\pricing for large floor tiling.pdf")
    meta = res.get("metadata", {})
    return ProjectTakeoff(
        project_name=meta.get("project_name", "[2827] 200 CPS"),
        client_name=meta.get("client_name", "GENCER HEPOZDEN"),
        client_company=meta.get("client_company", "TEMA BUILDERS GROUP"),
        estimator_name="",
        date_str="07/17/2026",
        trade_category="Tile & Stone",
        rooms=res.get("extracted_rooms", []),
        material_specs=res.get("material_specs", {}),
        exclusions=[
            "1) Counter Top",
            "2) Epoxy Grout",
            "3) Air freight any material."
        ]
    )
