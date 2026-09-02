from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from enum import Enum

class WorkType(str, Enum):
    SUPPLY_AND_INSTALL = "S&I"
    INSTALL_ONLY = "IO"

class UnitType(str, Enum):
    SQ_FT = "SQ FT"
    LNFT = "LNFT"
    PCS = "PCS"
    ITEM = "ITEM"

def classify_item_trade(finish_type: str, material_type: str, symbol: str) -> str:
    s = f"{finish_type} {material_type} {symbol}".upper()
    if any(k in s for k in ["TILE", "STONE", "PORCELAIN", "CERAMIC", "GRANITE", "MARBLE", "QUARTZ", "WATERPROOF", "MUD-SET", "SADDLE", "SCHLUTER", "SOLID SURFACE", "BULLNOSE", "GROUT"]):
        return "Tile & Stone"
    elif any(k in s for k in ["WOOD", "HARDWOOD", "PARQUET", "LVT", "VINYL", "CARPET", "POLYURETHANE", "SANDING", "FLOORING"]):
        return "Flooring & Wood"
    elif any(k in s for k in ["PAINT", "WALL COVER", "BENJAMIN", "PRIMER", "PLASTER", "COATING"]):
        return "Painting"
    elif any(k in s for k in ["CABINET", "MILLWORK", "KRAFTMAID", "DOOR", "HARDWARE", "SHELVING", "CARPENTRY", "VANITY"]):
        return "Millwork & Carpentry"
    elif any(k in s for k in ["PLUMB", "SINK", "TOILET", "FAUCET", "BATHTUB", "TUB", "DRAIN", "SHOWER TRIM", "ELKAY", "KOHLER"]):
        return "Plumbing"
    elif any(k in s for k in ["HVAC", "PTAC", "BOILER", "HEAT", "AC", "GAS LINE", "COOLING"]):
        return "HVAC & Mechanical"
    elif any(k in s for k in ["ELEC", "LIGHT", "FIXTURE", "RECESSED", "EV CHARGER", "POWER"]):
        return "Electrical"
    elif any(k in s for k in ["DEMO", "SOFFIT REMOVAL", "PARTITION REMOVAL"]):
        return "Demolition"
    elif any(k in s for k in ["PAVER", "FENCE", "PARAPET", "COPING", "ROOF", "TERRACE"]):
        return "Exterior & Pavers"
    return "Tile & Stone"

@dataclass
class TakeoffLineItem:
    symbol: str
    finish_type: str        # FLOOR, WALL, TRIM/BULLNOSE, BASE, FLOOR & WALL, WALL&FLOOR
    material_type: str      # TILE, STONE, BULLNOSE, PREP MATERIAL, METAL TRIM, MOSAIC
    work_type: str = "S&I"  # S&I or IO
    quantity: float = 0.0
    unit: str = "SQ FT"     # SQ FT, LNFT, PCS
    material_price: float = 0.0
    labor_price: float = 0.0
    notes: str = ""
    formula: Optional[str] = None
    trade: str = ""

    def __post_init__(self):
        if not self.trade:
            self.trade = classify_item_trade(self.finish_type, self.material_type, self.symbol)

    @property
    def total_bid(self) -> float:
        return self.quantity * (self.material_price + self.labor_price)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "symbol": self.symbol,
            "finish_type": self.finish_type,
            "material_type": self.material_type,
            "work_type": self.work_type,
            "quantity": round(self.quantity, 2),
            "unit": self.unit,
            "material_price": self.material_price,
            "labor_price": self.labor_price,
            "total_bid": round(self.total_bid, 2),
            "notes": self.notes,
            "trade": self.trade
        }

