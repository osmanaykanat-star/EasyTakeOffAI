import math
from typing import List, Dict, Optional
from .trade_base import RoomTakeoff, TakeoffLineItem, MaterialSpec

class CommercialFlooringEngine:
    """
    Core Estimation Engine for Commercial Flooring (Non-Tile):
    Implements industry standard rules for Carpet Tile, Luxury Vinyl Tile (LVT),
    Vinyl Composition Tile (VCT), Hardwood, Rubber Base, and Self-Leveling.
    """

    @staticmethod
    def get_default_specs() -> Dict[str, MaterialSpec]:
        return {
            "CPT-TILE-24X24": MaterialSpec(
                symbol="CPT-TILE-24X24",
                description="Interface / Shaw Contract 24x24 Modular Carpet Tile (Direct Glue)",
                unit="SQ FT",
                budget_price=3.95,
                notes="Heavy commercial traffic rating",
                trade="Commercial Flooring"
            ),
            "LVT-PLANK-20MIL": MaterialSpec(
                symbol="LVT-PLANK-20MIL",
                description="Commercial Luxury Vinyl Plank (LVT) 7x48 with 20mil Commercial Wear Layer",
                unit="SQ FT",
                budget_price=4.75,
                notes="Waterproof commercial flooring",
                trade="Commercial Flooring"
            ),
            "VCT-TILE-12X12": MaterialSpec(
                symbol="VCT-TILE-12X12",
                description="Armstrong Standard Excelon 12x12 Vinyl Composition Tile (VCT)",
                unit="SQ FT",
                budget_price=2.25,
                notes="High-durability utility & retail flooring",
                trade="Commercial Flooring"
            ),
            "WOOD-ENG-OAK": MaterialSpec(
                symbol="WOOD-ENG-OAK",
                description="European White Oak 5/8 in Engineered Hardwood Flooring (Nail/Glue Down)",
                unit="SQ FT",
                budget_price=9.50,
                notes="High-end executive & residential flooring",
                trade="Commercial Flooring"
            ),
            "RB-BASE-4IN": MaterialSpec(
                symbol="RB-BASE-4IN",
                description="Johnsonite / Roppe 4 in Commercial Thermoset Rubber Wall Base (1/8 in Gauge)",
                unit="LN FT",
                budget_price=2.10,
                notes="Perimeter wall base with preformed corners",
                trade="Commercial Flooring"
            ),
            "SUBFLOOR-SELF-LEVEL": MaterialSpec(
                symbol="SUBFLOOR-SELF-LEVEL",
                description="Ardex / Mapei Self-Leveling Subfloor Underlayment (1/4 in Average Lift)",
                unit="SQ FT",
                budget_price=2.35,
                notes="Precision subfloor flatness prep",
                trade="Commercial Flooring"
            ),
            "TRANSITION-REDUCER": MaterialSpec(
                symbol="TRANSITION-REDUCER",
                description="Johnsonite Solid Rubber / Aluminum Flooring Transition Reducer Strip",
                unit="LN FT",
                budget_price=4.50,
                notes="Transition between carpet and hard surface",
                trade="Commercial Flooring"
            )
        }

    @classmethod
    def calculate_room_flooring(cls, room_name: str, length_ft: float, width_ft: float, floor_type: str = "LVT", door_count: int = 1) -> List[TakeoffLineItem]:
        perimeter = 2 * (length_ft + width_ft)
        floor_area = length_ft * width_ft
        base_lnft = max(0.0, perimeter - (door_count * 3.0))
        
        items = []
        items.append(TakeoffLineItem(
            symbol="SUBFLOOR-SELF-LEVEL",
            finish_type="PREPARATION",
            material_type="SELF-LEVELING UNDERLAYMENT",
            work_type="S&I",
            quantity=round(floor_area, 2),
            unit="SQ FT",
            material_price=1.15,
            labor_price=1.20,
            notes="Subfloor Self-Leveling Underlayment & Primer",
            trade="Commercial Flooring"
        ))
        
        if floor_type.upper() == "CARPET":
            f_sym = "CPT-TILE-24X24"
            f_desc = "Interface 24x24 Modular Carpet Tile (Direct Glue-Down)"
            f_mat = "CARPET TILE"
            f_mat_price = 2.45
            f_lab_price = 1.50
        elif floor_type.upper() == "WOOD":
            f_sym = "WOOD-ENG-OAK"
            f_desc = "European White Oak 5/8 in Engineered Hardwood Flooring"
            f_mat = "ENGINEERED HARDWOOD"
            f_mat_price = 6.50
            f_lab_price = 3.00
        elif floor_type.upper() == "VCT":
            f_sym = "VCT-TILE-12X12"
            f_desc = "Armstrong Standard Excelon 12x12 VCT with Commercial Polish"
            f_mat = "VCT TILE"
            f_mat_price = 1.10
            f_lab_price = 1.15
        else: # LVT
            f_sym = "LVT-PLANK-20MIL"
            f_desc = "Commercial Luxury Vinyl Plank (LVT) with 20mil Wear Layer"
            f_mat = "LVT PLANK"
            f_mat_price = 2.95
            f_lab_price = 1.80
            
        items.append(TakeoffLineItem(
            symbol=f_sym,
            finish_type="FLOOR",
            material_type=f_mat,
            work_type="S&I",
            quantity=round(floor_area, 2),
            unit="SQ FT",
            material_price=f_mat_price,
            labor_price=f_lab_price,
            notes=f_desc,
            trade="Commercial Flooring"
        ))
        
        items.append(TakeoffLineItem(
            symbol="RB-BASE-4IN",
            finish_type="BASE",
            material_type="RUBBER BASE",
            work_type="S&I",
            quantity=round(base_lnft, 2),
            unit="LN FT",
            material_price=0.85,
            labor_price=1.25,
            notes="Johnsonite 4 in Thermoset Rubber Cove Base",
            trade="Commercial Flooring"
        ))
        
        if door_count > 0:
            items.append(TakeoffLineItem(
                symbol="TRANSITION-REDUCER",
                finish_type="FLOOR",
                material_type="RUBBER TRANSITION",
                work_type="S&I",
                quantity=round(door_count * 3.0, 2),
                unit="LN FT",
                material_price=2.00,
                labor_price=2.50,
                notes=f"Transition Reducer Strip at {door_count} Door Opening(s)",
                trade="Commercial Flooring"
            ))
            
        return items
