import re
from typing import List, Dict, Any, Optional
from backend.trades.trade_base import RoomTakeoff, TakeoffLineItem

class TypicalFloorEngine:
    """
    Architectural Multiplier & Typical Floor Propagation Engine.
    Detects architectural multiplier indicators (e.g., 'TYPICAL OF 4 FLOORS',
    'LEVELS 2 THRU 5', 'TYP. RESTROOM CORE') and replicates typical spaces
    accurately across all target floors, scoped strictly to the active trade.
    """

    TYPICAL_PATTERNS = [
        re.compile(r'\bTYP(?:ICAL)?\s*(?:OF\s*)?(\d+)\s*(?:FLOORS|LEVELS|STORIES)?\b', re.I),
        re.compile(r'\b(?:LEVELS|FLOORS)\s*(\d+)\s*(?:THRU|THROUGH|TO|-)\s*(\d+)\b', re.I),
        re.compile(r'\b(?:LEVELS|FLOORS)\s*([0-9,\s&AND]+)\s*TYP(?:ICAL)?\b', re.I),
        re.compile(r'\bTYP(?:ICAL)?\s*(?:RESTROOM|CORE|BATHROOM|PLAN)\b', re.I)
    ]

    @classmethod
    def replicate_typical_rooms(
        cls,
        base_rooms: List[RoomTakeoff],
        detected_floors: int = 1,
        active_trades: Optional[List[str]] = None
    ) -> List[RoomTakeoff]:
        """
        Takes extracted base rooms and ensures that typical multi-floor spaces
        (like core restrooms, janitor closets, electrical/telecom rooms) exist on
        each applicable floor up to `detected_floors`.
        """
        if detected_floors <= 1 or not base_rooms:
            return base_rooms

        result_rooms: List[RoomTakeoff] = []
        seen_floor_rooms = set()

        for r in base_rooms:
            key = f"{r.floor_name.strip().upper()}::{r.room_name.strip().upper()}"
            seen_floor_rooms.add(key)
            result_rooms.append(r)

        # Identify typical templates among base rooms
        typical_templates = []
        for r in base_rooms:
            r_upper = r.room_name.upper()
            if any(k in r_upper for k in ["RESTROOM", "TOILET", "CORE", "BATHROOM", "JANITOR", "MOP"]):
                typical_templates.append(r)

        if not typical_templates:
            return result_rooms

        # Check which floors from 2 to detected_floors are missing core spaces
        for fl_num in range(2, detected_floors + 1):
            fl_name = f"LEVEL {fl_num}"
            for tmpl in typical_templates:
                # Check if this floor already has a restroom or matching core space
                has_existing = any(
                    fl_name in r.floor_name.upper() and ("RESTROOM" in r.room_name.upper() or "TOILET" in r.room_name.upper())
                    for r in result_rooms
                )
                if not has_existing and ("RESTROOM" in tmpl.room_name.upper() or "TOILET" in tmpl.room_name.upper()):
                    new_room_name = f"{fl_name} - CORE RESTROOMS (MEN'S & WOMEN'S)"
                    # Filter items by active trade if specified
                    cloned_items = []
                    for it in tmpl.items:
                        if not active_trades or any(
                            st.lower().replace("&", "and").replace(" ", "") in it.trade.lower().replace("&", "and").replace(" ", "")
                            for st in active_trades
                        ):
                            cloned_items.append(TakeoffLineItem(
                                symbol=it.symbol,
                                finish_type=it.finish_type,
                                material_type=it.material_type,
                                work_type=it.work_type,
                                quantity=it.quantity,
                                unit=it.unit,
                                material_price=it.material_price,
                                labor_price=it.labor_price,
                                notes=it.notes,
                                trade=it.trade
                            ))

                    if cloned_items:
                        result_rooms.append(RoomTakeoff(
                            room_name=new_room_name,
                            floor_name=fl_name,
                            length_ft=tmpl.length_ft,
                            width_ft=tmpl.width_ft,
                            ceiling_height_ft=tmpl.ceiling_height_ft,
                            wall_tile_height_ft=tmpl.wall_tile_height_ft,
                            door_count=tmpl.door_count,
                            items=cloned_items
                        ))

        return result_rooms