@dataclass
class RoomTakeoff:
    room_name: str          # e.g., "WC 122A" or "BOYS BATH 711"
    floor_name: str         # e.g., "1ST FLOOR" or "7TH FLOOR"
    length_ft: float = 0.0
    width_ft: float = 0.0
    ceiling_height_ft: float = 9.0
    door_count: int = 1
    door_width_ft: float = 3.0
    door_height_ft: float = 7.0
    wall_tile_height_ft: float = 9.0 # e.g. full height or wainscot
    items: List[TakeoffLineItem] = field(default_factory=list)

    @property
    def floor_area_sqft(self) -> float:
        return self.length_ft * self.width_ft

    @property
    def perimeter_lnft(self) -> float:
        return 2 * (self.length_ft + self.width_ft)

    @property
    def gross_wall_area_sqft(self) -> float:
        return self.perimeter_lnft * self.wall_tile_height_ft

    @property
    def net_wall_area_sqft(self) -> float:
        doors_area = self.door_count * (self.door_width_ft * min(self.door_height_ft, self.wall_tile_height_ft))
        return max(0.0, self.gross_wall_area_sqft - doors_area)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "room_name": self.room_name,
            "floor_name": self.floor_name,
            "length_ft": self.length_ft,
            "width_ft": self.width_ft,
            "ceiling_height_ft": self.ceiling_height_ft,
            "wall_tile_height_ft": self.wall_tile_height_ft,
            "door_count": self.door_count,
            "floor_area_sqft": round(self.floor_area_sqft, 2),
            "perimeter_lnft": round(self.perimeter_lnft, 2),
            "net_wall_area_sqft": round(self.net_wall_area_sqft, 2),
            "items": [item.to_dict() for item in self.items]
        }

@dataclass
class MaterialSpec:
    symbol: str
    description: str        # Description of finish
    manufacturer: str = ""
    collection: str = ""
    size: str = ""
    finish: str = ""
    color: str = ""
    unit: str = "SQ FT"
    budget_price: float = 0.0
    notes: str = ""
    trade: str = ""

    def __post_init__(self):
        if not self.trade:
            self.trade = classify_item_trade(self.description, self.collection, self.symbol)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "symbol": self.symbol,
            "description": self.description,
            "manufacturer": self.manufacturer,
            "collection": self.collection,
            "size": self.size,
            "finish": self.finish,
            "color": self.color,
            "unit": self.unit,
            "budget_price": self.budget_price,
            "notes": self.notes,
            "trade": self.trade
        }

