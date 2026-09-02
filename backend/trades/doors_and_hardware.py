import math
from typing import List, Dict, Optional
from .trade_base import RoomTakeoff, TakeoffLineItem, MaterialSpec

class DoorsAndHardwareEngine:
    """
    Core Estimation Engine for Doors, Frames & Architectural Hardware:
    Implements industry standard rules for Hollow Metal (HM) frames, solid core wood doors,
    mortise locksets, overhead closers, panic exit hardware, and kickplates.
    """

    @staticmethod
    def get_default_specs() -> Dict[str, MaterialSpec]:
        return {
            "DOOR-HM-FRAME-3X7": MaterialSpec(
                symbol="DOOR-HM-FRAME-3X7",
                description="16GA Welded Hollow Metal (HM) Door Frame 3-0 x 7-0 (90-Min Fire Rated)",
                unit="PCS",
                budget_price=245.0,
                notes="Standard commercial fire-rated frame",
                trade="Doors & Hardware"
            ),
            "DOOR-SC-WOOD-3X7": MaterialSpec(
                symbol="DOOR-SC-WOOD-3X7",
                description="Solid Core Architectural Wood Door 3-0 x 7-0 (Plain Sliced White Oak)",
                unit="PCS",
                budget_price=385.0,
                notes="Interior commercial office door",
                trade="Doors & Hardware"
            ),
            "DOOR-HM-FLUSH-3X7": MaterialSpec(
                symbol="DOOR-HM-FLUSH-3X7",
                description="18GA Hollow Metal Flush Steel Door 3-0 x 7-0 (Fire Rated)",
                unit="PCS",
                budget_price=320.0,
                notes="Stairwell, electrical, and utility room door",
                trade="Doors & Hardware"
            ),
            "HW-SET-OFFICE": MaterialSpec(
                symbol="HW-SET-OFFICE",
                description="Commercial Hardware Set: Schlage ND Mortise Lockset, 3x BB Hinges, Wall Stop",
                unit="SET",
                budget_price=365.0,
                notes="Office entry hardware set",
                trade="Doors & Hardware"
            ),
            "HW-SET-EXIT-CLOSER": MaterialSpec(
                symbol="HW-SET-EXIT-CLOSER",
                description="Panic Hardware Set: Von Duprin 99 Exit Device, LCN 4040XP Closer, Smoke Gasket",
                unit="SET",
                budget_price=850.0,
                notes="Corridor and exit egress door hardware set",
                trade="Doors & Hardware"
            ),
            "HW-KICKPLATE-SS": MaterialSpec(
                symbol="HW-KICKPLATE-SS",
                description="Stainless Steel 10 in x 34 in Door Kickplate (.050 Gauge)",
                unit="PCS",
                budget_price=48.0,
                notes="Door bottom armor protection",
                trade="Doors & Hardware"
            )
        }

    @classmethod
    def calculate_room_doors(cls, room_name: str, door_count: int = 1, is_fire_exit: bool = False, is_wood_door: bool = True) -> List[TakeoffLineItem]:
        if door_count <= 0:
            return []
            
        items = []
        items.append(TakeoffLineItem(
            symbol="DOOR-HM-FRAME-3X7",
            finish_type="DOOR",
            material_type="HM FRAME",
            work_type="S&I",
            quantity=float(door_count),
            unit="PCS",
            material_price=165.0,
            labor_price=80.0,
            notes=f"16GA Welded Hollow Metal Door Frame for {door_count} Opening(s)",
            trade="Doors & Hardware"
        ))
        
        door_sym = "DOOR-SC-WOOD-3X7" if is_wood_door else "DOOR-HM-FLUSH-3X7"
        door_desc = "Solid Core Wood Door 3x7" if is_wood_door else "18GA Hollow Metal Steel Door 3x7"
        door_mat = "WOOD DOOR" if is_wood_door else "HM STEEL DOOR"
        door_mat_price = 265.0 if is_wood_door else 220.0
        
        items.append(TakeoffLineItem(
            symbol=door_sym,
            finish_type="DOOR",
            material_type=door_mat,
            work_type="S&I",
            quantity=float(door_count),
            unit="PCS",
            material_price=door_mat_price,
            labor_price=120.0,
            notes=f"{door_desc} for {door_count} Opening(s)",
            trade="Doors & Hardware"
        ))
        
        hw_sym = "HW-SET-EXIT-CLOSER" if is_fire_exit else "HW-SET-OFFICE"
        hw_desc = "Von Duprin Exit Device + LCN Closer Set" if is_fire_exit else "Schlage ND Mortise Lock + BB Hinges + Stop Set"
        hw_mat_price = 620.0 if is_fire_exit else 265.0
        hw_lab_price = 230.0 if is_fire_exit else 100.0
        
        items.append(TakeoffLineItem(
            symbol=hw_sym,
            finish_type="HARDWARE",
            material_type="HARDWARE SET",
            work_type="S&I",
            quantity=float(door_count),
            unit="SET",
            material_price=hw_mat_price,
            labor_price=hw_lab_price,
            notes=f"{hw_desc} for {door_count} Door(s)",
            trade="Doors & Hardware"
        ))
        
        items.append(TakeoffLineItem(
            symbol="HW-KICKPLATE-SS",
            finish_type="HARDWARE",
            material_type="KICKPLATE",
            work_type="S&I",
            quantity=float(door_count),
            unit="PCS",
            material_price=32.0,
            labor_price=16.0,
            notes=f"Stainless Steel 10x34 Kickplate for {door_count} Door(s)",
            trade="Doors & Hardware"
        ))
        
        return items
