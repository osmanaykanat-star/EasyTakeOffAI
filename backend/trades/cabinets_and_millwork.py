import math
from typing import List, Dict, Optional, Any
from .trade_base import RoomTakeoff, TakeoffLineItem, MaterialSpec

class CabinetsAndMillworkEngine:
    """
    Architectural Cabinets, Casework & Millwork Engine (CSI Division 06 41 00 / 12 35 00):
    Calculates commercial base cabinets, upper wall cabinets, tall pantry towers,
    ADA vanity casework, Blum European hardware, drawer slides, pulls, and toe kicks.
    """

    @staticmethod
    def get_default_specs() -> Dict[str, MaterialSpec]:
        return {
            "CAB-BASE-STD": MaterialSpec(
                symbol="CAB-BASE-STD",
                description="34-1/2 in H x 24 in D Commercial Grade Base Cabinets (3/4 in Plywood Box, Wilsonart HPL / Hardwood Veneer, Soft-Close Doors)",
                unit="LN FT",
                budget_price=245.0,
                notes="Pantry, break room, and kitchenette base casework",
                trade="Cabinets & Millwork"
            ),
            "CAB-BASE-ADA": MaterialSpec(
                symbol="CAB-BASE-ADA",
                description="34 in H ADA-Compliant Sink Base Cabinet with Removable Front Panel & Concealed Insulated Pipe Shield",
                unit="LN FT",
                budget_price=285.0,
                notes="ADA accessible sink casework",
                trade="Cabinets & Millwork"
            ),
            "CAB-BASE-DRAW": MaterialSpec(
                symbol="CAB-BASE-DRAW",
                description="34-1/2 in H Heavy-Duty 3-Drawer / 4-Drawer Base Cabinet Stack with Blum Full-Extension Undermount Runners",
                unit="LN FT",
                budget_price=310.0,
                notes="Utensil, tool, and storage drawer bank",
                trade="Cabinets & Millwork"
            ),
            "CAB-WALL-36": MaterialSpec(
                symbol="CAB-WALL-36",
                description="36 in H x 12 in D Upper Wall Cabinets with (2) Adjustable Shelves, Concealed Hanging Cleat & Under-Cabinet Light Valance",
                unit="LN FT",
                budget_price=195.0,
                notes="Upper storage cabinetry above counters",
                trade="Cabinets & Millwork"
            ),
            "CAB-TALL-84": MaterialSpec(
                symbol="CAB-TALL-84",
                description="84 in H x 24 in D Full-Height Pantry Storage Tower / Refrigerator Enclosure Panel System",
                unit="PCS",
                budget_price=850.0,
                notes="Tall utility and appliance enclosure units",
                trade="Cabinets & Millwork"
            ),
            "CAB-VANITY-COMM": MaterialSpec(
                symbol="CAB-VANITY-COMM",
                description="Commercial Restroom Vanity Base (Wall-Hung Floating or Floor Mounted) with ADA Removable Trap Enclosure",
                unit="LN FT",
                budget_price=275.0,
                notes="Restroom vanity cabinetry and casework",
                trade="Cabinets & Millwork"
            ),
            "CAB-HW-PULL": MaterialSpec(
                symbol="CAB-HW-PULL",
                description="Hafele / Richelieu 5 in Solid Satin Brass / Matte Black Architectural Wire Bar Pulls",
                unit="PCS",
                budget_price=12.50,
                notes="Door and drawer pulls",
                trade="Cabinets & Millwork"
            ),
            "CAB-HW-HINGE": MaterialSpec(
                symbol="CAB-HW-HINGE",
                description="Blum CLIP top BLUMOTION 110-Degree Soft-Close Concealed European Hinges",
                unit="PCS",
                budget_price=8.50,
                notes="Concealed cabinet door hinges",
                trade="Cabinets & Millwork"
            ),
            "CAB-HW-SLIDE": MaterialSpec(
                symbol="CAB-HW-SLIDE",
                description="Blum TANDEM Plus BLUMOTION 21 in Full-Extension Soft-Close Undermount Drawer Slides (100 lb Capacity)",
                unit="SET",
                budget_price=38.00,
                notes="Heavy duty drawer slide pairs",
                trade="Cabinets & Millwork"
            ),
            "CAB-TOE-KICK": MaterialSpec(
                symbol="CAB-TOE-KICK",
                description="4 in Continuous Finished Toe Kick Baseboard with Moisture Barrier Seal",
                unit="LN FT",
                budget_price=8.50,
                notes="Sub-cabinet base closure",
                trade="Cabinets & Millwork"
            )
        }

    @staticmethod
    def calculate_room_casework(room: RoomTakeoff) -> List[TakeoffLineItem]:
        """
        Dynamically calculates comprehensive architectural casework & millwork for any room:
        - Pantries, Kitchens, Break Rooms: Base cabinets, drawer stacks, upper wall cabinets, tall towers, hardware, toe kicks.
        - Restrooms & Vanities: ADA vanity casework, pipe enclosures, hinges, pulls.
        - Offices & Conference: Credenzas, storage casework, open shelving.
        """
        items: List[TakeoffLineItem] = []
        r_name = room.room_name.upper()
        l = room.length_ft
        w = room.width_ft

        is_pantry = any(k in r_name for k in ["PANTRY", "KITCHEN", "BREAK", "COFFEE", "CAFE", "LOUNGE", "FOOD"])
        is_restroom = any(k in r_name for k in ["RESTROOM", "TOILET", "BATH", "LAVATORY", "POWDER", "VANITY"])
        is_office_conf = any(k in r_name for k in ["OFFICE", "CONFERENCE", "BOARDROOM", "RECEPTION", "MEETING"])

        if is_pantry:
            # Typical pantry counter runs along length or width (e.g. 10 to 18 LF)
            counter_run_lf = round(max(6.0, min(l, 18.0)), 1)
            drawer_run_lf = round(min(3.0, counter_run_lf * 0.3), 1)
            std_base_lf = round(counter_run_lf - drawer_run_lf, 1)
            upper_run_lf = round(counter_run_lf * 0.85, 1)
            
            # Door & Drawer counts for hardware
            door_count = round(std_base_lf / 1.5) + round(upper_run_lf / 1.5)
            drawer_count = round(drawer_run_lf / 1.0) * 3
            pull_count = door_count + drawer_count
            hinge_count = door_count * 2

            items.extend([
                TakeoffLineItem(
                    symbol="CAB-BASE-STD",
                    finish_type="CASEWORK",
                    material_type="BASE CABINET",
                    work_type="S&I",
                    quantity=std_base_lf,
                    unit="LN FT",
                    material_price=165.0,
                    labor_price=80.0,
                    notes=f"Wilsonart HPL / Hardwood 34-1/2 in base cabinets along {std_base_lf} LF run",
                    trade="Cabinets & Millwork"
                ),
                TakeoffLineItem(
                    symbol="CAB-BASE-DRAW",
                    finish_type="CASEWORK",
                    material_type="DRAWER STACK",
                    work_type="S&I",
                    quantity=drawer_run_lf,
                    unit="LN FT",
                    material_price=210.0,
                    labor_price=100.0,
                    notes="3-drawer heavy-duty commercial drawer base bank",
                    trade="Cabinets & Millwork"
                ),
                TakeoffLineItem(
                    symbol="CAB-WALL-36",
                    finish_type="CASEWORK",
                    material_type="WALL CABINET",
                    work_type="S&I",
                    quantity=upper_run_lf,
                    unit="LN FT",
                    material_price=135.0,
                    labor_price=60.0,
                    notes="36 in H upper wall cabinets with adjustable shelves and light valance",
                    trade="Cabinets & Millwork"
                ),
                TakeoffLineItem(
                    symbol="CAB-TALL-84",
                    finish_type="CASEWORK",
                    material_type="PANTRY TOWER",
                    work_type="S&I",
                    quantity=1.0,
                    unit="PCS",
                    material_price=600.0,
                    labor_price=250.0,
                    notes="84 in H full-height pantry / refrigerator surround cabinet",
                    trade="Cabinets & Millwork"
                ),
                TakeoffLineItem(
                    symbol="CAB-HW-PULL",
                    finish_type="HARDWARE",
                    material_type="BAR PULL",
                    work_type="S&I",
                    quantity=float(pull_count),
                    unit="PCS",
                    material_price=8.50,
                    labor_price=4.00,
                    notes=f"Hafele / Richelieu 5 in solid bar pulls ({pull_count} pcs total)",
                    trade="Cabinets & Millwork"
                ),
                TakeoffLineItem(
                    symbol="CAB-HW-HINGE",
                    finish_type="HARDWARE",
                    material_type="CONCEALED HINGE",
                    work_type="S&I",
                    quantity=float(hinge_count),
                    unit="PCS",
                    material_price=5.50,
                    labor_price=3.00,
                    notes=f"Blum 110-deg soft-close European concealed hinges ({hinge_count} pcs)",
                    trade="Cabinets & Millwork"
                ),
                TakeoffLineItem(
                    symbol="CAB-HW-SLIDE",
                    finish_type="HARDWARE",
                    material_type="UNDERMOUNT SLIDE",
                    work_type="S&I",
                    quantity=float(drawer_count),
                    unit="SET",
                    material_price=26.0,
                    labor_price=12.0,
                    notes=f"Blum TANDEM Plus BLUMOTION 21 in full-extension undermount slide pairs ({drawer_count} sets)",
                    trade="Cabinets & Millwork"
                ),
                TakeoffLineItem(
                    symbol="CAB-TOE-KICK",
                    finish_type="BASE",
                    material_type="TOE KICK",
                    work_type="S&I",
                    quantity=counter_run_lf,
                    unit="LN FT",
                    material_price=5.00,
                    labor_price=3.50,
                    notes="4 in continuous matching toe kick with water-resistant seal",
                    trade="Cabinets & Millwork"
                )
            ])

        elif is_restroom:
            # Vanity casework
            vanity_lf = round(max(3.5, min(w * 0.6, 12.0)), 1)
            door_count = round(vanity_lf / 2.0) * 2
            items.extend([
                TakeoffLineItem(
                    symbol="CAB-VANITY-COMM",
                    finish_type="CASEWORK",
                    material_type="VANITY BASE",
                    work_type="S&I",
                    quantity=vanity_lf,
                    unit="LN FT",
                    material_price=185.0,
                    labor_price=90.0,
                    notes=f"Commercial ADA restroom vanity base with removable pipe shield panel along {vanity_lf} LF",
                    trade="Cabinets & Millwork"
                ),
                TakeoffLineItem(
                    symbol="CAB-HW-PULL",
                    finish_type="HARDWARE",
                    material_type="BAR PULL",
                    work_type="S&I",
                    quantity=float(door_count),
                    unit="PCS",
                    material_price=8.50,
                    labor_price=4.00,
                    notes="Hafele architectural vanity door pulls",
                    trade="Cabinets & Millwork"
                ),
                TakeoffLineItem(
                    symbol="CAB-HW-HINGE",
                    finish_type="HARDWARE",
                    material_type="CONCEALED HINGE",
                    work_type="S&I",
                    quantity=float(door_count * 2),
                    unit="PCS",
                    material_price=5.50,
                    labor_price=3.00,
                    notes="Blum soft-close concealed vanity hinges",
                    trade="Cabinets & Millwork"
                )
            ])

        elif is_office_conf:
            # Storage credenza or reception casework
            credenza_lf = 8.0
            items.extend([
                TakeoffLineItem(
                    symbol="CAB-BASE-STD",
                    finish_type="CASEWORK",
                    material_type="CREDENZA BASE",
                    work_type="S&I",
                    quantity=credenza_lf,
                    unit="LN FT",
                    material_price=190.0,
                    labor_price=85.0,
                    notes="Architectural wood veneer executive storage credenza casework",
                    trade="Cabinets & Millwork"
                ),
                TakeoffLineItem(
                    symbol="CAB-HW-PULL",
                    finish_type="HARDWARE",
                    material_type="BAR PULL",
                    work_type="S&I",
                    quantity=8.0,
                    unit="PCS",
                    material_price=8.50,
                    labor_price=4.00,
                    notes="Architectural executive credenza pulls",
                    trade="Cabinets & Millwork"
                )
            ])

        return items
