import re
import os
from typing import Dict, List, Any, Optional
import fitz  # PyMuPDF

class SheetIndexEngine:
    """
    Automated Architectural & Engineering Sheet Index (Drawing List) Extraction Engine.
    Scans the cover pages and initial blueprint sheets to construct a complete index
    of drawings, their disciplines, and their relevance to selected construction trades.
    """

    DISCIPLINE_PREFIXES = {
        "A": "Architectural",
        "ARCH": "Architectural",
        "AD": "Architectural Details / Modular",
        "S": "Structural",
        "STR": "Structural",
        "M": "Mechanical / HVAC",
        "ME": "Mechanical / HVAC",
        "HVAC": "Mechanical / HVAC",
        "P": "Plumbing",
        "PL": "Plumbing",
        "PLBG": "Plumbing",
        "E": "Electrical",
        "EL": "Electrical",
        "ELEC": "Electrical",
        "FA": "Fire Alarm",
        "SP": "Sprinkler / Fire Protection",
        "FP": "Sprinkler / Fire Protection",
        "EN": "Energy / Sustainability",
        "C": "Civil",
        "L": "Landscape",
        "G": "General / Title",
        "T": "Title / Life Safety"
    }

    TRADE_KEYWORDS = {
        "Tile & Stone": [
            "FINISH", "TILE", "PORCELAIN", "CERAMIC", "STONE", "MARBLE",
            "RESTROOM", "TOILET", "BATHROOM", "PANTRY", "JANITOR",
            "A-4", "A-5", "ENLARGED RESTROOM", "FINISH SCHEDULE", "WET WALL"
        ],
        "Flooring & Carpet": [
            "FINISH", "FLOORING", "CARPET", "CPT", "RESILIENT", "VINYL",
            "EPOXY", "LVT", "BASE", "A-4", "FLOOR FINISH"
        ],
        "Drywall & Ceilings": [
            "PARTITION", "WALL TYPES", "CEILING", "RCP", "ACOUSTICAL",
            "ACT", "GYPSUM", "DRYWALL", "A-1", "A-2", "A-6"
        ],
        "Painting": [
            "FINISH", "PAINT", "WALL FINISH", "INTERIOR ELEVATION", "A-4", "A-5"
        ],
        "Modular Walls / Casework": [
            "MODULAR", "WALL PANEL", "CASEWORK", "MILLWORK", "CABINET",
            "STRUT", "VAULT", "AD.", "INTERIOR ELEVATION"
        ],
        "Plumbing": [
            "PLUMBING", "PLBG", "FIXTURE", "RISER", "SANITARY", "WATER", "P-", "PL-"
        ],
        "HVAC & Mechanical": [
            "MECHANICAL", "HVAC", "DUCT", "AIR", "VENTILATION", "M-", "ME-"
        ],
        "Electrical": [
            "ELECTRICAL", "LIGHTING", "POWER", "PANEL", "ELEC", "E-"
        ]
    }

    @classmethod
    def extract_sheet_index(cls, pdf_path: str, max_scan_pages: int = 5) -> Dict[str, Any]:
        """
        Scans the first `max_scan_pages` of a blueprint PDF to extract:
        1. List of drawings (Sheet Number, Sheet Title, Discipline, Page Index)
        2. Trade-relevance mapping
        3. Project metadata (Total Floors, Building Type, Zoning/Code)
        """
        if not os.path.exists(pdf_path):
            return {"sheets": [], "trade_relevance": {}, "project_type": "Unknown", "detected_floors": 1}

        try:
            doc = fitz.open(pdf_path)
        except Exception:
            return {"sheets": [], "trade_relevance": {}, "project_type": "Unknown", "detected_floors": 1}

        sheets_found = []
        full_cover_text = ""
        total_pages = len(doc)
        pages_to_scan = min(max_scan_pages, total_pages)

        for p_idx in range(pages_to_scan):
            page = doc[p_idx]
            text = page.get_text()
            full_cover_text += f"\n--- PAGE {p_idx+1} ---\n" + text
            page_sheets = cls._parse_sheet_lines(text, p_idx + 1)
            sheets_found.extend(page_sheets)

        # Detect total floors mentioned in drawings or index
        detected_floors = cls._detect_floors(full_cover_text, total_pages)

        # Classify building / project type
        project_type = cls._detect_project_type(full_cover_text, total_pages)

        # Map sheet relevance to trades
        trade_relevance = cls._map_sheets_to_trades(sheets_found)

        return {
            "sheets": sheets_found,
            "total_drawings": len(sheets_found),
            "project_type": project_type,
            "detected_floors": detected_floors,
            "trade_relevance": trade_relevance,
            "total_pdf_pages": total_pages
        }

    @classmethod
    def _parse_sheet_lines(cls, text: str, page_num: int) -> List[Dict[str, Any]]:
        """Parses lines of text looking for sheet number and title patterns."""
        sheets = []
        lines = [l.strip() for l in text.split("\n") if l.strip()]

        # Regex for standard architectural sheet numbers: A-001, A-101.00, AD.01, S-101, M-001, SP-1
        pattern = re.compile(r'\b([A-Z]{1,4}[-.]\d{1,4}(?:\.\d{1,2})?)\b\s*(?:[-–:]\s*)?([A-Za-z0-9\s,&/\'\(\)\.\-]+)?')

        seen_numbers = set()
        for i, line in enumerate(lines):
            match = pattern.search(line)
            if match:
                sheet_no = match.group(1).upper()
                if sheet_no in seen_numbers or len(sheet_no) < 3:
                    continue

                # Title could be in group 2 or next line
                raw_title = match.group(2) or ""
                if len(raw_title.strip()) < 3 and i + 1 < len(lines):
                    next_line = lines[i + 1]
                    if not pattern.search(next_line) and len(next_line) < 60:
                        raw_title = next_line

                clean_title = raw_title.strip()
                if not clean_title or clean_title.upper() in ["NO", "DATE", "REV", "SHEET"]:
                    continue

                disc = cls._classify_discipline(sheet_no, clean_title)
                seen_numbers.add(sheet_no)
                sheets.append({
                    "sheet_number": sheet_no,
                    "sheet_title": clean_title,
                    "discipline": disc,
                    "found_on_page": page_num
                })

        return sheets

    @classmethod
    def _classify_discipline(cls, sheet_no: str, sheet_title: str) -> str:
        clean_no = sheet_no.upper().replace("-", "").replace(".", "")
        title_upper = sheet_title.upper()

        if "MODULAR" in title_upper:
            return "Modular Walls"
        if "FINISH" in title_upper:
            return "Finishes & Schedules"
        if "RESTROOM" in title_upper or "TOILET" in title_upper:
            return "Restrooms & Wet Areas"

        for pfx, disc in sorted(cls.DISCIPLINE_PREFIXES.items(), key=lambda x: -len(x[0])):
            if clean_no.startswith(pfx):
                return disc

        return "Architectural"

    @classmethod
    def _detect_floors(cls, text: str, total_pages: int) -> int:
        text_upper = text.upper()
        # Look for explicit floor counts: "5-STORY", "5 STORIES", "FLOORS 1 TO 5", "5TH FLOOR"
        floor_matches = re.findall(r'\b(\d{1,2})(?:TH|ST|ND|RD)?\s*(?:STORY|STORIES|FLOOR|LEVELS)\b', text_upper)
        max_floor = 1
        for m in floor_matches:
            try:
                val = int(m)
                if 1 <= val <= 80:
                    max_floor = max(max_floor, val)
            except ValueError:
                pass

        if "FIFTH FLOOR" in text_upper or "5TH FLOOR" in text_upper or "FLOOR 5" in text_upper:
            max_floor = max(max_floor, 5)
        elif "FOURTH FLOOR" in text_upper or "4TH FLOOR" in text_upper:
            max_floor = max(max_floor, 4)
        elif "THIRD FLOOR" in text_upper or "3RD FLOOR" in text_upper:
            max_floor = max(max_floor, 3)
        elif "SECOND FLOOR" in text_upper or "2ND FLOOR" in text_upper:
            max_floor = max(max_floor, 2)

        return max_floor

    @classmethod
    def _detect_project_type(cls, text: str, total_pages: int) -> str:
        text_upper = text.upper()
        if any(k in text_upper for k in ["COMMERCIAL", "OFFICE", "STORAGE", "FIT OUT", "FIT-OUT", "VAULT"]):
            return "Commercial Fit-Out / High-Rise"
        if any(k in text_upper for k in ["RESIDENTIAL", "APARTMENT", "MULTI-FAMILY", "DWELLING"]):
            return "Multi-Family Residential"
        if any(k in text_upper for k in ["HOSPITAL", "CLINIC", "MEDICAL"]):
            return "Healthcare / Medical"
        if any(k in text_upper for k in ["SCHOOL", "COLLEGE", "UNIVERSITY"]):
            return "Educational"
        if total_pages > 15:
            return "Commercial Multi-Story Facility"
        return "Interior Renovation"

    @classmethod
    def _map_sheets_to_trades(cls, sheets: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        trade_map = {t: [] for t in cls.TRADE_KEYWORDS}

        for sheet in sheets:
            combined_desc = (sheet["sheet_number"] + " " + sheet["sheet_title"]).upper()
            for trade, keywords in cls.TRADE_KEYWORDS.items():
                if any(kw in combined_desc for kw in keywords):
                    trade_map[trade].append(sheet)

        return trade_map

    @classmethod
    def get_sheets_for_trade(cls, index_result: Dict[str, Any], trade: str) -> List[Dict[str, Any]]:
        """Returns the specific sheets required for a given trade (e.g. Tile & Stone)."""
        relevance = index_result.get("trade_relevance", {})
        if trade in relevance and relevance[trade]:
            return relevance[trade]

        # Fuzzy trade matching
        trade_norm = trade.lower().replace("&", "and").replace(" ", "")
        for k, sheets in relevance.items():
            k_norm = k.lower().replace("&", "and").replace(" ", "")
            if trade_norm in k_norm or k_norm in trade_norm:
                return sheets

        return index_result.get("sheets", [])
