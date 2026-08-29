import math
from typing import List, Dict, Any, Tuple, Optional
from ..trades.trade_base import RoomTakeoff

class GeometryEngine:
    """
    Precision Blueprint Geometry & Polygon Overlay Engine:
    - Calculates spatial polygon bounding boxes (x, y, w, h, polygon points) for visual canvas
    - Supports architectural scale calibration (1/8\" = 1'-0\", 1/4\" = 1'-0\", 3/16\" = 1'-0\")
    - 2-Point manual ruler calibration: recalculates scale and room dimensions in real-time
    """

    DEFAULT_SCALE_RATIOS = {
        "1/8\" = 1'-0\"": 12.0,   # 12 pixels per foot at standard 96 DPI
        "1/4\" = 1'-0\"": 24.0,   # 24 pixels per foot
        "3/16\" = 1'-0\"": 18.0,  # 18 pixels per foot
        "1/2\" = 1'-0\"": 48.0,   # 48 pixels per foot
        "3/32\" = 1'-0\"": 9.0    # 9 pixels per foot
    }

    @staticmethod
    def calculate_scale_from_points(p1: Tuple[float, float], p2: Tuple[float, float], known_feet: float) -> float:
        """
        Calculates pixels_per_foot from two clicked points on canvas and known distance.
        """
        if known_feet <= 0:
            return 24.0 # default
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        pixel_dist = math.sqrt(dx * dx + dy * dy)
        pixels_per_foot = pixel_dist / known_feet
        return max(pixels_per_foot, 1.0)

    @staticmethod
    def generate_room_polygons(rooms: List[RoomTakeoff], canvas_width: float = 1600.0, canvas_height: float = 1200.0, pixels_per_foot: float = 24.0) -> List[Dict[str, Any]]:
        """
        Generates realistic 2D polygon overlays arranged across architectural floor levels.
        """
        polygons = []
        
        # Group by floor
        floor_groups = {}
        for r in rooms:
            fname = r.floor_name.upper() if r.floor_name else "MAIN FLOOR"
            if fname not in floor_groups:
                floor_groups[fname] = []
            floor_groups[fname].append(r)

        margin_x = 120.0
        margin_y = 140.0
        current_y = margin_y
        
        color_palette = {
            "RESTROOM": {"fill": "rgba(2, 132, 199, 0.25)", "stroke": "#0284c7", "label": "Tile & Stone (Wet Room)"},
            "TOILET": {"fill": "rgba(2, 132, 199, 0.25)", "stroke": "#0284c7", "label": "Tile & Stone (Wet Room)"},
            "BATHROOM": {"fill": "rgba(2, 132, 199, 0.25)", "stroke": "#0284c7", "label": "Tile & Stone (Wet Room)"},
            "PANTRY": {"fill": "rgba(245, 158, 11, 0.25)", "stroke": "#f59e0b", "label": "Countertop & Solid Surface"},
            "KITCHEN": {"fill": "rgba(245, 158, 11, 0.25)", "stroke": "#f59e0b", "label": "Countertop & Solid Surface"},
            "LOBBY": {"fill": "rgba(16, 185, 129, 0.25)", "stroke": "#10b981", "label": "Large Format Stone / Tile"},
            "CORRIDOR": {"fill": "rgba(139, 92, 246, 0.25)", "stroke": "#8b5cf6", "label": "Passage & Trim"},
            "VESTIBULE": {"fill": "rgba(139, 92, 246, 0.25)", "stroke": "#8b5cf6", "label": "Passage & Trim"},
            "STAIR": {"fill": "rgba(244, 63, 94, 0.25)", "stroke": "#f43f5e", "label": "Stair Treads & Risers"}
        }

        for floor_idx, (floor_name, f_rooms) in enumerate(floor_groups.items()):
            current_x = margin_x
            max_row_height = 0.0
            
            for r_idx, room in enumerate(f_rooms):
                l_ft = room.length_ft if room.length_ft > 0 else 10.0
                w_ft = room.width_ft if room.width_ft > 0 else 8.0
                
                poly_w = max(l_ft * pixels_per_foot, 90.0)
                poly_h = max(w_ft * pixels_per_foot, 70.0)
                
                # Check wrap
                if current_x + poly_w > canvas_width - margin_x:
                    current_x = margin_x
                    current_y += max_row_height + 40.0
                    max_row_height = 0.0
                    
                # Determine color scheme from room name
                matched_style = {"fill": "rgba(2, 132, 199, 0.25)", "stroke": "#0284c7", "label": "Tile & Stone"}
                for key, style in color_palette.items():
                    if key in room.room_name.upper():
                        matched_style = style
                        break
                        
                # Define 4 corner points
                points = [
                    {"x": round(current_x, 1), "y": round(current_y, 1)},
                    {"x": round(current_x + poly_w, 1), "y": round(current_y, 1)},
                    {"x": round(current_x + poly_w, 1), "y": round(current_y + poly_h, 1)},
                    {"x": round(current_x, 1), "y": round(current_y + poly_h, 1)}
                ]
                
                polygons.append({
                    "id": f"poly_{floor_idx}_{r_idx}",
                    "room_name": room.room_name,
                    "floor_name": floor_name,
                    "x": round(current_x, 1),
                    "y": round(current_y, 1),
                    "width": round(poly_w, 1),
                    "height": round(poly_h, 1),
                    "length_ft": round(l_ft, 1),
                    "width_ft": round(w_ft, 1),
                    "area_sqft": round(l_ft * w_ft, 1),
                    "perimeter_lnft": round(2 * (l_ft + w_ft), 1),
                    "points": points,
                    "style": matched_style,
                    "items_count": len(room.items)
                })
                
                current_x += poly_w + 30.0
                if poly_h > max_row_height:
                    max_row_height = poly_h
                    
            current_y += max_row_height + 60.0

        return polygons
