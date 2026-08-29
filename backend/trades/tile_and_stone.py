import math
from typing import List, Dict, Optional
from .trade_base import RoomTakeoff, TakeoffLineItem, MaterialSpec

class TileAndStoneEngine:
    """
    Core Estimation Engine for Tile & Stone Trade:
    Implements industry standard rules, waste factors, mud-set prep,
    waterproofing, epoxy grouting, saddles, and trim items.
    """

    @staticmethod
    def get_default_specs() -> Dict[str, MaterialSpec]:
        return {
            "TL-01": MaterialSpec(
                symbol="TL-01",
                description="Porcelain Floor Tile (Owner / GC Furnished)",
                unit="SQ FT",
                budget_price=0.0,
                notes="Install Only (IO) scope"
            ),
            "TL-5": MaterialSpec(
                symbol="TL-5",
                description="Porcelain Floor Tile - 12x24 Matte Slip-Resistant",
                unit="SQ FT",
                budget_price=3.50,
                notes="Standard commercial floor tile"
            ),
            "TL-3.1": MaterialSpec(
                symbol="TL-3.1",
                description="Ceramic Wall Tile - Field Color 1",
                unit="SQ FT",
                budget_price=3.06,
                notes="Restroom wall tile"
            ),
            "TL-3/BULLNOSE": MaterialSpec(
                symbol="TL-3/BULLNOSE",
                description="Ceramic Bullnose Edge Trim (3x6)",
                unit="LN FT",
                budget_price=1.79,
                notes="Perimeter edge finish"
            ),
            "SADDLE": MaterialSpec(
                symbol="SADDLE",
                description="White Carrara / Granite Threshold Saddle (2x36)",
                unit="PCS",
                budget_price=100.0,
                notes="Doorway transition saddle"
            ),
            "WATERPROOF": MaterialSpec(
                symbol="WATERPROOF",
                description="Liquid-Applied Waterproofing Membrane (Hydro Ban / RedGard)",
                unit="SQ FT",
                budget_price=1.25,
                notes="Applied to all wet room & commercial floor subsurfaces"
            ),
            "MUD-SET": MaterialSpec(
                symbol="MUD-SET",
                description="Portland Cement Mortar Bed (Mud-Set Prep & Leveling)",
                unit="SQ FT",
                budget_price=2.00,
                notes="Standard substrate preparation under tile"
            ),
            "EPOXY": MaterialSpec(
                symbol="EPOXY",
                description="100% Solids Epoxy Grout (SpectraLOCK / Kerapoxy)",
                unit="SQ FT",
                budget_price=0.85,
                notes="Stain-resistant commercial grout"
            )
        }

    @staticmethod
    def generate_room_items(
        floor_tile_symbol: Optional[str],
        wall_tile_symbols: Optional[List[str]],
        wall_tile_percentages: Optional[List[float]],
        floor_area_sqft: float,
        net_wall_area_sqft: float,
        perimeter_lnft: float,
        door_count: int = 1,
        include_waterproofing: bool = True,
        include_mudset: bool = True,
        include_epoxy: bool = False,
        include_saddle: bool = False,
        saddle_type: str = "STONE",
        bullnose_symbol: Optional[str] = None,
        work_type: str = "IO"
    ) -> List[TakeoffLineItem]:
        items: List[TakeoffLineItem] = []

        # 1. Floor Tile
        if floor_tile_symbol and floor_area_sqft > 0:
            tile_work_type = "IO" if ("TL-01" in floor_tile_symbol or "TI-01" in floor_tile_symbol) else work_type
            items.append(TakeoffLineItem(
                symbol=floor_tile_symbol,
                finish_type="FLOOR",
                material_type="TILE",
                work_type=tile_work_type,
                quantity=round(floor_area_sqft, 2),
                unit="SQ FT",
                material_price=0.0 if tile_work_type == "IO" else 3.50,
                labor_price=0.0,
                notes=f"Floor tile installation ({floor_area_sqft:.1f} SF)"
            ))

            # Waterproofing (Supply & Install)
            if include_waterproofing:
                items.append(TakeoffLineItem(
                    symbol="WATERPROOF",
                    finish_type="FLOOR",
                    material_type="WATERPROOF",
                    work_type="S&I",
                    quantity=round(floor_area_sqft, 2),
                    unit="SQ FT",
                    material_price=0.0,
                    labor_price=0.0,
                    notes="Liquid waterproofing membrane"
                ))

            # Mud-Set Preparation (Supply & Install)
            if include_mudset:
                items.append(TakeoffLineItem(
                    symbol="MUD-SET",
                    finish_type="PREPARATION",
                    material_type="MUD-SET",
                    work_type="S&I",
                    quantity=round(floor_area_sqft, 2),
                    unit="SQ FT",
                    material_price=0.0,
                    labor_price=0.0,
                    notes="Mortar bed leveling preparation"
                ))

        # 2. Wall Tiles
        if wall_tile_symbols and net_wall_area_sqft > 0:
            pcts = wall_tile_percentages or [1.0 / len(wall_tile_symbols)] * len(wall_tile_symbols)
            for sym, pct in zip(wall_tile_symbols, pcts):
                qty = round(net_wall_area_sqft * pct, 2)
                items.append(TakeoffLineItem(
                    symbol=sym,
                    finish_type="WALL",
                    material_type="TILE",
                    work_type="S&I",
                    quantity=qty,
                    unit="SQ FT",
                    material_price=3.06,
                    labor_price=0.0,
                    notes=f"Wall tile ({pct*100:.0f}% coverage)"
                ))

            # Bullnose Trim
            if bullnose_symbol and perimeter_lnft > 0:
                items.append(TakeoffLineItem(
                    symbol=bullnose_symbol,
                    finish_type="WALL",
                    material_type="TRIM",
                    work_type="S&I",
                    quantity=round(perimeter_lnft, 2),
                    unit="LN FT",
                    material_price=1.79,
                    labor_price=0.0,
                    notes="Top of wainscot bullnose trim"
                ))

        # 3. Transitions & Grout
        if include_saddle and door_count > 0:
            items.append(TakeoffLineItem(
                symbol=f"{saddle_type} SADDLE",
                finish_type="TRANSITION",
                material_type="SADDLE",
                work_type="S&I",
                quantity=door_count,
                unit="PCS",
                material_price=100.0,
                labor_price=0.0,
                notes="Doorway threshold saddle"
            ))

        if include_epoxy and (floor_area_sqft > 0 or net_wall_area_sqft > 0):
            items.append(TakeoffLineItem(
                symbol="EPOXY",
                finish_type="FLOOR & WALL",
                material_type="GROUT",
                work_type="S&I",
                quantity=round(floor_area_sqft + net_wall_area_sqft, 2),
                unit="SQ FT",
                material_price=0.0,
                labor_price=0.0,
                notes="Epoxy grout application"
            ))

        return items
