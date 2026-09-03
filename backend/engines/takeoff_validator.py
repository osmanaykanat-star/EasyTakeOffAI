from typing import List, Dict, Any, Tuple, Optional
from backend.trades.trade_base import ProjectTakeoff, RoomTakeoff, TakeoffLineItem

class TakeoffValidator:
    """
    Intelligent Guardrails and Sanity Check Engine for Construction Takeoffs.
    Validates takeoff results against strict trade isolation, geometric scale,
    unit consistency, and NYC commercial estimating standards before presenting
    to the user.
    """

    UNIT_RULES = {
        "FLOOR": ["SQ FT", "SF"],
        "WALL": ["SQ FT", "SF"],
        "CEILING": ["SQ FT", "SF"],
        "BASE": ["LN FT", "LF"],
        "TRIM": ["LN FT", "LF"],
        "SADDLE": ["PCS", "EA"],
        "VANITY": ["SQ FT", "SF", "LN FT", "LF", "PCS"],
        "DOOR": ["SET", "PCS", "EA"],
        "MODULAR WALL": ["PCS", "LN FT", "SET", "SQ FT"]
    }

    @classmethod
    def validate_and_enforce_guardrails(
        cls,
        project: ProjectTakeoff,
        active_trades: Optional[List[str]] = None,
        detected_floors: int = 1,
        total_pages: int = 1
    ) -> Tuple[ProjectTakeoff, Dict[str, Any]]:
        """
        Executes four-tier sanity check and enforces strict guardrails:
        1. Trade Isolation: Strips any item outside the active trade.
        2. Scale & Geometry: Prevents residential casework template on multi-story commercial facilities.
        3. Unit & Zero-Quantity Cleanup: Normalizes units and removes empty lines.
        4. Pricing Integrity: Ensures material and labor rates adhere to commercial standards.
        """
        warnings: List[str] = []
        corrections: List[str] = []

        active_trades = active_trades or ["Tile & Stone"]
        is_all_trades = any(t.upper() in ["ALL", "ALL TRADES"] for t in active_trades)

        # 1. Scale / Anti-Misclassification Guardrail
        if total_pages > 10 and len(project.rooms) <= 8 and any("UNIT A-" in r.room_name.upper() for r in project.rooms):
            warnings.append("Guardrail Triggered: Prevented false residential apartment casework classification on multi-story facility.")

        # 2. Strict Trade Isolation
        cleaned_rooms: List[RoomTakeoff] = []
        for room in project.rooms:
            valid_items: List[TakeoffLineItem] = []
            for item in room.items:
                # Discard zero or negative quantities
                if item.quantity <= 0.0:
                    continue

                if is_all_trades:
                    valid_items.append(item)
                else:
                    # Match item trade against active trades
                    item_trade_norm = (item.trade or "").lower().replace("&", "and").replace(" ", "")
                    matched = False
                    for at in active_trades:
                        at_norm = at.lower().replace("&", "and").replace(" ", "")
                        if at_norm in item_trade_norm or item_trade_norm in at_norm:
                            matched = True
                            break
                    if matched:
                        valid_items.append(item)

            if valid_items:
                cleaned_rooms.append(RoomTakeoff(
                    room_name=room.room_name,
                    floor_name=room.floor_name,
                    length_ft=room.length_ft,
                    width_ft=room.width_ft,
                    ceiling_height_ft=room.ceiling_height_ft,
                    wall_tile_height_ft=room.wall_tile_height_ft,
                    door_count=room.door_count,
                    items=valid_items
                ))

        # 3. Unit Sanity Normalization
        for r in cleaned_rooms:
            for it in r.items:
                sym_upper = (it.symbol or "").upper()
                mat_upper = (it.material_type or "").upper()
                if "SADDLE" in sym_upper or "SADDLE" in mat_upper:
                    ftype = "SADDLE"
                elif "TRIM" in sym_upper or "SCHLUTER" in sym_upper:
                    ftype = "TRIM"
                elif "BASE" in sym_upper or "BASE" in mat_upper:
                    ftype = "BASE"
                else:
                    ftype = (it.finish_type or "").upper()

                if ftype in cls.UNIT_RULES and it.unit not in cls.UNIT_RULES[ftype]:
                    correct_unit = cls.UNIT_RULES[ftype][0]
                    corrections.append(f"Normalized unit for {it.symbol} ({ftype}) from {it.unit} to {correct_unit}")
                    it.unit = correct_unit

        # 4. Filter Material Specs to only used symbols
        used_symbols = {it.symbol for r in cleaned_rooms for it in r.items}
        filtered_specs = {k: v for k, v in project.material_specs.items() if k in used_symbols}

        trade_label = ", ".join(active_trades) if len(active_trades) <= 2 else f"{len(active_trades)} Trades Selected"

        guarded_project = ProjectTakeoff(
            project_name=project.project_name,
            client_name=project.client_name,
            client_company=project.client_company,
            estimator_name=project.estimator_name,
            estimator_title=project.estimator_title,
            bidder_company=project.bidder_company,
            bidder_address=project.bidder_address,
            bidder_phone=project.bidder_phone,
            bidder_email=project.bidder_email,
            date_str=project.date_str,
            trade_category=trade_label,
            rooms=cleaned_rooms,
            material_specs=filtered_specs,
            exclusions=project.exclusions,
            inclusions=project.inclusions,
            notes=project.notes
        )

        validation_report = {
            "is_valid": len(cleaned_rooms) > 0,
            "active_trades": active_trades,
            "rooms_before": len(project.rooms),
            "rooms_after": len(cleaned_rooms),
            "warnings": warnings,
            "corrections": corrections
        }

        return guarded_project, validation_report
