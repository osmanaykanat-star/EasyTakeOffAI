import math
from typing import List, Dict, Optional
from .trade_base import RoomTakeoff, TakeoffLineItem, MaterialSpec

class DrywallAndFramingEngine:
    """
    Core Estimation Engine for Drywall & Framing Trade:
    Implements industry standard rules for metal stud framing, fire-rated GWB,
    moisture-resistant drywall, acoustical batt insulation, Level 4/5 taping,
    and drop ceiling grids.
    """

    @staticmethod
    def get_default_specs() -> Dict[str, MaterialSpec]:
        return {
            "STUD-25GA-358": MaterialSpec(
                symbol="STUD-25GA-358",
                description="3-5/8 in 25GA Cold-Formed Metal Studs @ 16 in O.C. with Runners",
                unit="SQ FT",
                budget_price=2.45,
                notes="Standard interior partition framing",
                trade="Drywall & Framing"
            ),
            "STUD-20GA-600": MaterialSpec(
                symbol="STUD-20GA-600",
                description="6 in 20GA Heavy-Duty Structural/Shaft Metal Studs @ 16 in O.C.",
                unit="SQ FT",
                budget_price=3.85,
                notes="High-wall and corridor fire partition framing",
                trade="Drywall & Framing"
            ),
            "GWB-58-TYPE-X": MaterialSpec(
                symbol="GWB-58-TYPE-X",
                description="5/8 in Type X Fire-Rated Gypsum Wallboard (USG Sheetrock)",
                unit="SQ FT",
                budget_price=1.65,
                notes="Standard commercial fire-rated wallboard",
                trade="Drywall & Framing"
            ),
            "GWB-58-MR": MaterialSpec(
                symbol="GWB-58-MR",
                description="5/8 in Moisture-Resistant Gypsum Board (Greenboard / DensArmor)",
                unit="SQ FT",
                budget_price=2.15,
                notes="Restrooms, kitchens, wet areas",
                trade="Drywall & Framing"
            ),
            "SOUND-BATT-R11": MaterialSpec(
                symbol="SOUND-BATT-R11",
                description="3-1/2 in R-11 Mineral Wool Acoustical Sound Attenuation Batts (SAFB)",
                unit="SQ FT",
                budget_price=1.10,
                notes="Sound control partition insulation",
                trade="Drywall & Framing"
            ),
            "TAPE-LEVEL-4": MaterialSpec(
                symbol="TAPE-LEVEL-4",
                description="Level 4 Taping & Joint Compound Finish (3-Coat System + Corner Beads)",
                unit="SQ FT",
                budget_price=0.95,
                notes="Standard commercial paint-ready finish",
                trade="Drywall & Framing"
            ),
            "TAPE-LEVEL-5": MaterialSpec(
                symbol="TAPE-LEVEL-5",
                description="Level 5 Premium Skim Coat Finish (Full Surface Skim for Gloss/Critical Light)",
                unit="SQ FT",
                budget_price=1.75,
                notes="High-end architectural smooth finish",
                trade="Drywall & Framing"
            ),
            "ACT-2X2-GRID": MaterialSpec(
                symbol="ACT-2X2-GRID",
                description="2x2 Heavy-Duty Acoustical Ceiling Tile & Suspension Grid System",
                unit="SQ FT",
                budget_price=4.50,
                notes="Suspended ceiling grid & mineral fiber tiles",
                trade="Drywall & Framing"
            )
        }

    @classmethod
    def calculate_room_framing_drywall(cls, room_name: str, length_ft: float, width_ft: float, ceiling_height_ft: float, is_wet_area: bool = False, level_5: bool = False) -> List[TakeoffLineItem]:
        perimeter = 2 * (length_ft + width_ft)
        wall_area = perimeter * ceiling_height_ft
        ceiling_area = length_ft * width_ft
        
        items = []
        items.append(TakeoffLineItem(
            symbol="STUD-25GA-358",
            finish_type="WALL",
            material_type="METAL STUD FRAMING",
            work_type="S&I",
            quantity=round(wall_area, 2),
            unit="SQ FT",
            material_price=1.20,
            labor_price=1.25,
            notes="3-5/8 in 25GA Metal Studs @ 16 in O.C. with Top & Bottom Track",
            trade="Drywall & Framing"
        ))
        items.append(TakeoffLineItem(
            symbol="SOUND-BATT-R11",
            finish_type="WALL",
            material_type="ACOUSTICAL BATT INSULATION",
            work_type="S&I",
            quantity=round(wall_area, 2),
            unit="SQ FT",
            material_price=0.55,
            labor_price=0.55,
            notes="R-11 Sound Attenuation Mineral Wool Batts",
            trade="Drywall & Framing"
        ))
        drywall_sym = "GWB-58-MR" if is_wet_area else "GWB-58-TYPE-X"
        drywall_desc = "5/8 in Moisture-Resistant Gypsum Board" if is_wet_area else "5/8 in Type X Fire-Rated Gypsum Wallboard"
        items.append(TakeoffLineItem(
            symbol=drywall_sym,
            finish_type="WALL",
            material_type="GYPSUM WALLBOARD",
            work_type="S&I",
            quantity=round(wall_area, 2),
            unit="SQ FT",
            material_price=0.85,
            labor_price=0.80,
            notes=drywall_desc,
            trade="Drywall & Framing"
        ))
        tape_sym = "TAPE-LEVEL-5" if level_5 else "TAPE-LEVEL-4"
        tape_desc = "Level 5 Full Surface Skim Coat" if level_5 else "Level 4 3-Coat Joint Compound & Corner Beads"
        tape_labor = 1.25 if level_5 else 0.70
        items.append(TakeoffLineItem(
            symbol=tape_sym,
            finish_type="PREPARATION",
            material_type="DRYWALL FINISHING",
            work_type="S&I",
            quantity=round(wall_area, 2),
            unit="SQ FT",
            material_price=0.25,
            labor_price=tape_labor,
            notes=tape_desc,
            trade="Drywall & Framing"
        ))
        items.append(TakeoffLineItem(
            symbol="ACT-2X2-GRID",
            finish_type="CEILING",
            material_type="ACOUSTICAL CEILING TILE",
            work_type="S&I",
            quantity=round(ceiling_area, 2),
            unit="SQ FT",
            material_price=2.50,
            labor_price=2.00,
            notes="2x2 Heavy-Duty Suspension Grid & Reveal Edge Acoustic Tiles",
            trade="Drywall & Framing"
        ))
        return items
