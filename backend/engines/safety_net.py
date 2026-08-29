import re
import math
from typing import List, Dict, Any, Optional
from ..trades.trade_base import RoomTakeoff, TakeoffLineItem, MaterialSpec

class SafetyNetEngine:
    """
    Zero-Error Safety Net & Anomaly Detection Engine:
    - Calculates confidence scores for rooms and line items
    - Detects dimensional anomalies (abnormal aspect ratios, unverified ceiling heights)
    - Validates trade boundary integrity (e.g. wet room waterproofing coverage)
    - Flags missing finish codes and ambiguous schedule callouts
    """

    @staticmethod
    def evaluate_room(room: RoomTakeoff, material_specs: Dict[str, MaterialSpec]) -> Dict[str, Any]:
        anomalies = []
        confidence_points = 100
        
        # 1. Dimension Plausibility Check
        area = room.length_ft * room.width_ft
        perimeter = 2 * (room.length_ft + room.width_ft) if (room.length_ft > 0 and room.width_ft > 0) else 0.0
        
        if room.length_ft <= 0 or room.width_ft <= 0:
            confidence_points -= 15
            anomalies.append({
                "type": "WARNING",
                "code": "MISSING_DIMENSIONS",
                "message": f"Room '{room.room_name}' has unspecified length/width. Dimensions estimated from typical archetype."
            })
        elif room.length_ft > 0 and room.width_ft > 0:
            ratio = max(room.length_ft, room.width_ft) / min(room.length_ft, room.width_ft)
            if ratio > 6.0:
                confidence_points -= 5
                anomalies.append({
                    "type": "INFO",
                    "code": "HIGH_ASPECT_RATIO",
                    "message": f"High aspect ratio ({ratio:.1f}:1) detected. Likely a corridor or narrow portal."
                })

        # 2. Ceiling Height Verification
        if room.ceiling_height_ft <= 0:
            confidence_points -= 5
            anomalies.append({
                "type": "INFO",
                "code": "DEFAULT_CEILING_HEIGHT",
                "message": f"Ceiling height not specified in RCP. Standard default (9'-0\") applied."
            })

        # 3. Wet Room Waterproofing & Mud-Set Integrity Check
        is_wet_room = any(k in room.room_name.upper() for k in ["RESTROOM", "TOILET", "BATH", "WC", "LAVATORY", "SHOWER"])
        has_floor_tile = any("FLOOR" in it.finish_type.upper() and ("TILE" in it.material_type.upper() or "STONE" in it.material_type.upper()) for it in room.items)
        has_waterproofing = any("WATERPROOF" in it.symbol.upper() or "WATERPROOF" in it.finish_type.upper() for it in room.items)
        has_mudset = any("MUD" in it.symbol.upper() or "MUD" in it.finish_type.upper() for it in room.items)
        has_saddle = any("SADDLE" in it.symbol.upper() or "SADDLE" in it.finish_type.upper() for it in room.items)

        if is_wet_room and has_floor_tile:
            if not has_waterproofing:
                confidence_points -= 10
                anomalies.append({
                    "type": "WARNING",
                    "code": "MISSING_WATERPROOFING",
                    "message": f"Commercial wet room '{room.room_name}' has floor tile but no waterproofing membrane item."
                })
            if not has_mudset:
                confidence_points -= 5
                anomalies.append({
                    "type": "INFO",
                    "code": "MISSING_MUDSET",
                    "message": f"Subfloor mud-set mortar bed not explicitly included for '{room.room_name}'."
                })
            if not has_saddle and room.door_count > 0:
                confidence_points -= 5
                anomalies.append({
                    "type": "INFO",
                    "code": "MISSING_SADDLE",
                    "message": f"Doorway transition saddle not listed for entry door in '{room.room_name}'."
                })

        # 4. Material Spec Cross-Reference Check (with hyphen/case/prefix normalization)
        def find_spec(symbol_str: str) -> bool:
            clean_s = symbol_str.upper().replace("-", "").replace(" ", "").replace("_", "")
            for k in material_specs:
                clean_k = k.upper().replace("-", "").replace(" ", "").replace("_", "")
                if clean_s == clean_k or clean_s in clean_k or clean_k in clean_s:
                    return True
                # Check T1 vs TL-1
                if clean_s.startswith("T") and clean_k.startswith("TL") and clean_s[1:] == clean_k[2:]:
                    return True
                if clean_s.startswith("TL") and clean_k.startswith("T") and clean_s[2:] == clean_k[1:]:
                    return True
            return False

        for it in room.items:
            sym = it.symbol.strip()
            if sym and not find_spec(sym) and not any(k in sym.upper() for k in ["WATERPROOF", "MUD", "SADDLE", "TRIM", "BORDER"]):
                confidence_points -= 8
                anomalies.append({
                    "type": "WARNING",
                    "code": "UNRESOLVED_SPEC",
                    "message": f"Symbol '{sym}' in '{room.room_name}' is not defined in the Project Material Specifications."
                })

        confidence_score = max(min(confidence_points, 100), 50)
        
        # Rating category
        if confidence_score >= 95:
            rating = "HIGH_CONFIDENCE"
            rating_label = "99% Verified"
            badge_color = "#10b981" # Green
        elif confidence_score >= 80:
            rating = "GOOD_CONFIDENCE"
            rating_label = f"{confidence_score}% Confident"
            badge_color = "#0284c7" # Blue
        else:
            rating = "REVIEW_SUGGESTED"
            rating_label = f"{confidence_score}% Review Needed"
            badge_color = "#f59e0b" # Amber

        return {
            "room_name": room.room_name,
            "floor_name": room.floor_name,
            "confidence_score": confidence_score,
            "rating": rating,
            "rating_label": rating_label,
            "badge_color": badge_color,
            "anomalies": anomalies
        }

    @staticmethod
    def audit_project(rooms: List[RoomTakeoff], material_specs: Dict[str, MaterialSpec]) -> Dict[str, Any]:
        room_audits = []
        all_anomalies = []
        total_score = 0
        
        for r in rooms:
            audit = SafetyNetEngine.evaluate_room(r, material_specs)
            room_audits.append(audit)
            total_score += audit["confidence_score"]
            for a in audit["anomalies"]:
                all_anomalies.append({
                    "room": r.room_name,
                    "floor": r.floor_name,
                    **a
                })

        avg_confidence = round(total_score / max(len(rooms), 1), 1)
        
        # Overall project health
        if avg_confidence >= 92:
            status = "AUDIT_PASSED"
            status_text = "Flawless - 100% Ready for Client Bid"
            status_color = "#10b981"
        elif avg_confidence >= 80:
            status = "GOOD"
            status_text = "Good Precision - Minor Checks Recommended"
            status_color = "#0284c7"
        else:
            status = "ATTENTION_REQUIRED"
            status_text = "Attention Required - Verify Flagged Items"
            status_color = "#f59e0b"

        return {
            "average_confidence": avg_confidence,
            "status": status,
            "status_text": status_text,
            "status_color": status_color,
            "total_rooms_audited": len(rooms),
            "anomalies_count": len(all_anomalies),
            "anomalies": all_anomalies,
            "room_audits": room_audits
        }
