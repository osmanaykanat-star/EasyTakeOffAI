import math
from typing import List, Dict, Optional
from .trade_base import RoomTakeoff, TakeoffLineItem, MaterialSpec

class PaintingAndCoatingsEngine:
    """
    Core Estimation Engine for Painting & Wall Coverings:
    Implements industry standard rules for drywall priming, 2-coat architectural paint,
    high-traffic scrubbable coatings, door frame enamel, and epoxy coatings.
    """

    @staticmethod
    def get_default_specs() -> Dict[str, MaterialSpec]:
        return {
            "PAINT-PRIME": MaterialSpec(
                symbol="PAINT-PRIME",
                description="Commercial High-Build PVA Drywall Primer & Sealer",
                unit="SQ FT",
                budget_price=0.45,
                notes="Essential base coat for new drywall",
                trade="Painting & Finishes"
            ),
            "PAINT-EGGSHELL": MaterialSpec(
                symbol="PAINT-EGGSHELL",
                description="Benjamin Moore Scuff-X Commercial Eggshell (2 Coats)",
                unit="SQ FT",
                budget_price=1.15,
                notes="High-traffic scrubbable interior wall finish",
                trade="Painting & Finishes"
            ),
            "PAINT-SEMI-GLOSS": MaterialSpec(
                symbol="PAINT-SEMI-GLOSS",
                description="Benjamin Moore Ultra Spec 500 Semi-Gloss Latex Enamel (2 Coats)",
                unit="SQ FT",
                budget_price=1.35,
                notes="Restrooms, kitchens, door frames, and wet areas",
                trade="Painting & Finishes"
            ),
            "PAINT-CEIL-FLAT": MaterialSpec(
                symbol="PAINT-CEIL-FLAT",
                description="Benjamin Moore Waterborne Ceiling Ultra-Flat White Latex",
                unit="SQ FT",
                budget_price=0.85,
                notes="Non-reflective ceiling paint",
                trade="Painting & Finishes"
            ),
            "DOOR-FRAME-ENAMEL": MaterialSpec(
                symbol="DOOR-FRAME-ENAMEL",
                description="Direct-to-Metal (DTM) Acrylic Enamel for Hollow Metal Frames",
                unit="LN FT",
                budget_price=1.85,
                notes="Door frame perimeter painting",
                trade="Painting & Finishes"
            ),
            "EPOXY-WALL-COATING": MaterialSpec(
                symbol="EPOXY-WALL-COATING",
                description="High-Performance 2-Part Seamless Epoxy Wall Coating",
                unit="SQ FT",
                budget_price=3.25,
                notes="Sterile medical and commercial kitchen walls",
                trade="Painting & Finishes"
            )
        }

    @classmethod
    def calculate_room_painting(cls, room_name: str, length_ft: float, width_ft: float, ceiling_height_ft: float, door_count: int = 1, is_wet_area: bool = False) -> List[TakeoffLineItem]:
        perimeter = 2 * (length_ft + width_ft)
        wall_area = perimeter * ceiling_height_ft
        ceiling_area = length_ft * width_ft
        frame_lnft = door_count * 20.0  # Approx 20 LF per 3x7 door frame
        
        items = []
        items.append(TakeoffLineItem(
            symbol="PAINT-PRIME",
            finish_type="PREPARATION",
            material_type="PRIMER",
            work_type="S&I",
            quantity=round(wall_area, 2),
            unit="SQ FT",
            material_price=0.15,
            labor_price=0.30,
            notes="Commercial High-Build PVA Drywall Primer",
            trade="Painting & Finishes"
        ))
        wall_paint_sym = "PAINT-SEMI-GLOSS" if is_wet_area else "PAINT-EGGSHELL"
        wall_paint_desc = "Benjamin Moore Semi-Gloss Latex (2 Coats)" if is_wet_area else "Benjamin Moore Scuff-X Eggshell (2 Coats)"
        items.append(TakeoffLineItem(
            symbol=wall_paint_sym,
            finish_type="WALL",
            material_type="ARCHITECTURAL PAINT",
            work_type="S&I",
            quantity=round(wall_area, 2),
            unit="SQ FT",
            material_price=0.35,
            labor_price=0.80,
            notes=wall_paint_desc,
            trade="Painting & Finishes"
        ))
        items.append(TakeoffLineItem(
            symbol="PAINT-CEIL-FLAT",
            finish_type="CEILING",
            material_type="CEILING PAINT",
            work_type="S&I",
            quantity=round(ceiling_area, 2),
            unit="SQ FT",
            material_price=0.25,
            labor_price=0.60,
            notes="Benjamin Moore Waterborne Ceiling Ultra-Flat White",
            trade="Painting & Finishes"
        ))
        if door_count > 0:
            items.append(TakeoffLineItem(
                symbol="DOOR-FRAME-ENAMEL",
                finish_type="TRIM",
                material_type="DTM ENAMEL",
                work_type="S&I",
                quantity=round(frame_lnft, 2),
                unit="LN FT",
                material_price=0.45,
                labor_price=1.40,
                notes=f"DTM Enamel Painting on {door_count} Hollow Metal Door Frame(s)",
                trade="Painting & Finishes"
            ))
        return items