@dataclass
class ProjectTakeoff:
    project_name: str
    client_name: str = ""
    client_company: str = ""
    estimator_name: str = ""
    estimator_title: str = "Senior Estimator"
    bidder_company: str = ""
    bidder_address: str = ""
    bidder_phone: str = ""
    bidder_email: str = ""
    date_str: str = ""
    trade_category: str = "Tile & Stone"
    rooms: List[RoomTakeoff] = field(default_factory=list)
    material_specs: Dict[str, MaterialSpec] = field(default_factory=dict)
    exclusions: List[str] = field(default_factory=list)
    inclusions: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)

    def filter_by_trades(self, selected_trades: Optional[List[str]]) -> "ProjectTakeoff":
        if not selected_trades or "All" in selected_trades or "ALL" in selected_trades or "all" in selected_trades:
            return self
        
        # Normalize trade query strings
        norm_selected = [t.lower().replace("&", "and").replace(" ", "").replace("_", "") for t in selected_trades if t]
        if not norm_selected:
            return self

        filtered_rooms = []
        for room in self.rooms:
            matching_items = []
            for item in room.items:
                item_trade_norm = item.trade.lower().replace("&", "and").replace(" ", "").replace("_", "")
                if any(st in item_trade_norm or item_trade_norm in st for st in norm_selected):
                    matching_items.append(item)
            if matching_items:
                filtered_rooms.append(RoomTakeoff(
                    room_name=room.room_name,
                    floor_name=room.floor_name,
                    length_ft=room.length_ft,
                    width_ft=room.width_ft,
                    ceiling_height_ft=room.ceiling_height_ft,
                    door_count=room.door_count,
                    door_width_ft=room.door_width_ft,
                    door_height_ft=room.door_height_ft,
                    wall_tile_height_ft=room.wall_tile_height_ft,
                    items=matching_items
                ))

        used_symbols = {item.symbol for r in filtered_rooms for item in r.items}
        filtered_specs = {k: v for k, v in self.material_specs.items() if k in used_symbols}
        trade_label = ", ".join(selected_trades) if len(selected_trades) <= 2 else f"{len(selected_trades)} Trades Selected"

        return ProjectTakeoff(
            project_name=self.project_name,
            client_name=self.client_name,
            client_company=self.client_company,
            estimator_name=self.estimator_name,
            estimator_title=self.estimator_title,
            bidder_company=self.bidder_company,
            bidder_address=self.bidder_address,
            bidder_phone=self.bidder_phone,
            bidder_email=self.bidder_email,
            date_str=self.date_str,
            trade_category=trade_label,
            rooms=filtered_rooms,
            material_specs=filtered_specs,
            exclusions=self.exclusions,
            inclusions=self.inclusions,
            notes=self.notes
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "project_name": self.project_name,
            "client_name": self.client_name,
            "client_company": self.client_company,
            "estimator_name": self.estimator_name,
            "estimator_title": self.estimator_title,
            "bidder_company": self.bidder_company,
            "bidder_address": self.bidder_address,
            "bidder_phone": self.bidder_phone,
            "bidder_email": self.bidder_email,
            "date_str": self.date_str,
            "trade_category": self.trade_category,
            "rooms": [r.to_dict() for r in self.rooms],
            "material_specs": {k: v.to_dict() for k, v in self.material_specs.items()},
            "exclusions": self.exclusions,
            "inclusions": self.inclusions,
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ProjectTakeoff":
        rooms_list = []
        for r in data.get("rooms", []):
            items_list = []
            for it in r.get("items", []):
                items_list.append(TakeoffLineItem(
                    symbol=it.get("symbol", ""),
                    finish_type=it.get("finish_type", ""),
                    material_type=it.get("material_type", ""),
                    work_type=it.get("work_type", "S&I"),
                    quantity=float(it.get("quantity", 0.0)),
                    unit=it.get("unit", "SQ FT"),
                    material_price=float(it.get("material_price", 0.0)),
                    labor_price=float(it.get("labor_price", 0.0)),
                    notes=it.get("notes", ""),
                    trade=it.get("trade", "")
                ))
            rooms_list.append(RoomTakeoff(
                room_name=r.get("room_name", ""),
                floor_name=r.get("floor_name", ""),
                length_ft=float(r.get("length_ft", 0.0)),
                width_ft=float(r.get("width_ft", 0.0)),
                ceiling_height_ft=float(r.get("ceiling_height_ft", 9.0)),
                wall_tile_height_ft=float(r.get("wall_tile_height_ft", 0.0)),
                door_count=int(r.get("door_count", 1)),
                items=items_list
            ))
        specs_dict = {}
        for k, v in data.get("material_specs", {}).items():
            specs_dict[k] = MaterialSpec(
                symbol=v.get("symbol", k),
                description=v.get("description", ""),
                manufacturer=v.get("manufacturer", ""),
                collection=v.get("collection", ""),
                size=v.get("size", ""),
                finish=v.get("finish", ""),
                color=v.get("color", ""),
                unit=v.get("unit", "SQ FT"),
                budget_price=float(v.get("budget_price", 0.0)),
                notes=v.get("notes", ""),
                trade=v.get("trade", "")
            )
        return cls(
            project_name=data.get("project_name", "New Takeoff Project"),
            client_name=data.get("client_name", ""),
            client_company=data.get("client_company", ""),
            estimator_name=data.get("estimator_name", ""),
            estimator_title=data.get("estimator_title", "Senior Estimator"),
            bidder_company=data.get("bidder_company", ""),
            bidder_address=data.get("bidder_address", ""),
            bidder_phone=data.get("bidder_phone", ""),
            bidder_email=data.get("bidder_email", ""),
            date_str=data.get("date_str", ""),
            trade_category=data.get("trade_category", "Tile & Stone"),
            rooms=rooms_list,
            material_specs=specs_dict,
            exclusions=data.get("exclusions", []),
            inclusions=data.get("inclusions", []),
            notes=data.get("notes", [])
        )
