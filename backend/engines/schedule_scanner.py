import re
from typing import Dict, List, Any, Optional

class ScheduleScanner:
    """
    Finish Schedule & Legend OCR Table Matrix Scanner:
    - Identifies architectural Room Finish Schedules (Sheets A-600, A-601)
    - Cross-references room numbers (e.g. A177, 101, 2125) with finish tags (Floor, Base, Walls, Ceiling)
    - Automatically builds material assignment matrices
    """

    @staticmethod
    def scan_finish_schedule_text(text: str) -> Dict[str, Dict[str, str]]:
        """
        Parses text for room finish schedule entries.
        Returns mapping: {room_id: {"floor_tag": ..., "base_tag": ..., "wall_tag": ..., "wall_height": ...}}
        """
        matrix = {}
        lines = text.split("\n")
        
        # Pattern for room numbers like A101, 101, 2125, #101
        room_line_regex = re.compile(
            r'\b([A-Z]?[0-9]{3,4}[A-Z]?)\s+([A-Z\s\'-]{3,25})\s+([A-Z0-9-]{2,6})\s+([A-Z0-9-]{2,6})?\s*([A-Z0-9-]{2,6})?',
            re.IGNORECASE
        )

        for line in lines:
            line_str = line.strip()
            if not line_str or any(h in line_str.upper() for h in ["ROOM NO", "ROOM NAME", "FINISH SCHEDULE", "FLOOR PLAN"]):
                continue
                
            m = room_line_regex.search(line_str)
            if m:
                room_no = m.group(1).upper()
                room_name = m.group(2).strip().upper()
                floor_tag = m.group(3).upper() if m.group(3) else ""
                base_tag = m.group(4).upper() if m.group(4) else ""
                wall_tag = m.group(5).upper() if m.group(5) else ""
                
                # Filter noise
                if len(room_name) >= 3 and floor_tag:
                    matrix[room_no] = {
                        "room_number": room_no,
                        "room_name": room_name,
                        "floor_tag": floor_tag,
                        "base_tag": base_tag,
                        "wall_tag": wall_tag
                    }

        return matrix
