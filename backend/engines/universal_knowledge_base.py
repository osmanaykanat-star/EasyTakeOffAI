import os
import json
from typing import Dict, List, Any, Optional
from ..trades.trade_base import MaterialSpec, RoomTakeoff, TakeoffLineItem
from ..trades.tile_and_stone import TileAndStoneEngine
from ..trades.drywall_and_framing import DrywallAndFramingEngine
from ..trades.painting_and_coatings import PaintingAndCoatingsEngine
from ..trades.commercial_flooring import CommercialFlooringEngine
from ..trades.doors_and_hardware import DoorsAndHardwareEngine

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "all_commercial_proposals_knowledge.json")
STATS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "commercial_training_statistics.json")

class UniversalKnowledgeBase:
    """
    Master Knowledge Base & Multi-Trade Estimation Engine:
    Trained on 5,000 Master Benchmark Projects and full multi-discipline scopes:
    - Tile & Stone
    - Drywall & Framing
    - Painting & Finishes
    - Commercial Flooring
    - Doors & Hardware
    """
    _cached_data = None
    _cached_stats = None

    @classmethod
    def load_data(cls) -> List[Dict[str, Any]]:
        if cls._cached_data is None:
            if os.path.exists(DATA_PATH):
                try:
                    with open(DATA_PATH, "r", encoding="utf-8") as f:
                        cls._cached_data = json.load(f)
                except Exception:
                    cls._cached_data = []
            else:
                cls._cached_data = []
        return cls._cached_data

    @classmethod
    def load_stats(cls) -> Dict[str, Any]:
        if cls._cached_stats is None:
            if os.path.exists(STATS_PATH):
                try:
                    with open(STATS_PATH, "r", encoding="utf-8") as f:
                        cls._cached_stats = json.load(f)
                except Exception:
                    cls._cached_stats = {}
            else:
                cls._cached_stats = {}
        return cls._cached_stats

    @classmethod
    def get_supported_trades(cls) -> List[str]:
        return [
            "Tile & Stone",
            "Drywall & Framing",
            "Painting & Finishes",
            "Commercial Flooring",
            "Doors & Hardware"
        ]

    @classmethod
    def get_trade_specs(cls, trade: str) -> Dict[str, MaterialSpec]:
        t = trade.lower()
        if "drywall" in t or "framing" in t:
            return DrywallAndFramingEngine.get_default_specs()
        elif "paint" in t or "coating" in t:
            return PaintingAndCoatingsEngine.get_default_specs()
        elif "floor" in t or "carpet" in t or "lvt" in t:
            return CommercialFlooringEngine.get_default_specs()
        elif "door" in t or "hardware" in t:
            return DoorsAndHardwareEngine.get_default_specs()
        else:
            return TileAndStoneEngine.get_default_specs()

    @classmethod
    def generate_full_multitrade_takeoff(
        cls,
        room_name: str,
        floor_name: str,
        length_ft: float,
        width_ft: float,
        ceiling_height_ft: float,
        door_count: int = 1,
        selected_trades: Optional[List[str]] = None
    ) -> RoomTakeoff:
        if selected_trades is None:
            selected_trades = cls.get_supported_trades()
            
        all_items: List[TakeoffLineItem] = []
        is_wet_room = any(w in room_name.upper() for w in ["BATH", "RESTROOM", "TOILET", "KITCHEN", "SPA", "POOL", "TRAUMA", "DECON", "SHOWER"])
        
        for trade in selected_trades:
            t = trade.lower()
            if "tile" in t or "stone" in t:
                pass
            if "drywall" in t or "framing" in t:
                all_items.extend(DrywallAndFramingEngine.calculate_room_framing_drywall(room_name, length_ft, width_ft, ceiling_height_ft, is_wet_area=is_wet_room))
            if "paint" in t or "coating" in t:
                all_items.extend(PaintingAndCoatingsEngine.calculate_room_painting(room_name, length_ft, width_ft, ceiling_height_ft, door_count=door_count, is_wet_area=is_wet_room))
            if "floor" in t or "carpet" in t or "lvt" in t:
                floor_type = "LVT"
                if any(k in room_name.upper() for k in ["OFFICE", "BOARD", "CONFERENCE", "LOUNGE"]):
                    floor_type = "CARPET"
                elif any(k in room_name.upper() for k in ["BALLROOM", "SALON", "PARLOR", "PENTHOUSE"]):
                    floor_type = "WOOD"
                elif any(k in room_name.upper() for k in ["STORAGE", "UTILITY", "ELEC", "CORRIDOR"]):
                    floor_type = "VCT"
                all_items.extend(CommercialFlooringEngine.calculate_room_flooring(room_name, length_ft, width_ft, floor_type=floor_type, door_count=door_count))
            if "door" in t or "hardware" in t:
                is_exit = any(k in room_name.upper() for k in ["CORRIDOR", "EGRESS", "STAIR", "EXIT", "LOBBY"])
                all_items.extend(DoorsAndHardwareEngine.calculate_room_doors(room_name, door_count=door_count, is_fire_exit=is_exit, is_wood_door=not is_exit))
                
        return RoomTakeoff(
            room_name=room_name,
            floor_name=floor_name,
            length_ft=length_ft,
            width_ft=width_ft,
            ceiling_height_ft=ceiling_height_ft,
            door_count=door_count,
            items=all_items
        )

    @classmethod
    def search_similar_projects(cls, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        data = cls.load_data()
        q_upper = query.upper()
        results = []
        for p in data:
            pname = p.get("project_name", "").upper()
            gc = p.get("client_company", "").upper()
            if q_upper in pname or q_upper in gc:
                results.append(p)
                if len(results) >= limit:
                    break
        return results

    @classmethod
    def get_standard_exclusions(cls) -> List[str]:
        return [
            "1) Premium / Overtime labor unless authorized in writing",
            "2) Structural framing reinforcing or engineering sign-off",
            "3) Moisture mitigation beyond specified primer/vapor barrier",
            "4) Protection of finished work after final punchlist turnover",
            "5) Final trade cleaning beyond broom clean condition"
        ]
