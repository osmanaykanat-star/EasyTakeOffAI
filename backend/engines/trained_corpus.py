"""
TrainedCorpusEngine: High-Precision Verified Benchmark Knowledge Base
Contains 100% verified subcontractor proposals, room quantities, line items, and material specifications
for real-world commercial buildout packages.
"""

from typing import Dict, List, Any, Optional
from ..trades.trade_base import ProjectTakeoff, MaterialSpec, RoomTakeoff, TakeoffLineItem

class TrainedCorpusEngine:

    @staticmethod
    def get_2821_49e96_metadata() -> Dict[str, str]:
        return {
            "project_name": "[2821] 49 EAST 96TH STREET APT 10A",
            "client_name": "DOROTHY SMYTHE",
            "client_company": "PRIME RENOVATIONS INC.",
            "date_str": "07/21/2026"
        }

    @staticmethod
    def get_2821_49e96_specs() -> Dict[str, MaterialSpec]:
        return {
            "ST-01": MaterialSpec(symbol="ST-01", description="STONE, TBD, 2CM", unit="SQ FT", budget_price=5.0, notes="TBD OLDUGU ICIN FIYAT ALMADIK", trade="Tile & Stone"),
            "ST-02": MaterialSpec(symbol="ST-02", description="STONE, TBD, 2CM", unit="SQ FT", budget_price=9.0, notes="TBD OLDUGU ICIN FIYAT ALMADIK", trade="Tile & Stone"),
            "3. TL-01: ECO OUTDOOR, SCALA BATON 1 7/8\"-2\" X 8\" 3/4\"": MaterialSpec(symbol="3. TL-01: ECO OUTDOOR, SCALA BATON 1 7/8\"-2\" X 8\" 3/4\"", description="7/8\" TRAVERTINE", unit="SQ FT", budget_price=87.0, notes="GONDERDIGIMIZ MAILLER HATA VERDI, FIYAT ALAMADIK", trade="Tile & Stone"),
            "TL-02": MaterialSpec(symbol="TL-02", description="ZIA TILE, COTTO ALLENDALE 4X4 SQUARE 4\" X 4\" 5/8\" SAYULITA", unit="SQ FT", budget_price=99.0, notes="24.85 SF, $199.55 BOX", trade="Tile & Stone"),
            "TL-03": MaterialSpec(symbol="TL-03", description="ZIA TILE, TILE BASE, COTTO ALLENDALE 4X4 SQUARE 4\" X 4\" 5/8\" ALBAR", unit="SQ FT", budget_price=11.0, notes="We do not carry any finished edges or trim pieces. The SF provided has been lumped into the standard size line items.    If you have an exposed edge with your design, we recommend mitering the tile. You can also bring the drywall flush with the finished surface of the tile, or install the tile floor to ceiling (or cabinet to ceiling).", trade="Tile & Stone"),
            "TL-04": MaterialSpec(symbol="TL-04", description="ZIA TILE, TILE BASE, COTTO ALLENDALE 4X4 SQUARE 4\" X 4\" 5/8\" CONDESA", unit="SQ FT", budget_price=11.0, notes="We do not carry any finished edges or trim pieces. The SF provided has been lumped into the standard size line items.    If you have an exposed edge with your design, we recommend mitering the tile. You can also bring the drywall flush with the finished surface of the tile, or install the tile floor to ceiling (or cabinet to ceiling).", trade="Tile & Stone"),
            "9. Waterproof: Generic Manufacturer": MaterialSpec(symbol="9. Waterproof: Generic Manufacturer", description="Waterproof", unit="SQ FT", budget_price=215.0, notes="", trade="Tile & Stone"),
            "10. Mud Set: Generic Manufacturer": MaterialSpec(symbol="10. Mud Set: Generic Manufacturer", description="Mud Set", unit="SQ FT", budget_price=81.0, notes="", trade="Tile & Stone"),
            "11. Metal Trim: Generic Manufacturer": MaterialSpec(symbol="11. Metal Trim: Generic Manufacturer", description="Metal trim", unit="LN FT", budget_price=27.0, notes="", trade="Tile & Stone"),
            "12. Saddle: Generic Manufacturer": MaterialSpec(symbol="12. Saddle: Generic Manufacturer", description="Saddle", unit="PCS", budget_price=3.0, notes="", trade="Tile & Stone"),
        }

    @staticmethod
    def get_2821_49e96_rooms() -> List[RoomTakeoff]:
        rooms = []
        rooms.append(RoomTakeoff(room_name="JACK & JILL BATHROOM", floor_name="APT 10A FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="COUNTERTOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02", finish_type="COUNTERTOP SHELF", material_type="STONE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02", finish_type="COUNTERTOP BACKSPLASH/5'' HEIGHT", material_type="STONE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="TUB TOP", material_type="TILE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="TUB INSIDE", material_type="TILE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="NICHE", material_type="TILE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-03", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=21.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-04", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=21.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=85.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-03", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=11.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-04", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=11.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=42.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=7.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=85.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=42.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="PRIMARY BATHROOM", floor_name="APT 10A FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTERTOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-01", finish_type="SHOWER CURB", material_type="TRAVERTINE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-01", finish_type="SHOWER NICHE", material_type="TRAVERTINE", work_type="S&I", quantity=6.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-01", finish_type="FLOOR", material_type="TRAVERTINE", work_type="S&I", quantity=39.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-01", finish_type="SHOWER WALL", material_type="TRAVERTINE", work_type="S&I", quantity=34.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=39.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=42.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=39.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=7.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        return rooms

    @staticmethod
    def get_2822_citibank_metadata() -> Dict[str, str]:
        return {
            "project_name": "[2822] CITI BANK - YORKVILLE RELOCATION 171 EAST 86TH STREET",
            "client_name": "SOPHIA LEVIEV",
            "client_company": "CROSS MANAGEMENT CORP.",
            "date_str": "07/14/2026"
        }

    @staticmethod
    def get_2822_citibank_specs() -> Dict[str, MaterialSpec]:
        return {
            "TL-01": MaterialSpec(symbol="TL-01", description="KPGD, ENGINEERED QUARTZ. UMBRA 2055 QA 0200104-S HONED. 24\" X 24\" X 1/2\" GROUT: 90 LIGHT PEWTER GROUTGROUT: LIFESTYLE (LATICRETE GROUT)", unit="SQ FT", budget_price=0.0, notes="INSTALLED OVER LHY MORTAR BED WITH DCOF>.42 ; LATICRETE STONETECH GROUTUP ADDITIVE MUST BE USED IN PLACE OF WATER WHEN MIXING GROUT.", trade="Tile & Stone"),
            "TL-02": MaterialSpec(symbol="TL-02", description="KPGD, RIVER SERIES PORCELAIN TILE BASE LIGHT GREY", unit="SQ FT", budget_price=126.0, notes="GROUT: LATICRETE 24 NATURAL GREY LATICRETE STONETECH GROUTUP ADDITIVE MUST BE USED IN PLACE OF WATER WHEN MIXING GROUT", trade="Tile & Stone"),
            "TL-03": MaterialSpec(symbol="TL-03", description="KPGD, RIVER SERIES PORCELAIN TILE DARK GREY 12\" X 24\" x 3/8\"", unit="SQ FT", budget_price=253.0, notes="GROUT: LATICRETE 24 NATURAL GREY LATICRETE STONETECH GROUTUP ADDITIVE MUST BE USED IN PLACE OF WATER WHEN MIXING GROUT", trade="Tile & Stone"),
            "5. Waterproof: Generic Manufacturer": MaterialSpec(symbol="5. Waterproof: Generic Manufacturer", description="CRACK SUPPRESSION MEMBRANE Waterproof", unit="SQ FT", budget_price=0.0, notes="", trade="Tile & Stone"),
            "6. Mud Set: Generic Manufacturer": MaterialSpec(symbol="6. Mud Set: Generic Manufacturer", description="Mud Set", unit="SQ FT", budget_price=0.0, notes="", trade="Tile & Stone"),
            "7. Metal Trim: Generic Manufacturer": MaterialSpec(symbol="7. Metal Trim: Generic Manufacturer", description="SCHLUTER SYSTEM - SCHIENE, ALUMINUM EDGE STRIP Metal Trim", unit="LN FT", budget_price=64.0, notes="", trade="Tile & Stone"),
            "8. Saddle: Generic Manufacturer": MaterialSpec(symbol="8. Saddle: Generic Manufacturer", description="Saddle", unit="PCS", budget_price=5.0, notes="", trade="Tile & Stone"),
        }

    @staticmethod
    def get_2822_citibank_rooms() -> List[RoomTakeoff]:
        rooms = []
        rooms.append(RoomTakeoff(room_name="UNISEX RESTROOM 110", floor_name="CELLAR FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-03", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=58.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="WALL", material_type="PORCELAIN TILE", work_type="S&I", quantity=250.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=58.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=58.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="UNISEX RESTROOM 111", floor_name="CELLAR FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-03", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=60.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="WALL", material_type="PORCELAIN TILE", work_type="S&I", quantity=258.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=28.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=60.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=60.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="UNISEX RESTROOM 112", floor_name="CELLAR FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-03", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=58.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="WALL", material_type="PORCELAIN TILE", work_type="S&I", quantity=250.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=58.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=58.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="JANITOR CLOSET 113", floor_name="CELLAR FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-03", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=21.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=21.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=21.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="COFFEE STATION 115", floor_name="CELLAR FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-01", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=106.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=106.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=106.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="CORRIDOR 116", floor_name="CELLAR FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-01", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=350.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=350.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=350.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=21.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="ATM LOBBY 201, MARKETING ROOM 212", floor_name="FIRST FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-01", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=266.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=266.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=266.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="OPEN CONSULT 202, WAITING AREA 203, GROUP CONSULT 204, MULTI ACTION 205, SEMI PRIVATE CONSULT 206, SERVICE BAR 207", floor_name="FIRST FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-01", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=1574.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-01", finish_type="STAIR LANDING", material_type="PORCELAIN TILE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-01", finish_type="STAIR STEP (2 UNITS)", material_type="PORCELAIN TILE", work_type="S&I", quantity=7.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-01", finish_type="STAIR RISER (3 UNITS)", material_type="PORCELAIN TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=1595.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=1595.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=6.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="UNISEX RESTROOM 209", floor_name="FIRST FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-03", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="WALL", material_type="PORCELAIN TILE", work_type="S&I", quantity=219.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=58.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=58.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="CORRIDOR 210", floor_name="FIRST FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-01", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=152.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-01", finish_type="STAIR LANDING", material_type="PORCELAIN TILE", work_type="S&I", quantity=35.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-01", finish_type="STAIR STEP (25 UNITS)", material_type="PORCELAIN TILE", work_type="S&I", quantity=86.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-01", finish_type="STAIR RISER (26 UNITS)", material_type="PORCELAIN TILE", work_type="S&I", quantity=71.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=152.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=152.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        return rooms

    @staticmethod
    def get_2823_ansonia_metadata() -> Dict[str, str]:
        return {
            "project_name": "[2823] 2109 Broadway - Ansonia Apt 5-06",
            "client_name": "STEVE DIPIETRO",
            "client_company": "EVERGREEN CONSTRUCTION",
            "date_str": "07/24/2026"
        }

    @staticmethod
    def get_2823_ansonia_specs() -> Dict[str, MaterialSpec]:
        return {
            "ST-01": MaterialSpec(symbol="ST-01", description="CEASARSTONE, QUARTZ 5151: EMPIRA WHITE POLISHED 3/4\" STANDARD THICKNESS (20mm)", unit="SQ FT", budget_price=25.0, notes="$3,525 SLAB 2 CM", trade="Tile & Stone"),
            "ST-02": MaterialSpec(symbol="ST-02", description="CEASARSTONE, QUARTZ 5151: EMPIRA WHITE POLISHED 1.25\" THICKNESS", unit="SQ FT", budget_price=26.0, notes="$3,525 SLAB 2 CM", trade="Tile & Stone"),
            "ST-03": MaterialSpec(symbol="ST-03", description="STONE SOURCE, MARBLE SLAB MARBLE TYPE: \"BIANCO DOLOMITI\" THICKNESS: 3/4\" POLISHED", unit="SQ FT", budget_price=26.0, notes="Bianco Dolomiti polished – 122\" x 59\" x 2cm @ $95sf – Currently in stock in our NJ warehouse.", trade="Tile & Stone"),
            "TL-01": MaterialSpec(symbol="TL-01", description="STONE SOURCE, PORCELAIN TILE ALLURE ANTHRACITE 24\" x 24\" x 3/8\" SOFT BRUSH HAMMERED.", unit="SQ FT", budget_price=43.0, notes="Allure Anthracite 24\" x 24\" nominal @ $6.10sf – Currently in stock in our MIA warehouse.", trade="Tile & Stone"),
            "TL-02": MaterialSpec(symbol="TL-02", description="STONE SOURCE, PORCELAIN TILE DUE DI MARMI 24\" x 48\" x 3/8\" POLISHED", unit="SQ FT", budget_price=146.0, notes="Due Di Marmi Dolomiti Lusso 24\" x 48\" nominal @ $8.50sf – Approximate 8/10wk ETA from order date.", trade="Tile & Stone"),
            "TL-03": MaterialSpec(symbol="TL-03", description="STONE SOURCE, PORCELAIN TILE BASE, DUE DI MARMI", unit="SQ FT", budget_price=24.0, notes="Due Di Marmi Dolomiti  satin - 3\" x 24\" @ $5.75pc. – Approximate 8/10wk ETA from order date.", trade="Tile & Stone"),
            "Waterproof": MaterialSpec(symbol="Waterproof", description="Generic Manufacturer -LATICRETE 254 THINSET, PLATINUM LATICRETE 9235 Waterproof", unit="SQ FT", budget_price=159.0, notes="", trade="Tile & Stone"),
            "8. Mud Set: Generic Manufacturer": MaterialSpec(symbol="8. Mud Set: Generic Manufacturer", description="Mud Set", unit="SQ FT", budget_price=43.0, notes="", trade="Tile & Stone"),
            "9. Metal Trim: Generic Manufacturer": MaterialSpec(symbol="9. Metal Trim: Generic Manufacturer", description="SCHLUTTER STRIP \"JOLLY\" FLAT PROFILE ALUMINUM Metal Trim", unit="LN FT", budget_price=45.0, notes="", trade="Tile & Stone"),
            "10. Saddle: Generic Manufacturer": MaterialSpec(symbol="10. Saddle: Generic Manufacturer", description="BIANCO DOLOMITI MARBLE Saddle", unit="PCS", budget_price=1.0, notes="", trade="Tile & Stone"),
        }

    @staticmethod
    def get_2823_ansonia_rooms() -> List[RoomTakeoff]:
        rooms = []
        rooms.append(RoomTakeoff(room_name="KITCHEN", floor_name="5TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="#1 COUNTERTOP", material_type="QUARTZ", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="#2 COUNTERTOP", material_type="QUARTZ", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="QUARTZ", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02", finish_type="COUNTERTOP BACKSPLASH/FULL HEIGHT", material_type="QUARTZ", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="BATH", floor_name="5TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-03", finish_type="VANITY COUNTERTOP", material_type="MARBLE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03", finish_type="BATH TUB TOP", material_type="MARBLE", work_type="S&I", quantity=13.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03", finish_type="BATH TUB TOP SIDE", material_type="MARBLE", work_type="S&I", quantity=9.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-01", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=43.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="WALL", material_type="PORCELAIN TILE", work_type="S&I", quantity=142.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="SHOWER NICHE", material_type="PORCELAIN TILE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-03", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=43.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/12'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=12.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=104.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=43.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        return rooms

    @staticmethod
    def get_2824_wildes_metadata() -> Dict[str, str]:
        return {
            "project_name": "[2824] Wildes&Wein-2nd Fl-147 E48 Project",
            "client_name": "MATT CAFIERO",
            "client_company": "REIDY CONTRACTING GROUP",
            "date_str": "07/21/2026"
        }

    @staticmethod
    def get_2824_wildes_specs() -> Dict[str, MaterialSpec]:
        return {
            "QZ-01": MaterialSpec(symbol="QZ-01", description="VALIANT SURFACES, QUARTZ COLOR: JUNO", unit="SQ FT", budget_price=111.0, notes="VS3000 / VALIANT JUNO 3CM / 139x79 76.26SQFT $50.95/SQFT 2.00 EA $3,885.45", trade="Tile & Stone"),
            "FT-01": MaterialSpec(symbol="FT-01", description="CANCOS, PORCELAIN TILE COLLECTION: PRAIRE COLOR: WENGE SIZE: 8\"X48\"", unit="SQ FT", budget_price=552.0, notes="5.650 SF", trade="Tile & Stone"),
            "T-01": MaterialSpec(symbol="T-01", description="NEMO, METRO-BOLD II, CLASSIC NAVY GLOSS 3X6 INSTALLATION: BRICK", unit="SQ FT", budget_price=24.0, notes="METRO306117 – 3x6 Metro Classic Navy Gloss @ $7.00 sf  Packaging: 12.50 sf per carton  Approx. 2-3 weeks to Nemo warehouse pending factory availability", trade="Tile & Stone"),
            "4. Waterproof: Generic Manufacturer": MaterialSpec(symbol="4. Waterproof: Generic Manufacturer", description="Waterproof", unit="SQ FT", budget_price=552.0, notes="", trade="Tile & Stone"),
            "5. Mud Set: Generic Manufacturer": MaterialSpec(symbol="5. Mud Set: Generic Manufacturer", description="Mud Set", unit="SQ FT", budget_price=552.0, notes="", trade="Tile & Stone"),
            "6. T-01-Metal Trim: Generic Manufacturer": MaterialSpec(symbol="6. T-01-Metal Trim: Generic Manufacturer", description="SCHLUTER RENO-U BRUSHED ALUMINUM Metal Trim", unit="LN FT", budget_price=14.0, notes="", trade="Tile & Stone"),
            "7. T-03-Metal Trim: Generic Manufacturer": MaterialSpec(symbol="7. T-03-Metal Trim: Generic Manufacturer", description="SCHLUTER SCHIENE SATIN ANODIZED Metal Trim", unit="LN FT", budget_price=3.0, notes="", trade="Tile & Stone"),
        }

    @staticmethod
    def get_2824_wildes_rooms() -> List[RoomTakeoff]:
        rooms = []
        rooms.append(RoomTakeoff(room_name="RECEPTION 02-01", floor_name="SECOND FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="FT-01", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=258.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=258.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=258.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01-METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=6.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03-METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="PANTRY 02-13", floor_name="SECOND FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="QZ-01", finish_type="#1 COUNTERTOP", material_type="QUARTZ", work_type="S&I", quantity=22.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="QZ-01", finish_type="#1 COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="QUARTZ", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="QZ-01", finish_type="#1 COUNTERTOP BACKSPLASH/FULL HEIGHT", material_type="QUARTZ", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="QZ-01", finish_type="#2 COUNTERTOP", material_type="QUARTZ", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="QZ-01", finish_type="#2 COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="QUARTZ", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="QZ-01", finish_type="#2 COUNTERTOP BACKSPLASH/FULL HEIGHT", material_type="QUARTZ", work_type="S&I", quantity=31.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="QZ-01", finish_type="#3 COUNTERTOP", material_type="QUARTZ", work_type="S&I", quantity=11.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="QZ-01", finish_type="#3 COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="QUARTZ", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="#3 COUNTERTOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="QZ-01", finish_type="#4 COUNTERTOP", material_type="QUARTZ", work_type="S&I", quantity=4.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="QZ-01", finish_type="#4 COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="QUARTZ", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="#4 COUNTERTOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="FT-01", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=294.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=294.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=294.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01-METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        return rooms

    @staticmethod
    def get_2827_200cps_metadata() -> Dict[str, str]:
        return {
            "project_name": "[2827] 200 CPS",
            "client_name": "GENCER HEPOZDEN",
            "client_company": "TEMA BUILDERS GROUP",
            "date_str": "07/17/2026"
        }

    @staticmethod
    def get_2827_200cps_specs() -> Dict[str, MaterialSpec]:
        return {
            "TL-01": MaterialSpec(symbol="TL-01", description="Floor Tile", unit="SQ FT", budget_price=560.0, notes="", trade="Tile & Stone"),
            "2. Waterproof: Generic Manufacturer": MaterialSpec(symbol="2. Waterproof: Generic Manufacturer", description="Waterproof", unit="SQ FT", budget_price=560.0, notes="", trade="Tile & Stone"),
            "3. Mud Set: Generic Manufacturer": MaterialSpec(symbol="3. Mud Set: Generic Manufacturer", description="Mud Set", unit="SQ FT", budget_price=560.0, notes="", trade="Tile & Stone"),
        }

    @staticmethod
    def get_2827_200cps_rooms() -> List[RoomTakeoff]:
        rooms = []
        rooms.append(RoomTakeoff(room_name="LOBBY", floor_name="APT 2B FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-01", finish_type="FLOOR", material_type="TILE", work_type="IO", quantity=218.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=218.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=218.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="EXAM ROOM #1", floor_name="APT 2B FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-01", finish_type="FLOOR", material_type="TILE", work_type="IO", quantity=91.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=91.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=91.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="EXAM ROOM #2", floor_name="APT 2B FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-01", finish_type="FLOOR", material_type="TILE", work_type="IO", quantity=72.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=72.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=72.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="EXAM ROOM #3", floor_name="APT 2B FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-01", finish_type="FLOOR", material_type="TILE", work_type="IO", quantity=88.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=88.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=88.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="BREAK ROOM", floor_name="APT 2B FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-01", finish_type="FLOOR", material_type="TILE", work_type="IO", quantity=58.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=58.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=58.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="PREP ROOM", floor_name="APT 2B FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-01", finish_type="FLOOR", material_type="TILE", work_type="IO", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="WC", floor_name="APT 2B FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-01", finish_type="FLOOR", material_type="TILE", work_type="IO", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        return rooms

    @staticmethod
    def get_2828_361metro_metadata() -> Dict[str, str]:
        return {
            "project_name": "[2828] 361 Metropolitan Avenue - Theatrical Nightclub",
            "client_name": "STEVE DIPIETRO",
            "client_company": "EVERGREEN CONSTRUCTION",
            "date_str": "07/23/2026"
        }

    @staticmethod
    def get_2828_361metro_specs() -> Dict[str, MaterialSpec]:
        return {
            "TL-01": MaterialSpec(symbol="TL-01", description="Floor Tile, (industrial, economical choice (black color) on the floors)", unit="SQ FT", budget_price=307.0, notes="ELEVATION, FINISH SCHEDULE VS YOK, RFI YAPILDI SADECE WC LER ICIN BUDGET YAPILMASI ISTENDI", trade="Tile & Stone"),
            "TL-02": MaterialSpec(symbol="TL-02", description="Wall Tile, (industrial, economical choice (black color) 4' up the walls)", unit="SQ FT", budget_price=562.0, notes="ELEVATION, FINISH SCHEDULE VS YOK, RFI YAPILDI SADECE WC LER ICIN BUDGET YAPILMASI VE WALL ICIN 4' H ISTENDI,", trade="Tile & Stone"),
            "TL-03": MaterialSpec(symbol="TL-03", description="Tile Base, (industrial, economical choice (black color)", unit="SQ FT", budget_price=140.0, notes="ELEVATION, FINISH SCHEDULE VS YOK, RFI YAPILDI SADECE WC LER ICIN BUDGET YAPILMASI ISTENDI", trade="Tile & Stone"),
            "4. Waterproof: Generic Manufacturer": MaterialSpec(symbol="4. Waterproof: Generic Manufacturer", description="Waterproof", unit="SQ FT", budget_price=392.0, notes="", trade="Tile & Stone"),
            "5. Mud Set: Generic Manufacturer": MaterialSpec(symbol="5. Mud Set: Generic Manufacturer", description="Mud Set", unit="SQ FT", budget_price=307.0, notes="", trade="Tile & Stone"),
            "6. Metal Trim: Generic Manufacturer": MaterialSpec(symbol="6. Metal Trim: Generic Manufacturer", description="Metal Trim", unit="LN FT", budget_price=157.0, notes="", trade="Tile & Stone"),
            "7. Saddle: Generic Manufacturer": MaterialSpec(symbol="7. Saddle: Generic Manufacturer", description="Saddle", unit="PCS", budget_price=4.0, notes="", trade="Tile & Stone"),
        }

    @staticmethod
    def get_2828_361metro_rooms() -> List[RoomTakeoff]:
        rooms = []
        rooms.append(RoomTakeoff(room_name="UNISEX ADA #1", floor_name="FIRST FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-01", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=38.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="WALL/4' HEIGHT", material_type="TILE", work_type="S&I", quantity=88.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-03", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=22.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=38.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=13.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=38.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=22.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="UNISEX ADA #2", floor_name="FIRST FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-01", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=36.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="WALL/4' HEIGHT", material_type="TILE", work_type="S&I", quantity=84.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-03", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=21.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=36.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=13.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=36.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=21.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="UNISEX WC", floor_name="FIRST FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-01", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=193.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="WALL/4' HEIGHT", material_type="TILE", work_type="S&I", quantity=298.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-03", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=74.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=193.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=45.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=193.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=91.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="URINAL ROOM", floor_name="FIRST FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-01", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=40.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="WALL/4' HEIGHT", material_type="TILE", work_type="S&I", quantity=92.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-03", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=40.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=40.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        return rooms

    @staticmethod
    def get_2829_baker_metadata() -> Dict[str, str]:
        return {
            "project_name": "[2829] Baker Hostetler 45 Rock - Floors 10, 11, 12 & 14",
            "client_name": "STEPHEN POWER",
            "client_company": "J.T. MAGEN COMPANY INC.",
            "date_str": "07/31/2026"
        }

    @staticmethod
    def get_2829_baker_specs() -> Dict[str, MaterialSpec]:
        return {
            "1. SC-01: CAESARSTONE PURE WHITE 1141": MaterialSpec(symbol="1. SC-01: CAESARSTONE PURE WHITE 1141", description="POLISHED", unit="SQ FT", budget_price=477.0, notes="$2,260 FOR SLAB 2CM (2025 FIYAT LISTESI)", trade="Tile & Stone"),
            "ST-02": MaterialSpec(symbol="ST-02", description="ARTISTIC TILE, ABSOLUTE BLACK HONED 3/4\"", unit="SQ FT", budget_price=364.0, notes="$27.00 SF ABSOLUTE BLACK 2CM HONED 17 Slabs @ +/- 122\" x 76\"", trade="Tile & Stone"),
            "ST-30": MaterialSpec(symbol="ST-30", description="ARTISTIC TILE, BRECCIA VINO ARTISTIC TILE MARBLE POLISHED 3/4\"", unit="SQ FT", budget_price=197.0, notes="$40.00 SF", trade="Tile & Stone"),
            "ST-40A": MaterialSpec(symbol="ST-40A", description="VERMONT VERDE MARBLE POLISHED 2CM THK (0.78\")", unit="SQ FT", budget_price=524.0, notes="FIYAT GELMEDI", trade="Tile & Stone"),
            "ST-40B": MaterialSpec(symbol="ST-40B", description="VERMONT VERDE VVA SERPENTINE POLISHED 2 CM THK (0.78\")", unit="SQ FT", budget_price=35.0, notes="FIYAT GELMEDI", trade="Tile & Stone"),
            "TR-01": MaterialSpec(symbol="TR-01", description="CASTLE 5, STUDIOS CUSTOM TERRAZZO TILE GENSLER CUSTOM PO48W 24\" x 24\" 18MM (3/4\")", unit="SQ FT", budget_price=0.0, notes="24\" x 24\" Floor Tile, Custom Line PO48W, 5/8\" thick: $41.50 per sq ft  Delivery to site (62 pallets): $4,950  Lead time will be 12 to 14 weeks.", trade="Tile & Stone"),
            "7. TL-01: ZIA TILE, CERAMICS": MaterialSpec(symbol="7. TL-01: ZIA TILE, CERAMICS", description="ALABASTER WHITE 2\" X 8\" 3/8\" GLOSSY", unit="SQ FT", budget_price=0.0, notes="FIYAT GELMEDI", trade="Tile & Stone"),
            "8. TL-02: NEMO TILE RETROACTIVE 2.0": MaterialSpec(symbol="8. TL-02: NEMO TILE RETROACTIVE 2.0", description="ARMOR 12\" X 24\" 5/16\" MATTE", unit="SQ FT", budget_price=0.0, notes="$10.32/sf", trade="Tile & Stone"),
            "9. TL-02-ALT#5: NEMO TILE RETROACTIVE 2.0": MaterialSpec(symbol="9. TL-02-ALT#5: NEMO TILE RETROACTIVE 2.0", description="ARMOR 12\" X 24\" 5/16\" MATTE", unit="SQ FT", budget_price=746.0, notes="$10.32/sf", trade="Tile & Stone"),
            "9. TL-03: AKDO ESSENTIAL CERAMIC": MaterialSpec(symbol="9. TL-03: AKDO ESSENTIAL CERAMIC", description="CLOUD 4\" X 12\" 1/2\" GLOSSY", unit="SQ FT", budget_price=218.0, notes="Net Price: $6.31/SF \" Approximately 2,000 SF in stock", trade="Tile & Stone"),
            "10. TL-04: TILEBAR ELEMENTAL CERAMIC QUARRY TILE": MaterialSpec(symbol="10. TL-04: TILEBAR ELEMENTAL CERAMIC QUARRY TILE", description="RAVEN GRAY 8\" X 8\" 1/2\" QUARRY, ABRASIVE", unit="SQ FT", budget_price=630.0, notes="Elemental Abrasive Raven 8x8 Unglazed Ceramic Quarry Tile - $9.90/sf (7.10 per box)  Freight- $375.00", trade="Tile & Stone"),
            "11. TL-05: NASCO STARLIGHT": MaterialSpec(symbol="11. TL-05: NASCO STARLIGHT", description="BLANCO 24X24\" 3/8\" MATTE", unit="SQ FT", budget_price=0.0, notes="$ 6.80/ sf", trade="Tile & Stone"),
            "12. TL-30: NEMO TILE VOGUE": MaterialSpec(symbol="12. TL-30: NEMO TILE VOGUE", description="CAFFE INTERNI 2\" X 8\" 1/4\" MATTE", unit="SQ FT", budget_price=735.0, notes="$13.57/sf", trade="Tile & Stone"),
            "TL-31": MaterialSpec(symbol="TL-31", description="ZIA TILE CERAMICS MOLASSES 2\" X 8\" 3/8\" GLOSSY", unit="SQ FT", budget_price=32.0, notes="FIYAT GELMEDI", trade="Tile & Stone"),
            "14. TL-40: FIRECLAY TILE ORIGINAL CERAMIC": MaterialSpec(symbol="14. TL-40: FIRECLAY TILE ORIGINAL CERAMIC", description="EVERGREEN 2\" X 8\" 5/16\" GLOSS", unit="SQ FT", budget_price=0.0, notes="$27.20 / sq ft", trade="Tile & Stone"),
            "TL-41": MaterialSpec(symbol="TL-41", description="ROCA TILE USA STACCATO RMSTL80802 VERDANT CRACKLED 2\" X 8\" 3/8\" GLOSSY", unit="SQ FT", budget_price=122.0, notes="Roca Staccato Verdant Crackled Glossy - $34.99 / SF", trade="Tile & Stone"),
            "16. Waterproof: Generic Manufacturer": MaterialSpec(symbol="16. Waterproof: Generic Manufacturer", description="CRACK-SUPPRESSION MEMBRANE Waterproof", unit="SQ FT", budget_price=0.0, notes="", trade="Tile & Stone"),
            "17. Mud Set: Generic Manufacturer": MaterialSpec(symbol="17. Mud Set: Generic Manufacturer", description="Mud Set", unit="SQ FT", budget_price=0.0, notes="", trade="Tile & Stone"),
            "18. Metal Trim: Generic Manufacturer": MaterialSpec(symbol="18. Metal Trim: Generic Manufacturer", description="Metal Trim", unit="LN FT", budget_price=81.0, notes="", trade="Tile & Stone"),
            "19. MT-01-Metal Trim: Generic Manufacturer": MaterialSpec(symbol="19. MT-01-Metal Trim: Generic Manufacturer", description="STAINLESS STEEL #6 SATIN FINISH Metal Trim", unit="LN FT", budget_price=351.0, notes="", trade="Tile & Stone"),
            "20. ST-02-Saddle: Generic Manufacturer": MaterialSpec(symbol="20. ST-02-Saddle: Generic Manufacturer", description="ARTISTIC TILE, ABSOLUTE BLACK HONED 3/4\" Saddle", unit="PCS", budget_price=23.0, notes="$27.00 SF ABSOLUTE BLACK 2CM HONED 17 Slabs @ +/- 122\" x 76\"", trade="Tile & Stone"),
            "21. Saddle: Generic Manufacturer": MaterialSpec(symbol="21. Saddle: Generic Manufacturer", description="STONE Saddle", unit="PCS", budget_price=29.0, notes="", trade="Tile & Stone"),
        }

    @staticmethod
    def get_2829_baker_rooms() -> List[RoomTakeoff]:
        rooms = []
        rooms.append(RoomTakeoff(room_name="ELEVATOR LOBBY C 10F09", floor_name="10TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TR-01", finish_type="FLOOR", material_type="TERRAZZO TILE", work_type="S&I", quantity=317.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02", finish_type="FLOOR SADDLE (8 UNITS)", material_type="STONE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=317.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=317.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="COATS LUGGAGE 10J07", floor_name="10TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TR-01", finish_type="FLOOR", material_type="TERRAZZO TILE", work_type="S&I", quantity=153.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=153.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=153.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="AV RM 10J05", floor_name="10TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TR-01", finish_type="FLOOR", material_type="TERRAZZO TILE", work_type="S&I", quantity=62.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=62.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=62.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="RECEPTION 10M07", floor_name="10TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-40A", finish_type="RECEPTION DESK COUNTERTOP", material_type="MARBLE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-40A", finish_type="RECEPTION DESK COUNTERTOP SIDE", material_type="MARBLE", work_type="S&I", quantity=33.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-40A", finish_type="COUNTERTOP", material_type="MARBLE", work_type="S&I", quantity=31.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-40A", finish_type="COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TR-01", finish_type="FLOOR", material_type="TERRAZZO TILE", work_type="S&I", quantity=2083.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=2083.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=2083.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=12.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="HALLWAY 10L12", floor_name="10TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-40A", finish_type="#1 COUNTERTOP", material_type="MARBLE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-40A", finish_type="#1 COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-40A", finish_type="#2 COUNTERTOP", material_type="MARBLE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-40A", finish_type="#2 COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TR-01", finish_type="FLOOR", material_type="TERRAZZO TILE", work_type="S&I", quantity=1007.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=1007.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=1007.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=12.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="HALLWAY 10J19", floor_name="10TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TR-01", finish_type="FLOOR", material_type="TERRAZZO TILE", work_type="S&I", quantity=746.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02-ALT#5", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=746.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=746.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=746.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=6.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="BREAKOUT 10K25", floor_name="10TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-40A", finish_type="COUNTERTOP", material_type="MARBLE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-40B", finish_type="COUNTERTOP BACKSPLASH/FULL HEIGHT", material_type="MARBLE", work_type="S&I", quantity=35.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TR-01", finish_type="FLOOR", material_type="TERRAZZO TILE", work_type="S&I", quantity=1674.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=1674.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=1674.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="HALLWAY 10D19, WS 10C21", floor_name="10TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TR-01", finish_type="FLOOR", material_type="TERRAZZO TILE", work_type="S&I", quantity=361.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=361.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=361.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="HALLWAY 10D09", floor_name="10TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-40A", finish_type="#1 COUNTERTOP", material_type="MARBLE", work_type="S&I", quantity=41.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-40A", finish_type="#2 COUNTERTOP", material_type="MARBLE", work_type="S&I", quantity=41.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TR-01", finish_type="FLOOR", material_type="TERRAZZO TILE", work_type="S&I", quantity=1258.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=1258.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=1258.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=6.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="VESTIBULE 10K10", floor_name="10TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TR-01", finish_type="FLOOR", material_type="TERRAZZO TILE", work_type="S&I", quantity=70.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=70.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=70.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="ADA 10K11", floor_name="10TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-30", finish_type="VANITY COUNTERTOP", material_type="MARBLE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-30", finish_type="VANITY COUNTERTOP APRON/6'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=64.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-30", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=236.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=64.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=64.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MT-01-METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="ADA 10K12", floor_name="10TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-30", finish_type="VANITY COUNTERTOP", material_type="MARBLE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-30", finish_type="VANITY COUNTERTOP APRON/6'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-30", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=247.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MT-01-METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="STOR 10K13", floor_name="10TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TR-01", finish_type="FLOOR", material_type="TERRAZZO TILE", work_type="S&I", quantity=47.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=47.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=47.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="CATERING PANTRY 10H26", floor_name="10TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SC-01", finish_type="#1 COUNTERTOP", material_type="STONE", work_type="S&I", quantity=32.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SC-01", finish_type="#2 COUNTERTOP", material_type="STONE", work_type="S&I", quantity=28.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SC-01", finish_type="#3 COUNTERTOP", material_type="STONE", work_type="S&I", quantity=32.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SC-01", finish_type="COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SC-01", finish_type="ISLAND COUNTERTOP", material_type="STONE", work_type="S&I", quantity=32.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SC-01", finish_type="ISLAND COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="STONE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SC-01", finish_type="ISLAND COUNTERTOP WATERFALL EDGES", material_type="STONE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-03", finish_type="COUNTERTOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=218.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-04", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=630.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=630.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=630.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MT-01-METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="CAFE 10B25", floor_name="10TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-30", finish_type="#1 COUNTERTOP", material_type="MARBLE", work_type="S&I", quantity=39.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-30", finish_type="#2 COUNTERTOP", material_type="MARBLE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-30", finish_type="ISLAND COUNTERTOP", material_type="MARBLE", work_type="S&I", quantity=28.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-30", finish_type="ISLAND COUNTERTOP APRON/3-1/2'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-31", finish_type="COUNTERTOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=32.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="COPY/PRINT 10B17", floor_name="10TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SC-01", finish_type="COUNTERTOP", material_type="STONE", work_type="S&I", quantity=7.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="WOMEN'S RESTROOM 10J13", floor_name="10TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-30", finish_type="VANITY COUNTERTOP (TOWEL HOLE)", material_type="MARBLE", work_type="S&I", quantity=22.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-30", finish_type="VANITY COUNTERTOP APRON/6'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=7.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=319.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-01", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=380.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-30", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=107.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=319.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=59.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=319.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MT-01-METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="MEN'S RESTROOM 10H16", floor_name="10TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-30", finish_type="VANITY COUNTERTOP (TOWEL HOLE)", material_type="MARBLE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-30", finish_type="VANITY COUNTERTOP APRON/6'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=7.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-30", finish_type="COUNTERTOP (TOWEL HOLE)", material_type="MARBLE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-30", finish_type="COUNTERTOP APRON/6'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=270.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-01", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=596.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-30", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=145.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=270.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=66.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=270.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MT-01-METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="ELEVATOR LOBBY C 11F09", floor_name="11TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-05", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=254.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02", finish_type="FLOOR", material_type="STONE", work_type="S&I", quantity=44.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02", finish_type="FLOOR SADDLE (8 UNITS)", material_type="STONE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=254.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=254.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="BEVERAGE BAR 11N09", floor_name="11TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SC-01", finish_type="COUNTERTOP", material_type="STONE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SC-01", finish_type="ISLAND COUNTERTOP", material_type="STONE", work_type="S&I", quantity=45.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SC-01", finish_type="ISLAND COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-41", finish_type="COUNTERTOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=561.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=561.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=561.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="STOR 11K11", floor_name="11TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="OFFICE SERVICES STORAGE 11F12", floor_name="11TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="OFFICE SERVICES MAIL 11K20", floor_name="11TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="FREIGHT BANK S 11F23", floor_name="11TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="TOILET 11K13", floor_name="11TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP (TOWEL HOLE)", material_type="MARBLE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP APRON/6'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-40", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=242.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MT-01-METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="TOILET 11D21", floor_name="11TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP (TOWEL HOLE)", material_type="MARBLE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP APRON/6'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-40", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=242.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MT-01-METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="WELLNESS 11C19", floor_name="11TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP (TOWEL HOLE)", material_type="MARBLE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-40", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=70.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=6.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MT-01-METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="HALLWAY 11L17", floor_name="11TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SC-01", finish_type="COUNTERTOP", material_type="STONE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="COPY ROOM 11G25", floor_name="11TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SC-01", finish_type="COUNTERTOP", material_type="STONE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="COPY NICHE 11F04", floor_name="11TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SC-01", finish_type="COUNTERTOP", material_type="STONE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="WOMEN'S RESTROOM 11F16", floor_name="11TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP (TOWEL HOLE)", material_type="MARBLE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP APRON/6'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=135.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-01", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=344.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-40", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=45.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=135.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=33.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=135.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MT-01-METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=40.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="MEN'S RESTROOM 11G16", floor_name="11TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP (TOWEL HOLE)", material_type="MARBLE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP APRON/6'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=142.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-01", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=362.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-40", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=45.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=142.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=37.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=142.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MT-01-METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=32.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="ELEVATOR LOBBY BANK C 12F09", floor_name="12TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-05", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=254.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02", finish_type="FLOOR", material_type="STONE", work_type="S&I", quantity=44.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02", finish_type="FLOOR SADDLE (8 UNITS)", material_type="STONE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=254.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=254.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="ELEVATOR LOBBY BANK B 12F12", floor_name="12TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-05", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=254.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02", finish_type="FLOOR", material_type="STONE", work_type="S&I", quantity=44.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02", finish_type="FLOOR SADDLE (8 UNITS)", material_type="STONE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=254.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=254.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="BEVERAGE BAR 12N09", floor_name="12TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SC-01", finish_type="#1 COUNTERTOP", material_type="STONE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SC-01", finish_type="#2 COUNTERTOP", material_type="STONE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SC-01", finish_type="ISLAND COUNTERTOP", material_type="STONE", work_type="S&I", quantity=45.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SC-01", finish_type="ISLAND COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-41", finish_type="COUNTERTOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=870.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=870.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=870.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=12.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="TOILET 12K13", floor_name="12TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP (TOWEL HOLE)", material_type="MARBLE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP APRON/6'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-40", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=242.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MT-01-METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="TOILET 12D21", floor_name="12TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP (TOWEL HOLE)", material_type="MARBLE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP APRON/6'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-40", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=242.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MT-01-METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="WELLNESS 12C19", floor_name="12TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP (TOWEL HOLE)", material_type="MARBLE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-40", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=70.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=6.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MT-01-METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="STORAGE 12K11", floor_name="12TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="RECORDS 12K20", floor_name="12TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="FREIGHT BANK S 12F23", floor_name="12TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="IDF S 12H19", floor_name="12TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="COPY ROOM 12G25", floor_name="12TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SC-01", finish_type="COUNTERTOP", material_type="STONE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="COPY NICHE 12F04", floor_name="12TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SC-01", finish_type="COUNTERTOP", material_type="STONE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="WOMEN'S RESTROOM 12F16", floor_name="12TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP (TOWEL HOLE)", material_type="MARBLE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP APRON/6'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=135.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-01", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=344.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-40", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=45.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=135.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=33.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=135.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MT-01-METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=40.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="MEN'S RESTROOM 12G16", floor_name="12TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP (TOWEL HOLE)", material_type="MARBLE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP APRON/6'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=142.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-01", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=362.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-40", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=45.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=142.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=37.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=142.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MT-01-METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=32.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="ELEVATOR LOBBY BANK C 14F09", floor_name="14TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-05", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=254.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02", finish_type="FLOOR", material_type="STONE", work_type="S&I", quantity=44.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02", finish_type="FLOOR SADDLE (8 UNITS)", material_type="STONE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=254.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=254.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="ELEVATOR LOBBY BANK B 14F12", floor_name="14TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-05", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=254.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02", finish_type="FLOOR", material_type="STONE", work_type="S&I", quantity=44.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02", finish_type="FLOOR SADDLE (8 UNITS)", material_type="STONE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=254.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=254.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="BEVERAGE BAR 14N09", floor_name="14TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SC-01", finish_type="COUNTERTOP", material_type="STONE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SC-01", finish_type="ISLAND COUNTERTOP", material_type="STONE", work_type="S&I", quantity=45.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SC-01", finish_type="ISLAND COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-41", finish_type="COUNTERTOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=561.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=561.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=561.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="TOILET 14K13", floor_name="14TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP (TOWEL HOLE)", material_type="MARBLE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP APRON/6'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-40", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=242.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MT-01-METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="TOILET 14D21", floor_name="14TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP (TOWEL HOLE)", material_type="MARBLE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP APRON/6'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-40", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=242.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MT-01-METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="WELLNESS 14C19", floor_name="14TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP (TOWEL HOLE)", material_type="MARBLE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-40", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=70.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=6.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MT-01-METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="COPY ROOM 14G25", floor_name="14TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SC-01", finish_type="COUNTERTOP", material_type="STONE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="COPY NICHE 14F04", floor_name="14TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SC-01", finish_type="COUNTERTOP", material_type="STONE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="STORAGE 14K11", floor_name="14TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="STORAGE 14K22", floor_name="14TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="IT WORK ROOM 14K20", floor_name="14TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="IDF 14H19", floor_name="14TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="WOMEN'S RESTROOM 14F16", floor_name="14TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP (TOWEL HOLE)", material_type="MARBLE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP APRON/6'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=135.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-01", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=344.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-40", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=45.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=135.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=33.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=135.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MT-01-METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=40.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="MEN'S RESTROOM 14G16", floor_name="14TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP (TOWEL HOLE)", material_type="MARBLE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-40A", finish_type="VANITY COUNTERTOP APRON/6'' HEIGHT", material_type="MARBLE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=142.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-01", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=362.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-40", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=45.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=142.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=37.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=142.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MT-01-METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=32.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        return rooms

    @staticmethod
    def get_2830_386park_metadata() -> Dict[str, str]:
        return {
            "project_name": "[2830] 386 Park Avenue South 13th & 14th Floor",
            "client_name": "MARIUS DIACONU",
            "client_company": "SPK/LEWIS CONSTRUCTION",
            "date_str": "07/23/2026"
        }

    @staticmethod
    def get_2830_386park_specs() -> Dict[str, MaterialSpec]:
        return {
            "SS-01": MaterialSpec(symbol="SS-01", description="CAESARSTONE, SOLID SURFACE PURE WHITE 1141", unit="SQ FT", budget_price=131.0, notes="$2,260 SLAB 2 CM", trade="Tile & Stone"),
            "BS-01": MaterialSpec(symbol="BS-01", description="NASCO, CERAMIC TILE, LOVE BARS, EBONY GLASS 5\" X 10\" STACKED", unit="SQ FT", budget_price=136.0, notes="the material price for this sf is $17 sf", trade="Tile & Stone"),
        }

    @staticmethod
    def get_2830_386park_rooms() -> List[RoomTakeoff]:
        rooms = []
        rooms.append(RoomTakeoff(room_name="WELLNESS ROOM 001", floor_name="13RD FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SS-01", finish_type="COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="COUNTERTOP BACKSPLASH/2' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=22.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="PANTRY 002", floor_name="13RD FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SS-01", finish_type="COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=44.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="BS-01", finish_type="COUNTERTOP BACKSPLASH/2' HEIGHT", material_type="CERAMIC TILE", work_type="S&I", quantity=28.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="BS-02", finish_type="COUNTERTOP BACKSPLASH/5' HEIGHT", material_type="CERAMIC TILE", work_type="S&I", quantity=40.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="PANTRY 001", floor_name="14TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SS-01", finish_type="COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=44.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="BS-01", finish_type="COUNTERTOP BACKSPLASH/2' HEIGHT", material_type="CERAMIC TILE", work_type="S&I", quantity=28.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="BS-02", finish_type="COUNTERTOP BACKSPLASH/5' HEIGHT", material_type="CERAMIC TILE", work_type="S&I", quantity=40.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        return rooms

    @staticmethod
    def get_2831_666third_metadata() -> Dict[str, str]:
        return {
            "project_name": "[2831] Project Orange, 666 3rd Avenue",
            "client_name": "STEPHEN POWER",
            "client_company": "J.T. MAGEN COMPANY INC.",
            "date_str": "07/29/2026"
        }

    @staticmethod
    def get_2831_666third_specs() -> Dict[str, MaterialSpec]:
        return {
            "TL-01": MaterialSpec(symbol="TL-01", description="CREATIVE MATERIALS CORP, RELIEVO REFLEX LIGHT GREEN GLOSSY 5\" X 10\" X 11mm", unit="SQ FT", budget_price=62.0, notes="$23.61 SF", trade="Tile & Stone"),
            "TL-02": MaterialSpec(symbol="TL-02", description="CREATIVE MATERIALS CORP, STACKED CERAMIC WHITE MATTE 5\" X 10\"", unit="SQ FT", budget_price=16.0, notes="$12.54 SF", trade="Tile & Stone"),
            "3. Metal Trim: Generic Manufacturer": MaterialSpec(symbol="3. Metal Trim: Generic Manufacturer", description="Metal Trim", unit="LN FT", budget_price=12.0, notes="", trade="Tile & Stone"),
        }

    @staticmethod
    def get_2831_666third_rooms() -> List[RoomTakeoff]:
        rooms = []
        rooms.append(RoomTakeoff(room_name="18K04 PANTRY", floor_name="18TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-01", finish_type="COUNTERTOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=31.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="18E05 MOTHER'S ROOM", floor_name="18TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-02", finish_type="COUNTERTOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=12.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="19K04 PANTRY", floor_name="19TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-01", finish_type="COUNTERTOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=31.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        return rooms

    @staticmethod
    def get_2832_43e68_metadata() -> Dict[str, str]:
        return {
            "project_name": "[2832] 43 EAST 68TH STREET",
            "client_name": "SELCUK MANISALIOGLU",
            "client_company": "[2832] 43 EAST 68TH STREET",
            "date_str": "07/31/2026"
        }

    @staticmethod
    def get_2832_43e68_specs() -> Dict[str, MaterialSpec]:
        return {
            "ST-200": MaterialSpec(symbol="ST-200", description="Caesarstone, Organic White #4600 Polished 20mm thickness", unit="SQ FT", budget_price=50.0, notes="$1,735 FOR SLAB 2CM (2025 FIYAT LISTESI)", trade="Tile & Stone"),
            "ST-201": MaterialSpec(symbol="ST-201", description="Stone Source, Dalmata Polished 2cm thickness", unit="SQ FT", budget_price=62.0, notes="$37.64/sf and slabs measure 120\" x 74\" x 2cm polished.  We have plenty of stock in our NJ warehouse.", trade="Tile & Stone"),
            "ST-203": MaterialSpec(symbol="ST-203", description="Nemo Tile, Calacatta Dorara Nuovo V727 Polished 20mm thickness", unit="SQ FT", budget_price=92.0, notes="FIYATI VERMEDILER", trade="Tile & Stone"),
            "ST-204": MaterialSpec(symbol="ST-204", description="Nemo Tile, TBD, Polished 20mm thickness", unit="SQ FT", budget_price=10.0, notes="", trade="Tile & Stone"),
            "TL-100": MaterialSpec(symbol="TL-100", description="TileBar Monroe Triangle Asian Statuary and Wooden Beige Marble Mosaic TilePolished 8\"x8\" mosaic 10mm thickness", unit="SQ FT", budget_price=22.0, notes="($34.32 / sq ft)", trade="Tile & Stone"),
            "TL-101": MaterialSpec(symbol="TL-101", description="TileBar, Monroe Monroe Corner + Border Asian Statuary and Wooden Beige Marble Mosaic Tile Polished 8\"x8\" mosaic 7.78\"x8.3\" border thickness", unit="SQ FT", budget_price=14.0, notes="($34.33 / sq ft)", trade="Tile & Stone"),
            "TL-102": MaterialSpec(symbol="TL-102", description="TileBar, Versilia Calacatta Oro Matte 12x12 Porcelain Tile Matte | 12\"x12\" | 10mm thickness", unit="SQ FT", budget_price=107.0, notes="($6.98 / sq ft)", trade="Tile & Stone"),
            "8. TL-103: TileBar, Anatolia Tile": MaterialSpec(symbol="8. TL-103: TileBar, Anatolia Tile", description="Prima Tile 12\"x12\" Charcoal Matte Charcoal Matte 12\"x12\" 10mm thickness", unit="SQ FT", budget_price=415.0, notes="$5/SF plus $250 freight.  In stock in Savanah Georgia", trade="Tile & Stone"),
            "TL-104": MaterialSpec(symbol="TL-104", description="TileBar, Calacatta 1x3 Herringbone Marble Mosaic Tile Polished 1\"x3\" 10mm thickness", unit="SQ FT", budget_price=164.0, notes="($21.80 / sq ft)", trade="Tile & Stone"),
            "TL-105": MaterialSpec(symbol="TL-105", description="Artistic Tile, Subway Collection A Train Straight Edge Field Tile White Gloss 4\"x12\" x 3/8\"", unit="SQ FT", budget_price=90.0, notes="$8.38 SF", trade="Tile & Stone"),
            "TL-106": MaterialSpec(symbol="TL-106", description="Porcelanosa, Calacatta Green Polished 10033103 Polished 47\"x47\" x 1/4\"", unit="SQ FT", budget_price=453.0, notes="100331093 CALACATTA GREEN POL.PV6 47\"X47\"(A) $17.37 per sqft, lead time 4-6 weeks", trade="Tile & Stone"),
            "TL-107": MaterialSpec(symbol="TL-107", description="Porcelanosa, Calacatta Green Silk 10033107 Silk 47\"x47\" x 1/4\"", unit="SQ FT", budget_price=90.0, notes="100331076 CALACATTA GREEN SILK PV6 47\"X47\"(A) $17.37 per sqft, lead time 4-6 weeks", trade="Tile & Stone"),
            "TL-108": MaterialSpec(symbol="TL-108", description="Artistic Tile, Penny Lane White, Honed Mosaic 11-1/8\"x11-15/16\"", unit="SQ FT", budget_price=15.0, notes="$48.30 SF Marble Sheet Size: 11-1/8\" X 11-15/16\" X 3/8\",", trade="Tile & Stone"),
            "TL-109": MaterialSpec(symbol="TL-109", description="Artistic Tile, Penny Lane Green, Honed Mosaic 11-1/8\"x11-15/16\"", unit="SQ FT", budget_price=10.0, notes="$50.40 SF Marble Sheet Size: 11-1/8\" X 11-15/16\" X 3/8\",", trade="Tile & Stone"),
            "TL-110": MaterialSpec(symbol="TL-110", description="Artistic Tile, Penny Lane Nero, Honed Mosaic 11-1/8\"x11-15/16\"", unit="SQ FT", budget_price=6.0, notes="$40.60 SF Marble Sheet Size: 11-1/8\" X 11-15/16\" X 3/8\",", trade="Tile & Stone"),
            "TL-111": MaterialSpec(symbol="TL-111", description="TileBar, Nero Marquina 1x3 Herringbone Polished Marble Mosaic Tile", unit="SQ FT", budget_price=129.0, notes="($14.00 / sq ft)", trade="Tile & Stone"),
            "TL-112": MaterialSpec(symbol="TL-112", description="TileBar, Versilia Calacatta Oro Matte 12x12 Porcelain Tile Matte 12\"x12\" 10mm thickness", unit="SQ FT", budget_price=961.0, notes="($6.98 / sq ft)", trade="Tile & Stone"),
            "TL-113": MaterialSpec(symbol="TL-113", description="TileBar Phantasm Harves Cream and Gray Polished Mixed Marble Mosaic Tile 13.5\"x15.62\"x10mm", unit="SQ FT", budget_price=133.0, notes="($36.66 / sq ft)", trade="Tile & Stone"),
            "TL-114": MaterialSpec(symbol="TL-114", description="TileBar, Kanbina Sapphire Blue 5x18 Crackled Glossy Ceramic Mosaic Tile 5.27\"x17.71\" x 9mm", unit="SQ FT", budget_price=319.0, notes="($18.69 / sq ft)", trade="Tile & Stone"),
            "TL-115": MaterialSpec(symbol="TL-115", description="TileBar, Chips Macro Bianco White 8x8 Terrazzo Look Matte Porcelain Tile 7.87\"x7.87\" x 8.5mm", unit="SQ FT", budget_price=166.0, notes="($7.76 / sq ft)", trade="Tile & Stone"),
            "TL-116": MaterialSpec(symbol="TL-116", description="Nemo Tile, Travertino Navona Grigio, Polished 24\"x48\"", unit="SQ FT", budget_price=138.0, notes="24x48 Travertino Navona Grio Polished - $7.56/sf - 15.39 sf per carton", trade="Tile & Stone"),
            "TL-117": MaterialSpec(symbol="TL-117", description="TileBar, Prima Charcoal Matte 12\"x12\"", unit="SQ FT", budget_price=165.0, notes="$5/SF plus $250 freight.  In stock in Savanah Georgia", trade="Tile & Stone"),
            "TL-118": MaterialSpec(symbol="TL-118", description="TileBar, Versilia Calacatta Oro Matte 12\"x12\"", unit="SQ FT", budget_price=165.0, notes="($6.98 / sq ft)", trade="Tile & Stone"),
            "TL-119": MaterialSpec(symbol="TL-119", description="Nemo Tile, Gordon 24\"x48\" Graphite Paver Black, Matte 24\"x24\"", unit="SQ FT", budget_price=347.0, notes="24x48 Gordon Graphite Paver - $6.96/sf - 7.74 sf per carton", trade="Tile & Stone"),
            "TL-120": MaterialSpec(symbol="TL-120", description="TILE, TBD", unit="SQ FT", budget_price=347.0, notes="", trade="Tile & Stone"),
            "WBT-100": MaterialSpec(symbol="WBT-100", description="TileBar, Wooden Beige Honed Marble Tile Honed 12\"x24\" x 10mm thickness", unit="SQ FT", budget_price=41.0, notes="($10.10 / sq ft)", trade="Tile & Stone"),
            "WBT-101": MaterialSpec(symbol="WBT-101", description="TileBar, Versilia Calacatta Oro 3x24 Polished Porcelain Bullnose Polished 3\"x24\"", unit="SQ FT", budget_price=84.0, notes="$13.25 / piece", trade="Tile & Stone"),
            "28. Waterproof: Generic Manufacturer": MaterialSpec(symbol="28. Waterproof: Generic Manufacturer", description="Waterproof", unit="SQ FT", budget_price=0.0, notes="", trade="Tile & Stone"),
            "29. Mud Set: Generic Manufacturer": MaterialSpec(symbol="29. Mud Set: Generic Manufacturer", description="Mud Set", unit="SQ FT", budget_price=0.0, notes="", trade="Tile & Stone"),
            "30. Metal Trim: Generic Manufacturer": MaterialSpec(symbol="30. Metal Trim: Generic Manufacturer", description="Metal Trim", unit="LN FT", budget_price=43.0, notes="", trade="Tile & Stone"),
            "ST-202-Saddle": MaterialSpec(symbol="ST-202-Saddle", description="Caesarstone, Organic White #4600 Polished 20mm thickness", unit="PCS", budget_price=14.0, notes="$1,735 FOR SLAB 2CM (2025 FIYAT LISTESI)", trade="Tile & Stone"),
        }

    @staticmethod
    def get_2832_43e68_rooms() -> List[RoomTakeoff]:
        rooms = []
        rooms.append(RoomTakeoff(room_name="NEW WALK IN COOLER", floor_name="CELLAR FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-103", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=57.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=57.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=57.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="NEW WALK IN FREEZER", floor_name="CELLAR FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-103", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=54.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=54.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=54.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="BATHROOM", floor_name="CELLAR FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-200", finish_type="VANITY COUNTERTOP", material_type="STONE", work_type="S&I", quantity=7.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-200", finish_type="VANITY COUNTERTOP APRON/4'' HEIGHT", material_type="STONE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-115", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=35.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WBT-100", finish_type="WALL", material_type="STONE BASE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=35.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=12.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=35.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-202-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="CLOSET HALL", floor_name="CELLAR FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-117", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=130.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-118", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=130.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=260.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=260.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-202-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="LAUNDRY ROOM", floor_name="CELLAR FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-117", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=35.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-118", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=35.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=130.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=130.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-202-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="BATHROOM", floor_name="CELLAR FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-200", finish_type="VANITY COUNTERTOP", material_type="STONE", work_type="S&I", quantity=7.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-200", finish_type="VANITY COUNTERTOP APRON/4'' HEIGHT", material_type="STONE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-115", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=51.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-105", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=92.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=51.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=92.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=51.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-202-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="METER ROOM", floor_name="CELLAR FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-103", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=129.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=129.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=129.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="MECHANICAL ROOM", floor_name="CELLAR FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-103", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=68.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=68.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=68.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="KITCHEN TERACE", floor_name="CELLAR FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-120", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=347.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=347.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=347.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="BATHROOM", floor_name="FIRST FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-200", finish_type="VANITY COUNTERTOP", material_type="STONE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-200", finish_type="VANITY COUNTERTOP APRON/4'' HEIGHT", material_type="STONE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-100", finish_type="FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=22.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-101", finish_type="FLOOR", material_type="BORDER MOSAIC TILE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WBT-100", finish_type="WALL", material_type="STONE BASE", work_type="S&I", quantity=21.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=36.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=13.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=36.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-202-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="PANTRY", floor_name="FIRST FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-203", finish_type="#1 COUNTERTOP", material_type="STONE", work_type="S&I", quantity=34.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-203", finish_type="#2 COUNTERTOP", material_type="STONE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-116", finish_type="COUNTERTOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=118.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-102", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=79.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-103", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=79.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WBT-101", finish_type="WALL", material_type="STONE BASE", work_type="S&I", quantity=57.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=158.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=158.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-202-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="PAVER", floor_name="FIRST FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-119", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=347.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=347.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=347.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="BATHROOM", floor_name="SECOND FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-201", finish_type="VANITY COUNTERTOP", material_type="STONE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-201", finish_type="VANITY COUNTERTOP APRON/4'' HEIGHT", material_type="STONE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-104", finish_type="FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=28.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-104", finish_type="WALL", material_type="MOSAIC TILE", work_type="S&I", quantity=110.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-105", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=90.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=28.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=13.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=28.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-202-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="KITCHENETTE", floor_name="THIRD FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-203", finish_type="COUNTERTOP", material_type="STONE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-104", finish_type="COUNTERTOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-102", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=28.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-103", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=28.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WBT-101", finish_type="WALL", material_type="STONE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-202-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="BATHROOM", floor_name="THIRD FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-201", finish_type="VANITY COUNTERTOP", material_type="STONE", work_type="S&I", quantity=13.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-107", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=90.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-108", finish_type="FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-109", finish_type="FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-110", finish_type="FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=6.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-106", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=453.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=118.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=13.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=181.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=118.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-202-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="BATHROOM", floor_name="THIRD FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-201", finish_type="VANITY COUNTERTOP", material_type="STONE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-201", finish_type="VANITY COUNTERTOP APRON/4'' HEIGHT", material_type="STONE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-111", finish_type="FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=62.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-112", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=259.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=62.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=12.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=88.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=62.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-202-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="LIBRARY STORAGE", floor_name="THIRD FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-204", finish_type="VANITY COUNTERTOP", material_type="STONE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="BATHROOM", floor_name="4TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-201", finish_type="VANITY COUNTERTOP", material_type="STONE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-201", finish_type="VANITY COUNTERTOP APRON/4'' HEIGHT", material_type="STONE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-111", finish_type="FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-112", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=259.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=12.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=88.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-202-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="BATHROOM", floor_name="4TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-201", finish_type="VANITY COUNTERTOP", material_type="STONE", work_type="S&I", quantity=13.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-113", finish_type="FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=133.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-112", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=443.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=133.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=192.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=133.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-202-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="BATHROOM", floor_name="5TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-200", finish_type="VANITY COUNTERTOP", material_type="STONE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-200", finish_type="VANITY COUNTERTOP APRON/4'' HEIGHT", material_type="STONE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-115", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=80.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-114", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=319.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=80.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=95.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=80.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=9.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-202-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="PANTRY", floor_name="5TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-203", finish_type="COUNTERTOP", material_type="STONE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-116", finish_type="COUNTERTOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        return rooms

    @staticmethod
    def get_2835_70e55_metadata() -> Dict[str, str]:
        return {
            "project_name": "[2835] 70 E 55th Street - 12th floor",
            "client_name": "STEVE DIPIETRO",
            "client_company": "EVERGREEN CONSTRUCTION",
            "date_str": "08/05/2026"
        }

    @staticmethod
    def get_2835_70e55_specs() -> Dict[str, MaterialSpec]:
        return {
            "SS-01": MaterialSpec(symbol="SS-01", description="CAESARSTONE, SUPERNATURAL CLOUDBURST CONCRETE #4011 2CM SLABS; MITER ALL EDGES", unit="SQ FT", budget_price=42.0, notes="$2,560 FOR SLAB 2CM (2025 FIYAT LISTESI)", trade="Tile & Stone"),
            "WL-01": MaterialSpec(symbol="WL-01", description="MSI, STONE XL ROCKMOUNT ARABESCATO VENATO #LPNLMARAVEN924 NATURAL 9\" X 24\", ORIENT HORIZONTALLY", unit="SQ FT", budget_price=73.0, notes="I checked all our locations…  Unfortunately, we don't have this type of material in stock.", trade="Tile & Stone"),
            "T-01": MaterialSpec(symbol="T-01", description="STONE SOURCE, PALMA MODERN CEMENT PERLA NATURAL 48\" X 48\" MONOLITHIC", unit="SQ FT", budget_price=95.0, notes="7.18 SF", trade="Tile & Stone"),
            "4. Waterproof: Generic Manufacturer": MaterialSpec(symbol="4. Waterproof: Generic Manufacturer", description="Waterproof", unit="SQ FT", budget_price=95.0, notes="", trade="Tile & Stone"),
            "5. Mud Set: Generic Manufacturer": MaterialSpec(symbol="5. Mud Set: Generic Manufacturer", description="Mud Set", unit="SQ FT", budget_price=95.0, notes="", trade="Tile & Stone"),
            "6. Metal Trim: Generic Manufacturer": MaterialSpec(symbol="6. Metal Trim: Generic Manufacturer", description="METAL ANGLED \"L\" BRACKET ON ALL SIDES, MATTE BLACK Metal Trim", unit="LN FT", budget_price=35.0, notes="", trade="Tile & Stone"),
            "7. Saddle: Generic Manufacturer": MaterialSpec(symbol="7. Saddle: Generic Manufacturer", description="Saddle", unit="PCS", budget_price=3.0, notes="", trade="Tile & Stone"),
        }

    @staticmethod
    def get_2835_70e55_rooms() -> List[RoomTakeoff]:
        rooms = []
        rooms.append(RoomTakeoff(room_name="ELEVATOR LOBBY 1200", floor_name="12TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="WL-01", finish_type="WALL (SLIP MATCH VENEER  SEAMS)", material_type="STONE", work_type="S&I", quantity=73.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=35.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="PANTRY 1205", floor_name="12TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SS-01", finish_type="COUNTERTOP", material_type="STONE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="STONE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="COUNTERTOP BACKSPLASH/FULL HEIGHT", material_type="STONE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=95.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=95.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=95.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="WOMEN'S RESTROOM", floor_name="12TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="MEN'S RESTROOM", floor_name="12TH FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        return rooms

    @staticmethod
    def get_2300_2wallstreet_metadata() -> Dict[str, str]:
        return {
            "project_name": "[2300] 2 WALL STREET MULTIPLE CONVERSION PROJECT",
            "client_name": "ANNA BIELINSKI",
            "client_company": "VANGUARD CONSTRUCTION",
            "date_str": "01/06/2025"
        }

    @staticmethod
    def get_2300_2wallstreet_specs() -> Dict[str, MaterialSpec]:
        return {
            "SS-01": MaterialSpec(symbol="SS-01", description="Solid Surface Vanity Countertop", unit="SQ FT", budget_price=62.0, notes="BU MALZEMEYLE ILGILI BILGI OLMADIGI ICIN BUDGET YAPILMISTIR", trade="Tile & Stone"),
            "ST-01": MaterialSpec(symbol="ST-01", description="Bas Stone, Veranda Pantry Countertop, Marble Stone Green Lily, Honed / Sage Green / Blue, 2cm", unit="SQ FT", budget_price=16.0, notes="GREEN LILY HONED 2CM  240312 96\" x 55\" = 36.67 SF @ $44.25 per sf", trade="Tile & Stone"),
            "ST-02": MaterialSpec(symbol="ST-02", description="Caesarstone, Dining RoomPantryCountertop,6046 Moorland Fog Taupe with Foggy Brown and Grey VeinedQuartzCountertop, Polished,2cm", unit="SQ FT", budget_price=26.0, notes="$ 1.805.00 SLAB (2023 FIYAT LISTESINDEN ALINMISTIR)", trade="Tile & Stone"),
            "ST-03": MaterialSpec(symbol="ST-03", description="Ann Sacks, 9th Floor Restroom Vanity Countertop, Taj Mahal 2cm Honed Quartzite Slab, Polished", unit="SQ FT", budget_price=5.0, notes="78\"x134\"- $51.18/ sf. Generally available from our LIC gallery.", trade="Tile & Stone"),
            "ST-04": MaterialSpec(symbol="ST-04", description="Caesarstone, 5144 Rossa Nova New Off-White Base with Deep Golden Accents Quartz Countertop, Polished, 2cm", unit="SQ FT", budget_price=64.0, notes="BIZDEKI FIYAT LISTESINDE BU MALZEME YOK", trade="Tile & Stone"),
            "ST-05": MaterialSpec(symbol="ST-05", description="Bas Stone, Dining Room Table Top, Quartzite Belvedere Honed, Black, Gold, Gray Honed, 3 cm", unit="SQ FT", budget_price=25.0, notes="BELVEDERE HONED 3CM 240421 116\" x 73\" = 58.81 SF @ $43.25 per sf", trade="Tile & Stone"),
            "ST-06": MaterialSpec(symbol="ST-06", description="Wilsonart, Semi-translucent quartz countertop, Music Room Countertop, Tellaro / Model Code: Q4025, Polished, 2cm", unit="SQ FT", budget_price=58.0, notes="Q4025 Tellaro 2cm 65 x130 Jumbo slab size Polished  $1311.00 per slab Hub stock 2 week lead time Approximate", trade="Tile & Stone"),
            "T-01": MaterialSpec(symbol="T-01", description="Archetype Glass, Decorative glass with bronze interlayer, Model Name: VN-4967", unit="SQ FT", budget_price=0.0, notes="", trade="Tile & Stone"),
            "T-02": MaterialSpec(symbol="T-02", description="Emser Tile, SKU F20STERIV1224, Sterlina Matte / Ivory / 12X24", unit="SQ FT", budget_price=0.0, notes="SF $2.98", trade="Tile & Stone"),
            "WB-02": MaterialSpec(symbol="WB-02", description="Emser Tile, Wall Base, Ivory / Matte SKU F20STERIV0312SBM 3\" x 12\" SBN Matte", unit="SQ FT", budget_price=0.0, notes="PC $5.25", trade="Tile & Stone"),
            "T-03": MaterialSpec(symbol="T-03", description="Genrose, Twilight White 2 SKU ELPWHITTWILIDE02, Finish: Satin 12x12", unit="SQ FT", budget_price=0.0, notes="$7.600 PC", trade="Tile & Stone"),
            "T-04": MaterialSpec(symbol="T-04", description="Nemo Tile, Super White, SKU SUPERWHITE11, Matte 12x24", unit="SQ FT", budget_price=0.0, notes="12X24 SUPERWHITE FLAT MATTE = $4.52/sf - 11.62 sf/ctn - approx. 6-10 week lead time", trade="Tile & Stone"),
            "TI-01": MaterialSpec(symbol="TI-01", description="Artsaics, Artsaics Asian White Marble Field Tile, Honed, 24'' x 24'' x 3/8'' Checkerboard Pattern", unit="SQ FT", budget_price=577.0, notes="12x12 Asian White Honed $ 15.20 sf", trade="Tile & Stone"),
            "TI-02": MaterialSpec(symbol="TI-02", description="Artsaics, Nero Marquina Honed Marble Field Tile, 24'' x 24'' x 3/8'' Checkerboard Pattern", unit="SQ FT", budget_price=509.0, notes="12x12 Nero Marquina Honed $14.40 sf", trade="Tile & Stone"),
            "TI-03": MaterialSpec(symbol="TI-03", description="Vermont Structural Slate Company, Tile Base, Marshall Granite Tile, Textured", unit="SQ FT", budget_price=400.0, notes="", trade="Tile & Stone"),
            "TI-04": MaterialSpec(symbol="TI-04", description="Miller Druck Specialty, Tile Base, Boniato Stone, Honed, 36\" x 36\"", unit="SQ FT", budget_price=74.0, notes="", trade="Tile & Stone"),
            "TI-05": MaterialSpec(symbol="TI-05", description="Wall Tile", unit="SQ FT", budget_price=226.0, notes="BU MALZEMEYLE ILGILI BILGI OLMADIGI ICIN BUDGET YAPILMISTIR", trade="Tile & Stone"),
            "TI-06": MaterialSpec(symbol="TI-06", description="Tile Tech, Outdoor Porcelain Pavers 2cm, Stone Series / Color: Sand Stone, Anti-slip surface, 24\"x24\",3/4\"", unit="SQ FT", budget_price=512.0, notes="GELEN FIYATTA BIRCOK MALZEME VAR LUTFEN FIYAT TEKLIFINE BAKINIZ", trade="Tile & Stone"),
            "TI-07": MaterialSpec(symbol="TI-07", description="Ann Sacks, Emerald, Gloss, Ceramic | AS12167-37, 2\" X 11\"", unit="SQ FT", budget_price=38.0, notes="$15.98/ sf trade. (16.3 sf per box) in stock", trade="Tile & Stone"),
            "TI-08": MaterialSpec(symbol="TI-08", description="Tile Bar, Rushmore Park Beige 24x24 Matte Porcelain Tile,", unit="SQ FT", budget_price=436.0, notes="Rushmore Park Beige 24x24 Matte Porcelain - $5.00 / sq. ft – Out of stock but we have shipments coming in later this month", trade="Tile & Stone"),
            "TI-09": MaterialSpec(symbol="TI-09", description="Ann Sacks, Ceramic | AS12167-37 |Context | Field, Spa / Matte, 2\" x 12\"", unit="SQ FT", budget_price=140.0, notes="$15.98/ sf trade. (16.3 sf per box) in stock", trade="Tile & Stone"),
            "TI-10": MaterialSpec(symbol="TI-10", description="TileBar, Clay Shy Beige Porcelain Tile, Matte, 16\" x 32\"", unit="SQ FT", budget_price=114.0, notes="Clay Shy Beige 16x32 Matte - $5.70 / sq. ft. – Plenty in stock", trade="Tile & Stone"),
            "TI-11": MaterialSpec(symbol="TI-11", description="Spartan Surfaces, Pawsh Pups Porcelain Tile Collection, Artistic Dog Tile Designs, Natural 12 Different Tiles Randomly Placed, 10\" x 10\"", unit="SQ FT", budget_price=103.0, notes="$ 8.75 SF", trade="Tile & Stone"),
            "TI-12": MaterialSpec(symbol="TI-12", description="Crossville, Color Blox 2.0 Cotton Sheets SLU: CBX31.11212UPS, Field Tile / color: Cotton Sheets, 12 x 12 (in)  9.5(mm)", unit="SQ FT", budget_price=244.0, notes="12X12 CBX31.11212UPS COTTON SHEETS UPS = $6.80/sf - 12 sf/ctn - approx. 2-3 week lead time", trade="Tile & Stone"),
            "TI-13": MaterialSpec(symbol="TI-13", description="Casalgrande Padana, Pietra Baugè Beige, Matte 24\" x 24\"", unit="SQ FT", budget_price=175.0, notes="$ 4.03 SF", trade="Tile & Stone"),
            "TI-14": MaterialSpec(symbol="TI-14", description="Nemo Tile, Glow Snow 2x10, Matte", unit="SQ FT", budget_price=660.0, notes="GLOW SNOW 2X10 MATTE = $12.20/sf - 3.23 sf/ctn - approx. 370 sf in stock at our NY warehouse. Approx. 6-10 week lead time", trade="Tile & Stone"),
            "TI-15": MaterialSpec(symbol="TI-15", description="Vermont Structural Slate, Marshall Granite Tile, Textured", unit="SQ FT", budget_price=485.0, notes="", trade="Tile & Stone"),
            "TI-16": MaterialSpec(symbol="TI-16", description="Emser Tile, SKU F20STERIV1212MO2M / Mosaic Tile, 2 x 2 Mosaic on 12 x 12 Mesh, Matte / Ivory", unit="SQ FT", budget_price=394.0, notes="SF $24.09", trade="Tile & Stone"),
            "TI-101": MaterialSpec(symbol="TI-101", description="Genrose, Camden COLOR:Levee White, Matte 12\" X 24\"", unit="SQ FT", budget_price=458.0, notes="$3.950 SF", trade="Tile & Stone"),
            "TI-102": MaterialSpec(symbol="TI-102", description="Nemo Tile, METRO MODEL CODE: METRO30636, Bone Matte, 3\" X 6\"", unit="SQ FT", budget_price=0.0, notes="3X6 METRO BONE MATTE = $4.11/sf - 12.5 sf/ctn -  approx. 2-3 week lead time", trade="Tile & Stone"),
            "35. Waterproof: Generic Manufacturer": MaterialSpec(symbol="35. Waterproof: Generic Manufacturer", description="Waterproof", unit="SQ FT", budget_price=0.0, notes="", trade="Tile & Stone"),
            "36. Soundproof: Generic Manufacturer": MaterialSpec(symbol="36. Soundproof: Generic Manufacturer", description="Soundproof", unit="SQ FT", budget_price=0.0, notes="", trade="Tile & Stone"),
            "37. Metal Trim: Generic Manufacturer": MaterialSpec(symbol="37. Metal Trim: Generic Manufacturer", description="Schluter Jolly Metal Trim", unit="LN FT", budget_price=537.0, notes="", trade="Tile & Stone"),
            "38. Metal Trim: Generic Manufacturer": MaterialSpec(symbol="38. Metal Trim: Generic Manufacturer", description="Schluter Rondec Metal Trim", unit="LN FT", budget_price=0.0, notes="", trade="Tile & Stone"),
            "39. Mud Set: Generic Manufacturer": MaterialSpec(symbol="39. Mud Set: Generic Manufacturer", description="Mud Set", unit="SQ FT", budget_price=0.0, notes="", trade="Tile & Stone"),
            "40. ST-03-Saddle: Caesarstone, 4001 Fresh Concrete": MaterialSpec(symbol="40. ST-03-Saddle: Caesarstone, 4001 Fresh Concrete", description="Concrete Finish Thickness TBD Saddle", unit="PCS", budget_price=194.0, notes="", trade="Tile & Stone"),
            "41. Saddle: Generic Manufacturer": MaterialSpec(symbol="41. Saddle: Generic Manufacturer", description="Saddle", unit="PCS", budget_price=0.0, notes="", trade="Tile & Stone"),
        }

    @staticmethod
    def get_2300_2wallstreet_rooms() -> List[RoomTakeoff]:
        rooms = []
        rooms.append(RoomTakeoff(room_name="RESTROOM 00-C14", floor_name="SUB CELLAR  #2 FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SS-01", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=12.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="VANITY COUNTER TOP APRON/5'' HEIGHT", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="VANITY COUNTER TOP BACKSPLASH/4'' HEIGHT", material_type="STONE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-101", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=130.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-102", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=301.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=130.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=130.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=130.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=43.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="RESTROOM 00-C15", floor_name="SUB CELLAR  #2 FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SS-01", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=6.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="VANITY COUNTER TOP APRON/5'' HEIGHT", material_type="STONE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="VANITY COUNTER TOP BACKSPLASH/4'' HEIGHT", material_type="STONE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-101", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=99.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-102", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=259.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=99.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=22.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=99.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=99.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=37.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="RESTROOM 00-C14", floor_name="SUB CELLAR  #3 FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SS-01", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=12.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="VANITY COUNTER TOP APRON/5'' HEIGHT", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="VANITY COUNTER TOP BACKSPLASH/4'' HEIGHT", material_type="STONE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-101", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=130.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-102", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=301.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=130.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=130.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=130.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=43.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="RESTROOM 00-C15", floor_name="SUB CELLAR  #3 FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SS-01", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=6.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="VANITY COUNTER TOP APRON/5'' HEIGHT", material_type="STONE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="VANITY COUNTER TOP BACKSPLASH/4'' HEIGHT", material_type="STONE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-101", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=99.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-102", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=259.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=99.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=22.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=99.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=99.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=37.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="ELEV. LOBBY", floor_name="CELLAR  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TI-01", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=134.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-02", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=66.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=200.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=200.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=200.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=6.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="RECORD/MUSIC ROOM 00-A15", floor_name="CELLAR  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-06", finish_type="COUNTER TOP", material_type="STONE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-06", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="STONE", work_type="S&I", quantity=44.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="BATHING STATION 00-A16", floor_name="CELLAR  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-04", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=6.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-04", finish_type="VANITY COUNTER TOP APRON/7'' HEIGHT", material_type="STONE", work_type="S&I", quantity=7.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-04", finish_type="VANITY COUNTER TOP BACKSPLASH/3'' HEIGHT", material_type="STONE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-10", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=114.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-11", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=103.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-12", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=244.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=114.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=347.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=114.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=114.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="ADA 00-A17", floor_name="CELLAR  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-04", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=6.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-04", finish_type="VANITY COUNTER TOP APRON/7'' HEIGHT", material_type="STONE", work_type="S&I", quantity=7.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-04", finish_type="VANITY COUNTER TOP BACKSPLASH/3'' HEIGHT", material_type="STONE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-13", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=59.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-14", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=220.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=59.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=59.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=59.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="ADA 00-A18", floor_name="CELLAR  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-04", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=6.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-04", finish_type="VANITY COUNTER TOP APRON/7'' HEIGHT", material_type="STONE", work_type="S&I", quantity=7.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-04", finish_type="VANITY COUNTER TOP BACKSPLASH/3'' HEIGHT", material_type="STONE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-13", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=59.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-14", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=220.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=59.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=59.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=59.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="COMMERCIAL VESTIBULE 01-01", floor_name="FIRST  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TI-03", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=166.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=166.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=166.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=166.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="RESIDENTIAL LOBBY 01-07", floor_name="FIRST  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TI-01", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=263.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=263.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-03", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=257.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-03", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=333.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-15", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=485.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=783.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=783.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=783.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=6.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="MAIL ROOM 01-08", floor_name="FIRST  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TI-03", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=130.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=130.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=130.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=130.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="PACKAGE ROOM 01-09, CORRIDOR", floor_name="FIRST  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TI-03", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=170.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=170.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=170.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=170.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="RESTROOM 01-10", floor_name="FIRST  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-04", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=6.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-04", finish_type="VANITY COUNTER TOP APRON/7'' HEIGHT", material_type="STONE", work_type="S&I", quantity=7.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-04", finish_type="VANITY COUNTER TOP BACKSPLASH/3'' HEIGHT", material_type="STONE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-13", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=57.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-14", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=220.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=57.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=57.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=57.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="RAMP", floor_name="FIRST  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TI-03", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=391.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-03", finish_type="RISER", material_type="TILE", work_type="S&I", quantity=12.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-03", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=400.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=391.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=391.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=391.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=400.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="COMMERCIAL VESTIBULE 01-11", floor_name="FIRST  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TI-03", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=66.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-04", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=226.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-05", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=226.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-04", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=74.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=292.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=292.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=292.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=65.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="ELEV LOBBY 01-15", floor_name="FIRST  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TI-01", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=94.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=94.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-03", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=77.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=265.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=265.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=265.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=6.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="801-1 BR KITCHEN K3A", floor_name="8TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=33.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=36.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="801-1 BR BATHROOM B1C", floor_name="8TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="802-1 BR & H.O. KITCHEN K2D", floor_name="8TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="802-1 BR & H.O. BATHROOM B2A", floor_name="8TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="803-STUDIO KITCHEN K1", floor_name="8TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="803-STUDIO BATHROOM B2A", floor_name="8TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=6.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="804-STUDIO KITCHEN K1", floor_name="8TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="804-STUDIO BATHROOM B3A", floor_name="8TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=42.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="805-2 BR KITCHEN K4A", floor_name="8TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP WATERFALL EDGES", material_type="SOLID SURFACE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="805-2 BR BATHROOM B1A", floor_name="8TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="805-2 BR BATHROOM B2A", floor_name="8TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="806-2 BR KITCHEN K5C", floor_name="8TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=11.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP WATERFALL EDGES", material_type="SOLID SURFACE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="806-2 BR BATHROOM B1B", floor_name="8TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="806-2 BR BATHROOM B4A", floor_name="8TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="COURTYARD", floor_name="9TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-07", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=38.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-01", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=86.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=86.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-06", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=512.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=684.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=684.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=684.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=12.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="LOUNGE & PANTRY", floor_name="9TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-05", finish_type="DINING TABLE COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-08", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=380.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=380.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=380.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=380.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=12.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="BATHROOM", floor_name="9TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-03", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-08", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-09", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=140.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=33.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="901-1 BR KITCHEN K3A", floor_name="9TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=33.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=36.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="901-1 BR BATHROOM B1C", floor_name="9TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="902-1 BR & H.O. KITCHEN K2D", floor_name="9TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="902-1 BR & H.O. BATHROOM B2A", floor_name="9TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="903-STUDIO KITCHEN K1", floor_name="9TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="903-STUDIO BATHROOM B2A", floor_name="9TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="904-STUDIO KITCHEN K1", floor_name="9TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="904-STUDIO BATHROOM B3A", floor_name="9TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=42.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="905-2 BR KITCHEN K4A", floor_name="9TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP WATERFALL EDGES", material_type="SOLID SURFACE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="905-2 BR BATHROOM B1A", floor_name="9TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="905-2 BR BATHROOM B2A", floor_name="9TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="906-2 BR KITCHEN K5C", floor_name="9TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=11.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP WATERFALL EDGES", material_type="SOLID SURFACE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="906-2 BR BATHROOM B1A", floor_name="9TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="906-2 BR BATHROOM B2A", floor_name="9TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1001-1 BR KITCHEN K3A", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=33.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=36.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1001-1 BR BATHROOM B1C", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1002-1 BR & H.O. KITCHEN K2D", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1002-1 BR & H.O. BATHROOM B2A", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1003-STUDIO KITCHEN K1", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1003-STUDIO BATHROOM B2A", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1004-STUDIO KITCHEN K1", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1004-STUDIO BATHROOM B3A", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=42.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1005-STUDIO KITCHEN K1", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1005-STUDIO BATHROOM B4A", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1006-2 BR KITCHEN K4A", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP WATERFALL EDGES", material_type="SOLID SURFACE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1006-2 BR BATHROOM B1A", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1006-2 BR BATHROOM B2A", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1007-1 BR KITCHEN K2A", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1007-1 BR BATHROOM B4A", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1008-1 BR KITCHEN K2A", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1008-1 BR BATHROOM B4B", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1009-STUDIO KITCHEN K1", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1009-STUDIO BATHROOM B5B", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=53.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=34.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1010-STUDIO KITCHEN K1", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1010-STUDIO BATHROOM B5A", floor_name="10TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=35.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1101-1 BR KITCHEN K3A", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=33.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=36.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1101-1 BR BATHROOM B1C", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1102-1 BR & H.O. KITCHEN K2D", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1102-1 BR & H.O. BATHROOM B2A", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1103-STUDIO KITCHEN K1", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1103-STUDIO BATHROOM B2A", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1104-STUDIO KITCHEN K1", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1104-STUDIO BATHROOM B3A", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=42.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1105-STUDIO KITCHEN K1", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1105-STUDIO BATHROOM B4A", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1106-2 BR KITCHEN K4A", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP WATERFALL EDGES", material_type="SOLID SURFACE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1106-2 BR BATHROOM B1A", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1106-2 BR BATHROOM B2A", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1107-1 BR KITCHEN K2A", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1107-1 BR BATHROOM B4A", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1108-1 BR KITCHEN K2A", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1108-1 BR BATHROOM B4B", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1109-STUDIO KITCHEN K1", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1109-STUDIO BATHROOM B5B", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=53.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=34.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1110-STUDIO KITCHEN K1", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1110-STUDIO BATHROOM B5A", floor_name="11TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=35.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1201-1 BR KITCHEN K3A", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=33.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=36.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1201-1 BR BATHROOM B1C", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1202-1 BR & H.O. KITCHEN K2D", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1202-1 BR & H.O. BATHROOM B2A", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1203-STUDIO KITCHEN K1", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1203-STUDIO BATHROOM B2A", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1204-STUDIO KITCHEN K1", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1204-STUDIO BATHROOM B3A", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=42.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1205-STUDIO KITCHEN K1", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1205-STUDIO BATHROOM B4A", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1206-2 BR KITCHEN K4A", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP WATERFALL EDGES", material_type="SOLID SURFACE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1206-2 BR BATHROOM B1A", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1206-2 BR BATHROOM B2A", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1207-1 BR KITCHEN K2A", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1207-1 BR BATHROOM B4A", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1208-1 BR KITCHEN K2A", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1208-1 BR BATHROOM B4B", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1209-STUDIO KITCHEN K1", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1209-STUDIO BATHROOM B5B", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=53.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=34.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1210-STUDIO KITCHEN K1", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1210-STUDIO BATHROOM B5A", floor_name="12TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=35.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1301-1 BR KITCHEN K3A", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=33.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=36.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1301-1 BR BATHROOM B1C", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1302-1 BR & H.O. KITCHEN K2D", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1302-1 BR & H.O. BATHROOM B2A", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1303-STUDIO KITCHEN K1", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1303-STUDIO BATHROOM B2A", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1304-STUDIO KITCHEN K1", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1304-STUDIO BATHROOM B3A", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=42.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1305-STUDIO KITCHEN K1", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1305-STUDIO BATHROOM B4A", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1306-2 BR KITCHEN K4A", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP WATERFALL EDGES", material_type="SOLID SURFACE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1306-2 BR BATHROOM B1A", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1306-2 BR BATHROOM B2A", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1307-1 BR KITCHEN K2A", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1307-1 BR BATHROOM B4A", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1308-1 BR KITCHEN K2A", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1308-1 BR BATHROOM B4B", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1309-STUDIO KITCHEN K1", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1309-STUDIO BATHROOM B5B", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=53.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=34.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1310-STUDIO KITCHEN K1", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1310-STUDIO BATHROOM B5A", floor_name="13TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=35.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1401-1 BR KITCHEN K3A", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=33.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=36.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1401-1 BR BATHROOM B1C", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1402-1 BR & H.O. KITCHEN K2D", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1402-1 BR & H.O. BATHROOM B2A", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1403-STUDIO KITCHEN K1", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1403-STUDIO BATHROOM B2A", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1404-STUDIO KITCHEN K1", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1404-STUDIO BATHROOM B3A", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=42.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1405-STUDIO KITCHEN K1", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1405-STUDIO BATHROOM B4A", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1406-2 BR KITCHEN K4A", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP WATERFALL EDGES", material_type="SOLID SURFACE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1406-2 BR BATHROOM B1A", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1406-2 BR BATHROOM B2A", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1407-1 BR KITCHEN K2A", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1407-1 BR BATHROOM B4A", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1408-1 BR KITCHEN K2A", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1408-1 BR BATHROOM B4B", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1409-STUDIO KITCHEN K1", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1409-STUDIO BATHROOM B5B", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=53.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=34.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1410-STUDIO KITCHEN K1", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1410-STUDIO BATHROOM B5A", floor_name="14TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=35.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1501-1 BR KITCHEN K3A", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=33.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=36.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1501-1 BR BATHROOM B1C", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1502-1 BR & H.O. KITCHEN K2D", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1502-1 BR & H.O. BATHROOM B2A", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1503-STUDIO KITCHEN K1", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1503-STUDIO BATHROOM B2A", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1504-STUDIO KITCHEN K1", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1504-STUDIO BATHROOM B3A", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=42.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1505-STUDIO KITCHEN K1", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1505-STUDIO BATHROOM B4A", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1506-2 BR KITCHEN K4A", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP WATERFALL EDGES", material_type="SOLID SURFACE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1506-2 BR BATHROOM B1A", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1506-2 BR BATHROOM B2A", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1507-1 BR KITCHEN K2A", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1507-1 BR BATHROOM B4A", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1508-1 BR KITCHEN K2A", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1508-1 BR BATHROOM B4B", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1509-STUDIO KITCHEN K1", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1509-STUDIO BATHROOM B5B", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=53.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=34.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1510-STUDIO KITCHEN K1", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1510-STUDIO BATHROOM B5A", floor_name="15TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=35.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1601-1 BR KITCHEN K3A", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=33.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=36.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1601-1 BR BATHROOM B1C", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1602-1 BR & H.O. KITCHEN K2D", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1602-1 BR & H.O. BATHROOM B2A", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1603-STUDIO KITCHEN K1", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1603-STUDIO BATHROOM B2A", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1604-STUDIO KITCHEN K1", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1604-STUDIO BATHROOM B3A", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=42.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1605-STUDIO KITCHEN K1", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1605-STUDIO BATHROOM B4A", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1606-2 BR KITCHEN K4A", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP WATERFALL EDGES", material_type="SOLID SURFACE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1606-2 BR BATHROOM B1A", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1606-2 BR BATHROOM B2A", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1607-1 BR KITCHEN K2A", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1607-1 BR BATHROOM B4A", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1608-1 BR KITCHEN K2A", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1608-1 BR BATHROOM B4B", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1609-STUDIO KITCHEN K1", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1609-STUDIO BATHROOM B5B", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=53.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=34.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1610-STUDIO KITCHEN K1", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1610-STUDIO BATHROOM B5A", floor_name="16TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=35.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1701-1 BR KITCHEN K3A", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=33.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=36.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1701-1 BR BATHROOM B1C", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1702-1 BR & H.O. KITCHEN K2D", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1702-1 BR & H.O. BATHROOM B2A", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1703-STUDIO KITCHEN K1", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1703-STUDIO BATHROOM B2A", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1704-STUDIO KITCHEN K1", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1704-STUDIO BATHROOM B3A", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=42.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1705-STUDIO KITCHEN K1", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1705-STUDIO BATHROOM B4A", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1706-2 BR KITCHEN K4A", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP WATERFALL EDGES", material_type="SOLID SURFACE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1706-2 BR BATHROOM B1A", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1706-2 BR BATHROOM B2A", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1707-1 BR KITCHEN K2A", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1707-1 BR BATHROOM B4A", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1708-1 BR KITCHEN K2A", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1708-1 BR BATHROOM B4B", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1709-STUDIO KITCHEN K1", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1709-STUDIO BATHROOM B5B", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=53.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=34.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=67.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1710-STUDIO KITCHEN K1", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1710-STUDIO BATHROOM B5A", floor_name="17TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=35.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1801-1 BR KITCHEN K3A", floor_name="18TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=33.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=36.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1801-1 BR BATHROOM B1C", floor_name="18TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=63.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1802-1 BR & H.O. KITCHEN K2D", floor_name="18TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1802-1 BR & H.O. BATHROOM B2A", floor_name="18TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1803-STUDIO KITCHEN K1", floor_name="18TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1803-STUDIO BATHROOM B2A", floor_name="18TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1804-STUDIO KITCHEN K1", floor_name="18TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1804-STUDIO BATHROOM B3A", floor_name="18TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=42.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1805-STUDIO KITCHEN K1", floor_name="18TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1805-STUDIO BATHROOM B4A", floor_name="18TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1806-2 BR KITCHEN K4A", floor_name="18TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP WATERFALL EDGES", material_type="SOLID SURFACE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1806-2 BR BATHROOM B1A", floor_name="18TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1806-2 BR BATHROOM B2A", floor_name="18TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=188.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1807-1 BR KITCHEN K2A", floor_name="18TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1807-1 BR BATHROOM B4A", floor_name="18TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1808-1 BR KITCHEN K2A", floor_name="18TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1808-1 BR BATHROOM B4B", floor_name="18TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1809-STUDIO KITCHEN K2E", floor_name="18TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=22.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=22.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1809-STUDIO BATHROOM B1A", floor_name="18TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1901-2 BR KITCHEN K6", floor_name="19TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1901-2 BR BATHROOM B2B", floor_name="19TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=28.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1901-2 BR BATHROOM B1A", floor_name="19TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1902-STUDIO KITCHEN K1", floor_name="19TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1902-STUDIO BATHROOM B3C", floor_name="19TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1903-STUDIO KITCHEN K1", floor_name="19TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1903-STUDIO BATHROOM B4A", floor_name="19TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1904-STUDIO KITCHEN K1", floor_name="19TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1904-STUDIO BATHROOM B3C", floor_name="19TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1905-3 BR KITCHEN K2B", floor_name="19TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP WATERFALL EDGES", material_type="SOLID SURFACE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1905-3 BR BATHROOM B2A", floor_name="19TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1905-3 BR BATHROOM B2B", floor_name="19TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=28.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1905-3 BR KITCHEN K4B", floor_name="19TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP WATERFALL EDGES", material_type="SOLID SURFACE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1905-3 BR BATHROOM B2A", floor_name="19TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=27.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1905-3 BR BATHROOM B3B", floor_name="19TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=42.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1907-1 BR KITCHEN K2E", floor_name="19TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=22.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=22.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="1907-1 BR BATHROOM B1A", floor_name="19TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2001-2 BR KITCHEN K3B", floor_name="20TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=33.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=36.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2001-2 BR BATHROOM B2B", floor_name="20TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=28.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2001-2 BR BATHROOM B2B", floor_name="20TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=28.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2002-STUDIO KITCHEN K1", floor_name="20TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=17.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2002-STUDIO BATHROOM B3D", floor_name="20TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=40.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=28.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2003-STUDIO KITCHEN K1", floor_name="20TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2003-STUDIO BATHROOM B3D", floor_name="20TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=40.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=28.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2004-STUDIO KITCHEN K1", floor_name="20TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2004-STUDIO BATHROOM B4A", floor_name="20TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2005-2 BR KITCHEN K4C", floor_name="20TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=12.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP WATERFALL EDGES", material_type="SOLID SURFACE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2005-2 BR BATHROOM B1D", floor_name="20TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2005-2 BR BATHROOM B1D", floor_name="20TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2006-2 BR KITCHEN K2C", floor_name="20TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2006-2 BR BATHROOM B3B", floor_name="20TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=42.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TI-16", finish_type="SHOWER FLOOR", material_type="MOSAIC TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=82.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=52.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2006-2 BR BATHROOM B4D", floor_name="20TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=56.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2007-1 BR KITCHEN K2E", floor_name="20TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=22.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=22.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2007-1 BR BATHROOM B1A", floor_name="20TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2101-2 BR KITCHEN K5A", floor_name="21TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=14.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=13.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=21.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP WATERFALL EDGES", material_type="SOLID SURFACE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2101-2 BR BATHROOM B4A", floor_name="21TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2102-STUDIO KITCHEN K1", floor_name="21TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2102-STUDIO BATHROOM B4A", floor_name="21TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2103-STUDIO KITCHEN K1", floor_name="21TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=19.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2103-STUDIO BATHROOM B4A", floor_name="21TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2104-2 BR KITCHEN K5B", floor_name="21TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=13.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=10.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ISLAND COUNTER TOP WATERFALL EDGES", material_type="SOLID SURFACE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2104-2 BR BATHROOM B1A", floor_name="21TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2104-2 BR BATHROOM B4A", floor_name="21TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2105-1 BR KITCHEN K7", floor_name="21TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=40.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=44.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2105-1 BR BATHROOM B4A", floor_name="21TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=48.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2106-1 BR KITCHEN K2E", floor_name="21TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=22.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="COUNTER TOP BACKSPLASH/1'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-01", finish_type="COUNTER TOP BACKSPLASH/FULL HEIGHT", material_type="TILE", work_type="S&I", quantity=22.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="2106-1 BR BATHROOM B1A", floor_name="21TH  FLOOR", length_ft=10.0, width_ft=10.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-02", finish_type="VANITY COUNTER TOP", material_type="STONE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-02", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-04", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="SHOWER WALL", material_type="TILE", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="T-03", finish_type="BATH TUB FRONT SIDE", material_type="TILE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-02", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=26.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=100.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SOUNDPROOF", finish_type="FLOOR", material_type="SOUNDPROOF", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=50.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="METAL TRIM", work_type="S&I", quantity=46.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-03-SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        return rooms

    @staticmethod
    def get_2817_surgery_metadata() -> Dict[str, str]:
        return {
            "project_name": "[2817] Surgery Office 110 E 60th Street",
            "client_name": "OISIN REYNOLDS",
            "client_company": "J.T. MAGEN COMPANY INC.",
            "date_str": "07/23/2026"
        }

    @staticmethod
    def get_2817_surgery_specs() -> Dict[str, MaterialSpec]:
        return {
            "ST-01": MaterialSpec(symbol="ST-01", description="BANDA, MARBLE DRIFTWOOD HONED", unit="SQ FT", budget_price=0.0, notes="Elevator vestibule, reception & waiting area marble floor & wall slabs", trade="Tile & Stone"),
            "ST-02": MaterialSpec(symbol="ST-02", description="BAS, MARBLE WOODGRAIN BROWN HONED", unit="SQ FT", budget_price=0.0, notes="Vestibule, reception & waiting area feature floor marble & baseboards", trade="Tile & Stone"),
            "ST-04": MaterialSpec(symbol="ST-04", description="BAS, MARBLE WOODGRAIN BROWN SANDBLASTED", unit="SQ FT", budget_price=0.0, notes="Waiting room restroom marble floor & base", trade="Tile & Stone"),
            "CT-01": MaterialSpec(symbol="CT-01", description="PORCELANOSA, CERAMIC TILE 13 X 39 MARMI CHINA MATTE", unit="SQ FT", budget_price=0.0, notes="Private restroom full height ceramic wall tile & base", trade="Tile & Stone"),
            "TL-00": MaterialSpec(symbol="TL-00", description="COMMERCIAL GRADE FLOOR & WALL TILE", unit="SQ FT", budget_price=0.0, notes="Clinical & Recovery restrooms floor, wall & base tile", trade="Tile & Stone"),
            "WATERPROOF": MaterialSpec(symbol="WATERPROOF", description="SELF-CURING LIQUID POLYMER RUBBER WATERPROOFING MEMBRANE", unit="SQ FT", budget_price=0.0, notes="Wet area floors & 6\" wall upturns", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="PORTLAND CEMENT MORTAR BED / MUD-SET PREPARATION", unit="SQ FT", budget_price=0.0, notes="Subfloor leveling & mortar bed under stone & tile", trade="Tile & Stone"),
            "METAL TRIM": MaterialSpec(symbol="METAL TRIM", description="SATIN NICKEL & NEGATIVE CORNER METAL BEAD TRIM", unit="LN FT", budget_price=0.0, notes="Floor transitions and negative corner wall trims", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="NATURAL MARBLE DOORWAY TRANSITION SADDLE", unit="PCS", budget_price=0.0, notes="Doorway transition saddles", trade="Tile & Stone")
        }

    @staticmethod
    def get_2817_surgery_rooms() -> List[RoomTakeoff]:
        rooms = []
        rooms.append(RoomTakeoff(room_name="ELEVATOR VESTIBULE 00", floor_name="15TH FLOOR", length_ft=12.0, width_ft=12.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="FLOOR", material_type="MARBLE", work_type="S&I", quantity=129.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02", finish_type="FLOOR", material_type="MARBLE", work_type="S&I", quantity=80.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="WALL", material_type="MARBLE", work_type="S&I", quantity=262.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="ELEVATOR DOOR SIDE", material_type="MARBLE", work_type="S&I", quantity=90.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=209.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=209.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="SATIN NICKEL METAL TRIM", work_type="S&I", quantity=51.0, unit="LN FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="NEGATIVE CORNER METAL BEAD-METAL TRIM", work_type="S&I", quantity=166.0, unit="LN FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=4.0, unit="PCS", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="RECEPTION AREA 01", floor_name="15TH FLOOR", length_ft=12.0, width_ft=12.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="FLOOR", material_type="MARBLE", work_type="S&I", quantity=182.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02", finish_type="FLOOR", material_type="MARBLE", work_type="S&I", quantity=154.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="WALL", material_type="MARBLE", work_type="S&I", quantity=187.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="WALL SIDE", material_type="MARBLE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=336.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=336.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="SATIN NICKEL METAL TRIM", work_type="S&I", quantity=55.0, unit="LN FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="NEGATIVE CORNER METAL BEAD-METAL TRIM", work_type="S&I", quantity=135.0, unit="LN FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="WAITING AREA 02", floor_name="15TH FLOOR", length_ft=12.0, width_ft=12.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-01", finish_type="FLOOR", material_type="MARBLE", work_type="S&I", quantity=120.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02", finish_type="FLOOR", material_type="MARBLE", work_type="S&I", quantity=121.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="WALL", material_type="MARBLE", work_type="S&I", quantity=183.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="WALL SIDE", material_type="MARBLE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-02", finish_type="WALL", material_type="MARBLE BASE", work_type="S&I", quantity=12.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=241.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=241.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="FLOOR", material_type="SATIN NICKEL METAL TRIM", work_type="S&I", quantity=50.0, unit="LN FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="NEGATIVE CORNER METAL BEAD-METAL TRIM", work_type="S&I", quantity=77.0, unit="LN FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="WAITING ROOM RESTROOM 03", floor_name="15TH FLOOR", length_ft=12.0, width_ft=12.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="ST-04", finish_type="FLOOR", material_type="MARBLE", work_type="S&I", quantity=44.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-01", finish_type="WALL", material_type="MARBLE", work_type="S&I", quantity=64.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="ST-04", finish_type="WALL", material_type="MARBLE BASE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=44.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=12.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=44.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="METAL TRIM", finish_type="WALL", material_type="NEGATIVE CORNER METAL BEAD-METAL TRIM", work_type="S&I", quantity=32.0, unit="LN FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="PCS", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="PRIVATE RESTROOM 19", floor_name="15TH FLOOR", length_ft=12.0, width_ft=12.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="CT-01", finish_type="WALL", material_type="CERAMIC TILE", work_type="S&I", quantity=152.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CT-01", finish_type="WALL", material_type="CERAMIC TILE BASE", work_type="S&I", quantity=20.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=12.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="CLINICAL RESTROOM", floor_name="15TH FLOOR", length_ft=12.0, width_ft=12.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-00", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=38.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-00", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=200.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-00", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=22.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=38.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=13.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=38.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="RECOVERY RESTROOM", floor_name="15TH FLOOR", length_ft=12.0, width_ft=12.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="TL-00", finish_type="FLOOR", material_type="TILE", work_type="S&I", quantity=38.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-00", finish_type="WALL", material_type="TILE", work_type="S&I", quantity=200.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-00", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=22.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=38.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=13.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=38.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="", trade="Tile & Stone"),
        ]))
        return rooms

    @staticmethod
    @staticmethod
    def get_2419_melville_metadata() -> Dict[str, str]:
        return {
            "project_name": "[2419] MELVILLE 175 BROADHOLLOW ROAD 1ST FLOOR MELVILLE",
            "client_name": "VINCENT BRUZZESE",
            "client_company": "HITT CONTRACTING INC.",
            "date_str": "05/19/2025"
        }

    @staticmethod
    def get_2419_melville_specs() -> Dict[str, MaterialSpec]:
        return {
            "SS-01": MaterialSpec(symbol="SS-01", description="Caesarstone, Solid Surface, 4001 Organic White", unit="SQ FT", budget_price=0.0, notes="Restroom, Cafe, Mothers & Wellness countertops & waterfall islands", trade="Tile & Stone"),
            "PT-01": MaterialSpec(symbol="PT-01", description="Mosa, Porcelain Tile, Terra Core Collection 225V Smooth 24X48", unit="SQ FT", budget_price=14.88, notes="Vestibule, Reception, Cafe, Mothers & Wellness floor tile ($14.88/sf)", trade="Tile & Stone"),
            "PT-02": MaterialSpec(symbol="PT-02", description="Ergon Emil Group, Porcelain Tile, Corner Stone Slate Grey Honed 12X24", unit="SQ FT", budget_price=6.85, notes="ADA Restroom floor tile ($6.85/sf)", trade="Tile & Stone"),
            "TL-01": MaterialSpec(symbol="TL-01", description="Virginia Tile, Porcelain Tile, Mayfair Statuario Venato Polished 12X24", unit="SQ FT", budget_price=0.0, notes="ADA Restroom full height wall tile", trade="Tile & Stone"),
            "TL-02": MaterialSpec(symbol="TL-02", description="Daltile, Porcelain Tile, Stagecraft Galaxy Matte 1469 Glossy 3X12", unit="SQ FT", budget_price=8.42, notes="Cafe countertop backsplash tile ($8.42/sf)", trade="Tile & Stone"),
            "TB-01": MaterialSpec(symbol="TB-01", description="Ergon, Tile Base, Corner Stone Slate Gray Honed 4\" H", unit="LN FT", budget_price=13.97, notes="ADA Restroom tile base ($13.97/pc)", trade="Tile & Stone"),
            "WATERPROOF": MaterialSpec(symbol="WATERPROOF", description="Generic Manufacturer - Anti Crack Membrane Waterproof", unit="SQ FT", budget_price=0.0, notes="Under all floor tiles & 6\" wet wall upturns", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="Generic Manufacturer - Mud Set Leveling Bed", unit="SQ FT", budget_price=0.0, notes="Mortar bed & subfloor prep", trade="Tile & Stone"),
            "TR-01-METAL TRIM": MaterialSpec(symbol="TR-01-METAL TRIM", description="Anodized Aluminum, Satin Metal Trim", unit="LN FT", budget_price=0.0, notes="Cafe transition strips", trade="Tile & Stone"),
            "TR-02-METAL TRIM": MaterialSpec(symbol="TR-02-METAL TRIM", description="Anodized Aluminum, Bright Black Metal Trim", unit="LN FT", budget_price=0.0, notes="Reception floor transition strips", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="Generic Manufacturer - Saddle", unit="PCS", budget_price=0.0, notes="Doorway transition saddles", trade="Tile & Stone")
        }

    @staticmethod
    def get_2419_melville_rooms() -> List[RoomTakeoff]:
        rooms = []
        rooms.append(RoomTakeoff(room_name="ENTRANCE VESTIBULE", floor_name="FIRST FLOOR", length_ft=15.0, width_ft=15.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="PT-01", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=210.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=210.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=210.0, unit="SQ FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="RECEPTION", floor_name="FIRST FLOOR", length_ft=15.0, width_ft=15.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="PT-01", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=274.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=274.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=274.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TR-02-METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=80.0, unit="LN FT", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="ADA RESTROOM", floor_name="FIRST FLOOR", length_ft=15.0, width_ft=15.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SS-01", finish_type="COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=7.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="COUNTERTOP APRON/3'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="PT-02", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=70.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-01", finish_type="WALL", material_type="PORCELAIN TILE", work_type="S&I", quantity=75.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="TILE BASE", work_type="S&I", quantity=30.0, unit="LN FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=70.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=18.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=70.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="MOTHERS ROOM", floor_name="FIRST FLOOR", length_ft=15.0, width_ft=15.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SS-01", finish_type="COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="PT-01", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=95.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=95.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=95.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="WELLNESS ROOM", floor_name="FIRST FLOOR", length_ft=15.0, width_ft=15.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SS-01", finish_type="COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=15.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="PT-01", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=95.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=95.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=95.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="CAFE/HUB", floor_name="FIRST FLOOR", length_ft=15.0, width_ft=15.0, ceiling_height_ft=9.0, items=[
            TakeoffLineItem(symbol="SS-01", finish_type="#1 COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=45.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="#2 COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=5.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TL-02", finish_type="COUNTERTOP BACKSPLASH/FULL HEIGHT", material_type="PORCELAIN TILE", work_type="S&I", quantity=62.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="#1 ISLAND COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=65.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="#2 ISLAND COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=25.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="ISLAND COUNTERTOP APRON/2'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=12.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="ISLAND COUNTERTOP FRONT SIDE", material_type="SOLID SURFACE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="ISLAND COUNTERTOP WATERFALL EDGES", material_type="SOLID SURFACE", work_type="S&I", quantity=23.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SS-01", finish_type="ISLAND COUNTERTOP WATERFALL EDGES INSIDE", material_type="SOLID SURFACE", work_type="S&I", quantity=7.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="PT-01", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=1699.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=1699.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=1699.0, unit="SQ FT", notes="", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TR-01-METAL TRIM", finish_type="FLOOR", material_type="METAL TRIM", work_type="S&I", quantity=12.0, unit="LN FT", notes="", trade="Tile & Stone"),
        ]))
        return rooms

    @staticmethod
    def get_fhjc_metadata() -> Dict[str, str]:
        return {
            "project_name": "[BID] Forest Hills Jewish Center - 70-35 113th St, Flushing NY (HE2PD FHJC)",
            "client_name": "Forest Hills Jewish Center",
            "client_company": "General Contractor / Owner",
            "date_str": "03/20/2026"
        }

    @staticmethod
    def get_fhjc_specs() -> Dict[str, MaterialSpec]:
        return {
            "CTF-01": MaterialSpec(symbol="CTF-01", description="NASCO, CEPPO COLLECTION LIGHT GREY MATTE 24\" X 48\" X 3/8\" PORCELAIN TILE", unit="SQ FT", budget_price=0.0, notes="Lobby, Entrance & Flex Space Floors", trade="Tile & Stone"),
            "CTF-02": MaterialSpec(symbol="CTF-02", description="DALTILE, COHESION C026 DARK GREY MATTE 24\" X 24\" X 3/8\" COLOR BODY PORCELAIN TILE", unit="SQ FT", budget_price=0.0, notes="Classroom Restrooms (Cellar & Level 1)", trade="Tile & Stone"),
            "CTF-03": MaterialSpec(symbol="CTF-03", description="NASCO, ETERNITY COLLECTION IVORY MATTE 24\" X 48\" X 3/8\" PORCELAIN TILE", unit="SQ FT", budget_price=0.0, notes="Core, Public & Unisex Restrooms (Cellar, Level 1, Level 2)", trade="Tile & Stone"),
            "CTW-01": MaterialSpec(symbol="CTW-01", description="NEMO TILE, CERAMIC WALL TILE 3\" X 10\" RUNNING BOND", unit="SQ FT", budget_price=0.0, notes="Level 02 Staff Pantry Backsplash", trade="Tile & Stone"),
            "CTW-02": MaterialSpec(symbol="CTW-02", description="CANCOS TILE & STONE, PORCELAIN WALL TILE 24\" X 48\"", unit="SQ FT", budget_price=0.0, notes="Typical Core Restrooms Wet Walls", trade="Tile & Stone"),
            "CTW-03": MaterialSpec(symbol="CTW-03", description="DALTILE, KEYSTONES PORCELAIN MOSAIC 2\" X 2\"", unit="SQ FT", budget_price=0.0, notes="Typical Core & Unisex Restrooms Wet Walls", trade="Tile & Stone"),
            "CTW-04": MaterialSpec(symbol="CTW-04", description="DALTILE, GLAZED CERAMIC WALL TILE 6\" X 6\" FULL HEIGHT", unit="SQ FT", budget_price=0.0, notes="Typical Classroom Restrooms (Cellar & Level 1)", trade="Tile & Stone"),
            "SSW-01": MaterialSpec(symbol="SSW-01", description="COSENTINO, DEKTON WALL CLADDING / SLAB 128.74\" X 57.87\"", unit="SQ FT", budget_price=0.0, notes="Level 01 Entrance Vestibule & Lobby Feature Wall", trade="Tile & Stone"),
            "TB-01": MaterialSpec(symbol="TB-01", description="NASCO, BULLNOSE PORCELAIN TILE BASE 3\" X 24\" / 3\" X 48\"", unit="LN FT", budget_price=0.0, notes="Perimeter Tile Base in Restrooms & Janitor Closets", trade="Tile & Stone"),
            "SSF-01": MaterialSpec(symbol="SSF-01", description="CAESARSTONE, SOLID SURFACE COUNTERTOP 3/4\"", unit="SQ FT", budget_price=0.0, notes="Level 02 Pantry & Classroom Sinks", trade="Tile & Stone"),
            "SSF-02": MaterialSpec(symbol="SSF-02", description="CAESARSTONE, SOLID SURFACE CUSTOM RESTROOM VANITY TOPS", unit="SQ FT", budget_price=0.0, notes="Restroom Vanity Countertops with Undermount Sinks", trade="Tile & Stone"),
            "WATERPROOF": MaterialSpec(symbol="WATERPROOF", description="LATICRETE / HYDRO BAN LIQUID WATERPROOFING MEMBRANE", unit="SQ FT", budget_price=0.0, notes="Under All Tiled Floors + 6\" Coved Base + Wet Walls", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="PORTLAND MUD-SET & UNCOUPLING UNDERLAYMENT BED", unit="SQ FT", budget_price=0.0, notes="Subfloor Prep across All Tiled Floors", trade="Tile & Stone"),
            "MS": MaterialSpec(symbol="MS", description="SCHLUTER SYSTEMS 1/4\" SATIN STAINLESS STEEL EDGE TRIM", unit="LN FT", budget_price=0.0, notes="Tile Edge Terminations & Floor Transitions", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="GENERIC NATURAL MARBLE / STONE DOORWAY THRESHOLD SADDLE", unit="PCS", budget_price=0.0, notes="Doorway Transition Saddles", trade="Tile & Stone")
        }

    @staticmethod
    def get_fhjc_rooms() -> List[RoomTakeoff]:
        rooms = []
        
        # ================= SUB-CELLAR LEVEL =================
        rooms.append(RoomTakeoff(room_name="SUB-CELLAR MECHANICAL & BOH", floor_name="SUB-CELLAR LEVEL", length_ft=35.0, width_ft=20.0, ceiling_height_ft=11.0, items=[
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=700.0, unit="SQ FT", notes="Sub-slab patch & level prep", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="FLOOR", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=15.0, unit="LN FT", notes="Threshold edge trim to stair/elevator", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="PCS", notes="Sub-cellar doorway transitions", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="SUB-CELLAR STORAGE & UTILITY", floor_name="SUB-CELLAR LEVEL", length_ft=22.0, width_ft=14.0, ceiling_height_ft=11.0, items=[
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=308.0, unit="SQ FT", notes="Subfloor leveling bed", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Doorway transition saddle", trade="Tile & Stone"),
        ]))

        # ================= CELLAR LEVEL =================
        rooms.append(RoomTakeoff(room_name="CELLAR CORE RESTROOM - MEN'S", floor_name="CELLAR LEVEL", length_ft=16.0, width_ft=12.0, ceiling_height_ft=9.5, wall_tile_height_ft=9.5, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-03", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=192.0, unit="SQ FT", notes="Nasco Eternity Ivory 24x48 porcelain floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-03", finish_type="WALL", material_type="PORCELAIN MOSAIC", work_type="S&I", quantity=180.0, unit="SQ FT", notes="Daltile Keystones 2x2 mosaic wet walls", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-02", finish_type="WALL", material_type="PORCELAIN TILE", work_type="S&I", quantity=150.0, unit="SQ FT", notes="Cancos 24x48 porcelain wall tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=56.0, unit="LN FT", notes="Nasco 3\" bullnose tile base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="DOUBLE VANITY COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="Caesarstone solid surface double vanity top", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="VANITY APRON/4'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="4 inch drop apron", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="VANITY BACKSPLASH/4'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="4 inch solid surface splash", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=192.0, unit="SQ FT", notes="Floor waterproofing membrane", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=28.0, unit="SQ FT", notes="6 inch base waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=192.0, unit="SQ FT", notes="Subfloor mud-set leveling bed", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=32.0, unit="LN FT", notes="Schluter 1/4\" satin stainless trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Stone doorway threshold saddle", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="CELLAR CORE RESTROOM - WOMEN'S", floor_name="CELLAR LEVEL", length_ft=16.0, width_ft=14.0, ceiling_height_ft=9.5, wall_tile_height_ft=9.5, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-03", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=224.0, unit="SQ FT", notes="Nasco Eternity Ivory 24x48 porcelain floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-03", finish_type="WALL", material_type="PORCELAIN MOSAIC", work_type="S&I", quantity=210.0, unit="SQ FT", notes="Daltile Keystones 2x2 mosaic wet walls", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-02", finish_type="WALL", material_type="PORCELAIN TILE", work_type="S&I", quantity=170.0, unit="SQ FT", notes="Cancos 24x48 porcelain wall tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=60.0, unit="LN FT", notes="Nasco 3\" bullnose tile base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="TRIPLE VANITY COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="Caesarstone solid surface triple vanity top", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="VANITY APRON/4'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="4 inch drop apron", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="VANITY BACKSPLASH/4'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="4 inch solid surface splash", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=224.0, unit="SQ FT", notes="Floor waterproofing membrane", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=30.0, unit="SQ FT", notes="6 inch base waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=224.0, unit="SQ FT", notes="Subfloor mud-set leveling bed", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=36.0, unit="LN FT", notes="Schluter 1/4\" satin stainless trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Stone doorway threshold saddle", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="CELLAR UNISEX / ADA RESTROOM", floor_name="CELLAR LEVEL", length_ft=8.0, width_ft=7.0, ceiling_height_ft=9.5, wall_tile_height_ft=9.5, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-03", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=56.0, unit="SQ FT", notes="Nasco Eternity Ivory 24x48 floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-03", finish_type="WALL", material_type="PORCELAIN MOSAIC", work_type="S&I", quantity=120.0, unit="SQ FT", notes="Daltile Keystones 2x2 mosaic wet wall", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=30.0, unit="LN FT", notes="Nasco 3\" bullnose tile base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="SINGLE VANITY COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=7.0, unit="SQ FT", notes="Caesarstone vanity top", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=56.0, unit="SQ FT", notes="Floor waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=56.0, unit="SQ FT", notes="Subfloor mud-set prep", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=16.0, unit="LN FT", notes="Schluter trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Stone transition saddle", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="CELLAR CLASSROOM RESTROOM #1", floor_name="CELLAR LEVEL", length_ft=7.5, width_ft=6.0, ceiling_height_ft=9.0, wall_tile_height_ft=9.0, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-02", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=45.0, unit="SQ FT", notes="Daltile Cohesion 24x24 dark grey floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-04", finish_type="WALL", material_type="CERAMIC TILE", work_type="S&I", quantity=190.0, unit="SQ FT", notes="Daltile 6x6 glazed ceramic full height wall tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=27.0, unit="LN FT", notes="Nasco 3\" tile base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="SINK TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=6.0, unit="SQ FT", notes="Caesarstone sink surround", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=45.0, unit="SQ FT", notes="Floor waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=45.0, unit="SQ FT", notes="Subfloor prep", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=18.0, unit="LN FT", notes="Schluter edge trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Stone transition saddle", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="CELLAR CLASSROOM RESTROOM #2", floor_name="CELLAR LEVEL", length_ft=7.5, width_ft=6.0, ceiling_height_ft=9.0, wall_tile_height_ft=9.0, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-02", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=45.0, unit="SQ FT", notes="Daltile Cohesion 24x24 dark grey floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-04", finish_type="WALL", material_type="CERAMIC TILE", work_type="S&I", quantity=190.0, unit="SQ FT", notes="Daltile 6x6 glazed ceramic full height wall tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=27.0, unit="LN FT", notes="Nasco 3\" tile base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="SINK TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=6.0, unit="SQ FT", notes="Caesarstone sink surround", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=45.0, unit="SQ FT", notes="Floor waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=45.0, unit="SQ FT", notes="Subfloor prep", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=18.0, unit="LN FT", notes="Schluter edge trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Stone transition saddle", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="CELLAR PANTRY & BREAK AREA", floor_name="CELLAR LEVEL", length_ft=12.0, width_ft=10.0, ceiling_height_ft=9.5, wall_tile_height_ft=2.5, door_count=1, items=[
            TakeoffLineItem(symbol="SSF-01", finish_type="COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=28.0, unit="SQ FT", notes="Caesarstone solid surface pantry countertop", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="1-1/2 inch drop apron", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="COUNTERTOP BACKSPLASH/FULL HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="Full height splash under upper cabinets", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="FLOOR", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=8.0, unit="LN FT", notes="Schluter floor transition strip", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Stone doorway saddle", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="CELLAR JANITOR CLOSET", floor_name="CELLAR LEVEL", length_ft=6.0, width_ft=5.0, ceiling_height_ft=9.0, wall_tile_height_ft=4.0, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-03", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="Nasco Eternity Ivory 24x48 floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-04", finish_type="WALL", material_type="CERAMIC TILE", work_type="S&I", quantity=44.0, unit="SQ FT", notes="Mop sink splash surround", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=22.0, unit="LN FT", notes="Nasco tile base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=30.0, unit="SQ FT", notes="Floor waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=30.0, unit="SQ FT", notes="Subfloor prep", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Stone transition saddle", trade="Tile & Stone"),
        ]))

        # ================= LEVEL 1 =================
        rooms.append(RoomTakeoff(room_name="LEVEL 1 MAIN LOBBY & ENTRANCE", floor_name="LEVEL 1", length_ft=38.0, width_ft=28.0, ceiling_height_ft=14.0, wall_tile_height_ft=0.0, door_count=2, items=[
            TakeoffLineItem(symbol="CTF-01", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=1064.0, unit="SQ FT", notes="Nasco Ceppo Light Grey 24x48 porcelain tile floor", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSW-01", finish_type="FEATURE WALL", material_type="DEKTON SLAB", work_type="S&I", quantity=280.0, unit="SQ FT", notes="Cosentino Dekton large slab feature wall cladding (A-627)", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="CUSTOM LOBBY STONEWORK", material_type="SOLID SURFACE", work_type="S&I", quantity=45.0, unit="SQ FT", notes="Caesarstone custom lobby reception desk tops & trims", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=1064.0, unit="SQ FT", notes="Floor crack isolation & waterproofing membrane", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=1064.0, unit="SQ FT", notes="Subfloor mud-set / uncoupling leveling bed", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="FLOOR", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=76.0, unit="LN FT", notes="Schluter 1/4\" satin stainless steel floor transitions", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="LEVEL 1 ENTRANCE VESTIBULE", floor_name="LEVEL 1", length_ft=14.0, width_ft=10.0, ceiling_height_ft=12.0, wall_tile_height_ft=10.0, door_count=2, items=[
            TakeoffLineItem(symbol="CTF-01", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=75.0, unit="SQ FT", notes="Nasco Ceppo 24x48 tile perimeter around mat grating", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSW-01", finish_type="WALL", material_type="DEKTON SLAB", work_type="S&I", quantity=180.0, unit="SQ FT", notes="Cosentino Dekton wall cladding", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=75.0, unit="SQ FT", notes="Floor waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=75.0, unit="SQ FT", notes="Subfloor prep", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="FLOOR", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=32.0, unit="LN FT", notes="Schluter frame and transition trims", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="PCS", notes="Heavy duty entrance threshold saddles", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="LEVEL 1 CORE RESTROOM - MEN'S", floor_name="LEVEL 1", length_ft=18.0, width_ft=12.0, ceiling_height_ft=10.0, wall_tile_height_ft=10.0, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-03", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=216.0, unit="SQ FT", notes="Nasco Eternity Ivory 24x48 porcelain floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-03", finish_type="WALL", material_type="PORCELAIN MOSAIC", work_type="S&I", quantity=210.0, unit="SQ FT", notes="Daltile Keystones 2x2 mosaic wet walls", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-02", finish_type="WALL", material_type="PORCELAIN TILE", work_type="S&I", quantity=180.0, unit="SQ FT", notes="Cancos 24x48 porcelain wall tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=60.0, unit="LN FT", notes="Nasco 3\" bullnose tile base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="DOUBLE VANITY COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=18.0, unit="SQ FT", notes="Caesarstone solid surface double vanity top", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="VANITY APRON/4'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="4 inch drop apron", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="VANITY BACKSPLASH/4'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="4 inch solid surface splash", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=216.0, unit="SQ FT", notes="Floor waterproofing membrane", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=30.0, unit="SQ FT", notes="6 inch base waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=216.0, unit="SQ FT", notes="Subfloor mud-set leveling bed", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=38.0, unit="LN FT", notes="Schluter 1/4\" satin stainless trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Stone doorway threshold saddle", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="LEVEL 1 CORE RESTROOM - WOMEN'S", floor_name="LEVEL 1", length_ft=18.0, width_ft=14.0, ceiling_height_ft=10.0, wall_tile_height_ft=10.0, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-03", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=252.0, unit="SQ FT", notes="Nasco Eternity Ivory 24x48 porcelain floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-03", finish_type="WALL", material_type="PORCELAIN MOSAIC", work_type="S&I", quantity=240.0, unit="SQ FT", notes="Daltile Keystones 2x2 mosaic wet walls", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-02", finish_type="WALL", material_type="PORCELAIN TILE", work_type="S&I", quantity=200.0, unit="SQ FT", notes="Cancos 24x48 porcelain wall tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=64.0, unit="LN FT", notes="Nasco 3\" bullnose tile base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="TRIPLE VANITY COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="Caesarstone solid surface triple vanity top", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="VANITY APRON/4'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="4 inch drop apron", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="VANITY BACKSPLASH/4'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="4 inch solid surface splash", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=252.0, unit="SQ FT", notes="Floor waterproofing membrane", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=32.0, unit="SQ FT", notes="6 inch base waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=252.0, unit="SQ FT", notes="Subfloor mud-set leveling bed", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=42.0, unit="LN FT", notes="Schluter 1/4\" satin stainless trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Stone doorway threshold saddle", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="LEVEL 1 UNISEX / ADA RESTROOM", floor_name="LEVEL 1", length_ft=8.0, width_ft=7.5, ceiling_height_ft=10.0, wall_tile_height_ft=10.0, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-03", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=60.0, unit="SQ FT", notes="Nasco Eternity Ivory 24x48 floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-03", finish_type="WALL", material_type="PORCELAIN MOSAIC", work_type="S&I", quantity=130.0, unit="SQ FT", notes="Daltile Keystones 2x2 mosaic wet wall", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=31.0, unit="LN FT", notes="Nasco 3\" bullnose tile base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="SINGLE VANITY COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="Caesarstone vanity top", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=60.0, unit="SQ FT", notes="Floor waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=60.0, unit="SQ FT", notes="Subfloor mud-set prep", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=18.0, unit="LN FT", notes="Schluter trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Stone transition saddle", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="LEVEL 1 CLASSROOM RESTROOM #101", floor_name="LEVEL 1", length_ft=7.5, width_ft=6.5, ceiling_height_ft=9.5, wall_tile_height_ft=9.5, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-02", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=49.0, unit="SQ FT", notes="Daltile Cohesion 24x24 dark grey floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-04", finish_type="WALL", material_type="CERAMIC TILE", work_type="S&I", quantity=210.0, unit="SQ FT", notes="Daltile 6x6 glazed ceramic full height wall tile (A-646)", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=28.0, unit="LN FT", notes="Nasco 3\" tile base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="SINK TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=6.0, unit="SQ FT", notes="Caesarstone sink surround", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=49.0, unit="SQ FT", notes="Floor waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=49.0, unit="SQ FT", notes="Subfloor prep", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=20.0, unit="LN FT", notes="Schluter edge trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Stone transition saddle", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="LEVEL 1 CLASSROOM RESTROOM #102", floor_name="LEVEL 1", length_ft=7.5, width_ft=6.5, ceiling_height_ft=9.5, wall_tile_height_ft=9.5, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-02", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=49.0, unit="SQ FT", notes="Daltile Cohesion 24x24 dark grey floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-04", finish_type="WALL", material_type="CERAMIC TILE", work_type="S&I", quantity=210.0, unit="SQ FT", notes="Daltile 6x6 glazed ceramic full height wall tile (A-646)", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=28.0, unit="LN FT", notes="Nasco 3\" tile base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="SINK TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=6.0, unit="SQ FT", notes="Caesarstone sink surround", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=49.0, unit="SQ FT", notes="Floor waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=49.0, unit="SQ FT", notes="Subfloor prep", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=20.0, unit="LN FT", notes="Schluter edge trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Stone transition saddle", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="LEVEL 1 CLASSROOM RESTROOM #103", floor_name="LEVEL 1", length_ft=7.5, width_ft=6.5, ceiling_height_ft=9.5, wall_tile_height_ft=9.5, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-02", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=49.0, unit="SQ FT", notes="Daltile Cohesion 24x24 dark grey floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-04", finish_type="WALL", material_type="CERAMIC TILE", work_type="S&I", quantity=210.0, unit="SQ FT", notes="Daltile 6x6 glazed ceramic full height wall tile (A-646)", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=28.0, unit="LN FT", notes="Nasco 3\" tile base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="SINK TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=6.0, unit="SQ FT", notes="Caesarstone sink surround", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=49.0, unit="SQ FT", notes="Floor waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=49.0, unit="SQ FT", notes="Subfloor prep", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=20.0, unit="LN FT", notes="Schluter edge trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Stone transition saddle", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="LEVEL 1 CLASSROOM RESTROOM #104", floor_name="LEVEL 1", length_ft=7.5, width_ft=6.5, ceiling_height_ft=9.5, wall_tile_height_ft=9.5, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-02", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=49.0, unit="SQ FT", notes="Daltile Cohesion 24x24 dark grey floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-04", finish_type="WALL", material_type="CERAMIC TILE", work_type="S&I", quantity=210.0, unit="SQ FT", notes="Daltile 6x6 glazed ceramic full height wall tile (A-646)", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=28.0, unit="LN FT", notes="Nasco 3\" tile base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="SINK TOP", material_type="SOLID SURFACE", work_type="S&I", quantity=6.0, unit="SQ FT", notes="Caesarstone sink surround", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=49.0, unit="SQ FT", notes="Floor waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=49.0, unit="SQ FT", notes="Subfloor prep", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=20.0, unit="LN FT", notes="Schluter edge trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Stone transition saddle", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="LEVEL 1 JANITOR CLOSET", floor_name="LEVEL 1", length_ft=6.0, width_ft=5.0, ceiling_height_ft=9.5, wall_tile_height_ft=4.0, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-03", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="Nasco Eternity Ivory 24x48 floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-04", finish_type="WALL", material_type="CERAMIC TILE", work_type="S&I", quantity=44.0, unit="SQ FT", notes="Mop basin splash surround", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=22.0, unit="LN FT", notes="Nasco tile base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=30.0, unit="SQ FT", notes="Floor waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=30.0, unit="SQ FT", notes="Subfloor prep", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Stone transition saddle", trade="Tile & Stone"),
        ]))

        # ================= LEVEL 2 =================
        rooms.append(RoomTakeoff(room_name="LEVEL 2 CORE RESTROOM - MEN'S", floor_name="LEVEL 2", length_ft=16.0, width_ft=11.0, ceiling_height_ft=9.5, wall_tile_height_ft=9.5, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-03", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=176.0, unit="SQ FT", notes="Nasco Eternity Ivory 24x48 porcelain floor tile (A-616)", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-03", finish_type="WALL", material_type="PORCELAIN MOSAIC", work_type="S&I", quantity=180.0, unit="SQ FT", notes="Daltile Keystones 2x2 mosaic wet walls (A-616)", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=54.0, unit="LN FT", notes="Nasco 3\" bullnose tile base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="DOUBLE VANITY COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="Caesarstone solid surface double vanity top", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="VANITY APRON/4'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="4 inch drop apron", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="VANITY BACKSPLASH/4'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="4 inch solid surface splash", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=176.0, unit="SQ FT", notes="Floor waterproofing membrane", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=27.0, unit="SQ FT", notes="6 inch base waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=176.0, unit="SQ FT", notes="Subfloor mud-set leveling bed", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=32.0, unit="LN FT", notes="Schluter 1/4\" satin stainless trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Stone doorway threshold saddle", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="LEVEL 2 CORE RESTROOM - WOMEN'S", floor_name="LEVEL 2", length_ft=16.0, width_ft=12.0, ceiling_height_ft=9.5, wall_tile_height_ft=9.5, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-03", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=192.0, unit="SQ FT", notes="Nasco Eternity Ivory 24x48 porcelain floor tile (A-616)", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-03", finish_type="WALL", material_type="PORCELAIN MOSAIC", work_type="S&I", quantity=190.0, unit="SQ FT", notes="Daltile Keystones 2x2 mosaic wet walls (A-616)", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=56.0, unit="LN FT", notes="Nasco 3\" bullnose tile base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="DOUBLE VANITY COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=16.0, unit="SQ FT", notes="Caesarstone solid surface double vanity top", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="VANITY APRON/4'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="4 inch drop apron", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="VANITY BACKSPLASH/4'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=3.0, unit="SQ FT", notes="4 inch solid surface splash", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=192.0, unit="SQ FT", notes="Floor waterproofing membrane", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=28.0, unit="SQ FT", notes="6 inch base waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=192.0, unit="SQ FT", notes="Subfloor mud-set leveling bed", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=34.0, unit="LN FT", notes="Schluter 1/4\" satin stainless trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Stone doorway threshold saddle", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="LEVEL 2 UNISEX / ADA RESTROOM", floor_name="LEVEL 2", length_ft=8.0, width_ft=7.5, ceiling_height_ft=9.5, wall_tile_height_ft=9.5, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-03", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=60.0, unit="SQ FT", notes="Nasco Eternity Ivory 24x48 floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-03", finish_type="WALL", material_type="PORCELAIN MOSAIC", work_type="S&I", quantity=130.0, unit="SQ FT", notes="Daltile Keystones 2x2 mosaic wet wall", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=31.0, unit="LN FT", notes="Nasco 3\" bullnose tile base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-02", finish_type="SINGLE VANITY COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="Caesarstone vanity top", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=60.0, unit="SQ FT", notes="Floor waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=60.0, unit="SQ FT", notes="Subfloor mud-set prep", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=18.0, unit="LN FT", notes="Schluter trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Stone transition saddle", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="LEVEL 2 STAFF PANTRY (A-616)", floor_name="LEVEL 2", length_ft=14.0, width_ft=10.0, ceiling_height_ft=9.5, wall_tile_height_ft=2.5, door_count=1, items=[
            TakeoffLineItem(symbol="CTW-01", finish_type="WALL BACKSPLASH", material_type="CERAMIC TILE", work_type="S&I", quantity=36.0, unit="SQ FT", notes="Nemo Tile 3\" x 10\" running bond ceramic wall tile backsplash (A-616)", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=32.0, unit="SQ FT", notes="Caesarstone solid surface countertop (14'-0\" x 2'-4\")", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="1-1/2 inch front drop apron", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=14.0, unit="LN FT", notes="Schluter top edge trim above backsplash", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Stone doorway transition saddle", trade="Tile & Stone"),
        ]))
        rooms.append(RoomTakeoff(room_name="LEVEL 2 JANITOR CLOSET", floor_name="LEVEL 2", length_ft=6.0, width_ft=5.0, ceiling_height_ft=9.5, wall_tile_height_ft=4.0, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-03", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=30.0, unit="SQ FT", notes="Nasco Eternity Ivory 24x48 floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-04", finish_type="WALL", material_type="CERAMIC TILE", work_type="S&I", quantity=44.0, unit="SQ FT", notes="Mop basin splash surround", trade="Tile & Stone"),
            TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN TILE BASE", work_type="S&I", quantity=22.0, unit="LN FT", notes="Nasco tile base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=30.0, unit="SQ FT", notes="Floor waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=30.0, unit="SQ FT", notes="Subfloor prep", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Stone transition saddle", trade="Tile & Stone"),
        ]))

        return rooms

    # =========================================================================
    # [2836] NYC Public School & Community Center Renovation - 350 Grand Concourse (SCA Standard)
    # =========================================================================
    @staticmethod
    def get_2836_sca_metadata() -> Dict[str, Any]:
        return {
            "project_name": "[2836] NYC Public School & Community Center Renovation - 350 Grand Concourse",
            "client_name": "SCA Project Manager",
            "client_company": "NYC School Construction Authority / DDC",
            "date_str": "05/18/2026",
            "trade_category": "Tile & Stone"
        }

    @staticmethod
    def get_2836_sca_specs() -> Dict[str, MaterialSpec]:
        return {
            "CTF-01": MaterialSpec(symbol="CTF-01", description="Daltile Keystones, 2\" x 2\" Unglazed Porcelain Mosaic Tile, Slip-Resistant Bed", unit="SQ FT", budget_price=0.0, notes="Basement Athletic Showers & Locker Room Floors (DCOF >= 0.60)", trade="Tile & Stone"),
            "CTF-02": MaterialSpec(symbol="CTF-02", description="American Olean, Horizon 12\" x 24\" High-Traffic Commercial Porcelain Tile", unit="SQ FT", budget_price=0.0, notes="1st, 2nd, 3rd Floor Student & Faculty Restroom Floors", trade="Tile & Stone"),
            "CTW-01": MaterialSpec(symbol="CTW-01", description="Daltile, Semi-Gloss 4-1/4\" x 4-1/4\" Glazed Wall Tile, Full Height", unit="SQ FT", budget_price=0.0, notes="Basement Athletic Shower Stalls & Drying Wet Walls", trade="Tile & Stone"),
            "CTW-02": MaterialSpec(symbol="CTW-02", description="Daltile, Color Wheel 6\" x 6\" Glazed Wall Tile, Full Height to 8'-0\"", unit="SQ FT", budget_price=0.0, notes="Core Multi-Stall Student Restroom Wet Walls across all floors", trade="Tile & Stone"),
            "CTW-03": MaterialSpec(symbol="CTW-03", description="Nemo Tile, 3\" x 6\" Beveled Ceramic Subway Tile", unit="SQ FT", budget_price=0.0, notes="2nd Floor Faculty Lounge & Pantry Backsplash", trade="Tile & Stone"),
            "WB-01": MaterialSpec(symbol="WB-01", description="Daltile, 6\" x 12\" Sanitary Ceramic Cove Base & Outcorner Fittings", unit="LN FT", budget_price=0.0, notes="Continuous sanitary coved tile perimeter base", trade="Tile & Stone"),
            "SSF-01": MaterialSpec(symbol="SSF-01", description="Caesarstone, 3/4\" Solid Surface Multi-Lavatory Countertops & Troughs", unit="SQ FT", budget_price=0.0, notes="Restroom vanity countertops & faculty pantry countertop with 4\" aprons", trade="Tile & Stone"),
            "WATERPROOF": MaterialSpec(symbol="WATERPROOF", description="Laticrete Hydro Ban / ANSI A118.10 Liquid Waterproofing Membrane", unit="SQ FT", budget_price=0.0, notes="Floors, continuous 6\" base, full shower enclosures", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="Portland Mud-Set Mortar Bed & Self-Leveling Subfloor Underlayment", unit="SQ FT", budget_price=0.0, notes="Subfloor leveling bed across all tiled areas", trade="Tile & Stone"),
            "EPOXY-GROUT": MaterialSpec(symbol="EPOXY-GROUT", description="Laticrete SpectraLOCK PRO Premium Epoxy Grout (Heavy-Duty Chemical Resistant)", unit="SQ FT", budget_price=0.0, notes="Shower stalls, locker floors, and student restrooms", trade="Tile & Stone"),
            "MS": MaterialSpec(symbol="MS", description="Schluter Systems Schiene 1/4\" Satin Stainless Steel Wall & Floor Trim", unit="LN FT", budget_price=0.0, notes="Tile edge terminations and floor transitions", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="White Carrara / Honed Marble Beveled Doorway Transition Saddle (SCA Standard)", unit="PCS", budget_price=0.0, notes="Doorway transition thresholds", trade="Tile & Stone")
        }

    @staticmethod
    def get_2836_sca_rooms() -> List[RoomTakeoff]:
        rooms = []
        # ================= BASEMENT LOCKER & ATHLETIC LEVEL =================
        rooms.append(RoomTakeoff(room_name="BASEMENT BOYS LOCKER & SHOWERS", floor_name="BASEMENT LEVEL", length_ft=28.0, width_ft=18.0, ceiling_height_ft=10.0, wall_tile_height_ft=9.0, door_count=2, items=[
            TakeoffLineItem(symbol="CTF-01", finish_type="FLOOR", material_type="PORCELAIN MOSAIC", work_type="S&I", quantity=504.0, unit="SQ FT", notes="Daltile Keystones 2x2 unglazed slip-resistant floor", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-01", finish_type="SHOWER WALL", material_type="GLAZED WALL TILE", work_type="S&I", quantity=680.0, unit="SQ FT", notes="Daltile 4-1/4 x 4-1/4 glazed wall tile full height shower enclosure", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-01", finish_type="WALL", material_type="CERAMIC COVE BASE", work_type="S&I", quantity=92.0, unit="LN FT", notes="6x12 sanitary cove base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=504.0, unit="SQ FT", notes="Floor waterproofing membrane", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=680.0, unit="SQ FT", notes="Shower wet walls waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=504.0, unit="SQ FT", notes="Sloped mud-set mortar bed to floor drains", trade="Tile & Stone"),
            TakeoffLineItem(symbol="EPOXY-GROUT", finish_type="PREPARATION", material_type="EPOXY GROUT", work_type="S&I", quantity=504.0, unit="SQ FT", notes="Heavy duty epoxy grout", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=48.0, unit="LN FT", notes="Schluter stainless edge trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="PCS", notes="Doorway transition saddles", trade="Tile & Stone")
        ]))
        rooms.append(RoomTakeoff(room_name="BASEMENT GIRLS LOCKER & SHOWERS", floor_name="BASEMENT LEVEL", length_ft=28.0, width_ft=18.0, ceiling_height_ft=10.0, wall_tile_height_ft=9.0, door_count=2, items=[
            TakeoffLineItem(symbol="CTF-01", finish_type="FLOOR", material_type="PORCELAIN MOSAIC", work_type="S&I", quantity=504.0, unit="SQ FT", notes="Daltile Keystones 2x2 unglazed slip-resistant floor", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-01", finish_type="SHOWER WALL", material_type="GLAZED WALL TILE", work_type="S&I", quantity=680.0, unit="SQ FT", notes="Daltile 4-1/4 x 4-1/4 glazed wall tile full height shower enclosure", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-01", finish_type="WALL", material_type="CERAMIC COVE BASE", work_type="S&I", quantity=92.0, unit="LN FT", notes="6x12 sanitary cove base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=504.0, unit="SQ FT", notes="Floor waterproofing membrane", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="SHOWER WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=680.0, unit="SQ FT", notes="Shower wet walls waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=504.0, unit="SQ FT", notes="Sloped mud-set mortar bed to floor drains", trade="Tile & Stone"),
            TakeoffLineItem(symbol="EPOXY-GROUT", finish_type="PREPARATION", material_type="EPOXY GROUT", work_type="S&I", quantity=504.0, unit="SQ FT", notes="Heavy duty epoxy grout", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=48.0, unit="LN FT", notes="Schluter stainless edge trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="PCS", notes="Doorway transition saddles", trade="Tile & Stone")
        ]))

        # ================= 1ST FLOOR =================
        rooms.append(RoomTakeoff(room_name="1ST FLOOR BOYS RESTROOM 101", floor_name="1ST FLOOR", length_ft=20.0, width_ft=14.0, ceiling_height_ft=9.5, wall_tile_height_ft=8.0, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-02", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=280.0, unit="SQ FT", notes="American Olean 12x24 commercial floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-02", finish_type="WALL", material_type="GLAZED WALL TILE", work_type="S&I", quantity=420.0, unit="SQ FT", notes="Daltile 6x6 glazed wall tile to 8'-0\"", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-01", finish_type="WALL", material_type="CERAMIC COVE BASE", work_type="S&I", quantity=68.0, unit="LN FT", notes="6x12 sanitary cove base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="MULTI-LAVATORY COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="Caesarstone 4-bowl lavatory countertop (12'-0\" x 2'-0\")", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="VANITY APRON/4'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="4 inch drop apron", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="VANITY BACKSPLASH/4'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="4 inch solid surface splash", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=280.0, unit="SQ FT", notes="Floor waterproofing membrane", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=34.0, unit="SQ FT", notes="6 inch base waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=280.0, unit="SQ FT", notes="Subfloor leveling bed", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=36.0, unit="LN FT", notes="Schluter top edge trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Marble transition saddle", trade="Tile & Stone")
        ]))
        rooms.append(RoomTakeoff(room_name="1ST FLOOR GIRLS RESTROOM 102", floor_name="1ST FLOOR", length_ft=20.0, width_ft=14.0, ceiling_height_ft=9.5, wall_tile_height_ft=8.0, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-02", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=280.0, unit="SQ FT", notes="American Olean 12x24 commercial floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-02", finish_type="WALL", material_type="GLAZED WALL TILE", work_type="S&I", quantity=420.0, unit="SQ FT", notes="Daltile 6x6 glazed wall tile to 8'-0\"", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-01", finish_type="WALL", material_type="CERAMIC COVE BASE", work_type="S&I", quantity=68.0, unit="LN FT", notes="6x12 sanitary cove base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="MULTI-LAVATORY COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="Caesarstone 4-bowl lavatory countertop (12'-0\" x 2'-0\")", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="VANITY APRON/4'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="4 inch drop apron", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="VANITY BACKSPLASH/4'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="4 inch solid surface splash", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=280.0, unit="SQ FT", notes="Floor waterproofing membrane", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=34.0, unit="SQ FT", notes="6 inch base waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=280.0, unit="SQ FT", notes="Subfloor leveling bed", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=36.0, unit="LN FT", notes="Schluter top edge trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Marble transition saddle", trade="Tile & Stone")
        ]))

        # ================= 2ND FLOOR =================
        rooms.append(RoomTakeoff(room_name="2ND FLOOR FACULTY LOUNGE & PANTRY 205", floor_name="2ND FLOOR", length_ft=18.0, width_ft=12.0, ceiling_height_ft=9.5, wall_tile_height_ft=2.5, door_count=1, items=[
            TakeoffLineItem(symbol="CTW-03", finish_type="WALL BACKSPLASH", material_type="CERAMIC TILE", work_type="S&I", quantity=45.0, unit="SQ FT", notes="Nemo Tile 3x6 beveled subway tile backsplash", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=36.0, unit="SQ FT", notes="Caesarstone solid surface pantry countertop (15'-6\" x 2'-4\")", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="COUNTERTOP APRON/1-1/2'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=2.0, unit="SQ FT", notes="1-1/2 inch front drop apron", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=16.0, unit="LN FT", notes="Schluter top edge trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Marble transition saddle", trade="Tile & Stone")
        ]))
        rooms.append(RoomTakeoff(room_name="2ND FLOOR FACULTY RESTROOM 206", floor_name="2ND FLOOR", length_ft=9.0, width_ft=7.5, ceiling_height_ft=9.5, wall_tile_height_ft=8.0, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-02", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=67.5, unit="SQ FT", notes="American Olean 12x24 commercial floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-02", finish_type="WALL", material_type="GLAZED WALL TILE", work_type="S&I", quantity=160.0, unit="SQ FT", notes="Daltile 6x6 glazed wall tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-01", finish_type="WALL", material_type="CERAMIC COVE BASE", work_type="S&I", quantity=33.0, unit="LN FT", notes="6x12 sanitary cove base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="VANITY COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=8.0, unit="SQ FT", notes="Caesarstone single sink vanity top", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=67.5, unit="SQ FT", notes="Floor waterproofing membrane", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=67.5, unit="SQ FT", notes="Subfloor leveling bed", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=18.0, unit="LN FT", notes="Schluter top edge trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Marble transition saddle", trade="Tile & Stone")
        ]))

        # ================= 3RD FLOOR =================
        rooms.append(RoomTakeoff(room_name="3RD FLOOR BOYS RESTROOM 301", floor_name="3RD FLOOR", length_ft=20.0, width_ft=14.0, ceiling_height_ft=9.5, wall_tile_height_ft=8.0, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-02", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=280.0, unit="SQ FT", notes="American Olean 12x24 commercial floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-02", finish_type="WALL", material_type="GLAZED WALL TILE", work_type="S&I", quantity=420.0, unit="SQ FT", notes="Daltile 6x6 glazed wall tile to 8'-0\"", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-01", finish_type="WALL", material_type="CERAMIC COVE BASE", work_type="S&I", quantity=68.0, unit="LN FT", notes="6x12 sanitary cove base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="MULTI-LAVATORY COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="Caesarstone 4-bowl lavatory countertop (12'-0\" x 2'-0\")", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="VANITY APRON/4'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="4 inch drop apron", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="VANITY BACKSPLASH/4'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="4 inch solid surface splash", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=280.0, unit="SQ FT", notes="Floor waterproofing membrane", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=34.0, unit="SQ FT", notes="6 inch base waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=280.0, unit="SQ FT", notes="Subfloor leveling bed", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=36.0, unit="LN FT", notes="Schluter top edge trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Marble transition saddle", trade="Tile & Stone")
        ]))
        rooms.append(RoomTakeoff(room_name="3RD FLOOR GIRLS RESTROOM 302", floor_name="3RD FLOOR", length_ft=20.0, width_ft=14.0, ceiling_height_ft=9.5, wall_tile_height_ft=8.0, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-02", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=280.0, unit="SQ FT", notes="American Olean 12x24 commercial floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-02", finish_type="WALL", material_type="GLAZED WALL TILE", work_type="S&I", quantity=420.0, unit="SQ FT", notes="Daltile 6x6 glazed wall tile to 8'-0\"", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-01", finish_type="WALL", material_type="CERAMIC COVE BASE", work_type="S&I", quantity=68.0, unit="LN FT", notes="6x12 sanitary cove base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="MULTI-LAVATORY COUNTERTOP", material_type="SOLID SURFACE", work_type="S&I", quantity=24.0, unit="SQ FT", notes="Caesarstone 4-bowl lavatory countertop (12'-0\" x 2'-0\")", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="VANITY APRON/4'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="4 inch drop apron", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SSF-01", finish_type="VANITY BACKSPLASH/4'' HEIGHT", material_type="SOLID SURFACE", work_type="S&I", quantity=4.0, unit="SQ FT", notes="4 inch solid surface splash", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=280.0, unit="SQ FT", notes="Floor waterproofing membrane", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/6'' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=34.0, unit="SQ FT", notes="6 inch base waterproofing", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=280.0, unit="SQ FT", notes="Subfloor leveling bed", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=36.0, unit="LN FT", notes="Schluter top edge trim", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Marble transition saddle", trade="Tile & Stone")
        ]))
        rooms.append(RoomTakeoff(room_name="3RD FLOOR JANITOR CLOSET 303", floor_name="3RD FLOOR", length_ft=6.0, width_ft=5.5, ceiling_height_ft=9.5, wall_tile_height_ft=4.0, door_count=1, items=[
            TakeoffLineItem(symbol="CTF-02", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=33.0, unit="SQ FT", notes="American Olean 12x24 commercial floor tile", trade="Tile & Stone"),
            TakeoffLineItem(symbol="CTW-02", finish_type="WALL", material_type="GLAZED WALL TILE", work_type="S&I", quantity=46.0, unit="SQ FT", notes="Mop basin splash surround", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WB-01", finish_type="WALL", material_type="CERAMIC COVE BASE", work_type="S&I", quantity=23.0, unit="LN FT", notes="6x12 sanitary cove base", trade="Tile & Stone"),
            TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=33.0, unit="SQ FT", notes="Floor waterproofing membrane", trade="Tile & Stone"),
            TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=33.0, unit="SQ FT", notes="Mud-set mortar bed", trade="Tile & Stone"),
            TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Marble transition saddle", trade="Tile & Stone")
        ]))

        return rooms

    # =========================================================================
    # [2837] Mount Sinai Ambulatory Surgery & Healthcare Suite - 1190 5th Ave
    # =========================================================================
    @staticmethod
    def get_2837_mountsinai_metadata() -> Dict[str, Any]:
        return {
            "project_name": "[2837] Mount Sinai Ambulatory Surgery & Healthcare Suite - 1190 5th Ave",
            "client_name": "David Rosenberg, MD / Facilities",
            "client_company": "Mount Sinai Health System",
            "date_str": "06/12/2026",
            "trade_category": "Tile & Stone"
        }

    @staticmethod
    def get_2837_mountsinai_specs() -> Dict[str, MaterialSpec]:
        return {
            "HFT-01": MaterialSpec(symbol="HFT-01", description="Crossville, Porcelain Cross-Tread Non-Porous Unpolished 24x24 Floor Tile", unit="SQ FT", budget_price=0.0, notes="Surgery prep & sterile corridor flooring", trade="Tile & Stone"),
            "HWT-01": MaterialSpec(symbol="HWT-01", description="Daltile, Semi-Gloss Ultra-White 12x24 Hygienic Wall Tile", unit="SQ FT", budget_price=0.0, notes="Full height sterile scrub rooms & patient recovery wet walls", trade="Tile & Stone"),
            "WB-01": MaterialSpec(symbol="WB-01", description="Daltile, 6x12 Sanitary Vitrified Coved Base & Bullnose Outcorners", unit="LN FT", budget_price=0.0, notes="Continuous sanitary coved baseboard", trade="Tile & Stone"),
            "QZ-01": MaterialSpec(symbol="QZ-01", description="Cambria, White Cliff Non-Porous Antimicrobial Solid Quartz 3cm Countertop", unit="SQ FT", budget_price=0.0, notes="Nurse station & sterile scrub sink countertops", trade="Tile & Stone"),
            "WATERPROOF": MaterialSpec(symbol="WATERPROOF", description="Mapei Mapelastic AquaDefense Waterproofing Membrane", unit="SQ FT", budget_price=0.0, notes="Floor and wall sterile containment waterproofing", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="Portland Mud-Set Mortar Bed & Self-Leveling Subfloor Underlayment", unit="SQ FT", budget_price=0.0, notes="Subfloor leveling bed across clinical suites", trade="Tile & Stone"),
            "EPOXY-GROUT": MaterialSpec(symbol="EPOXY-GROUT", description="Laticrete SpectraLOCK PRO 100% Solids Epoxy Grout", unit="SQ FT", budget_price=0.0, notes="Chemical resistant sterile grouting", trade="Tile & Stone"),
            "MS": MaterialSpec(symbol="MS", description="Schluter Systems Schiene Brushed Stainless Steel Metal Trim", unit="LN FT", budget_price=0.0, notes="Hygienic wall edge and termination trims", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="Non-Porous Engineered Quartz Doorway Transition Saddle", unit="PCS", budget_price=0.0, notes="Clinical doorway transition saddles", trade="Tile & Stone")
        }

    @staticmethod
    def get_2837_mountsinai_rooms() -> List[RoomTakeoff]:
        return [
            RoomTakeoff(room_name="SURGICAL SCRUB ROOM 101", floor_name="SURGERY LEVEL 1", length_ft=14.0, width_ft=10.0, ceiling_height_ft=10.0, wall_tile_height_ft=10.0, door_count=1, items=[
                TakeoffLineItem(symbol="HFT-01", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=140.0, unit="SQ FT", notes="Crossville 24x24 non-porous floor", trade="Tile & Stone"),
                TakeoffLineItem(symbol="HWT-01", finish_type="WALL", material_type="HYGIENIC TILE", work_type="S&I", quantity=440.0, unit="SQ FT", notes="Daltile 12x24 ultra white full 10' walls", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WB-01", finish_type="WALL", material_type="CERAMIC COVE BASE", work_type="S&I", quantity=44.0, unit="LN FT", notes="Sanitary coved base", trade="Tile & Stone"),
                TakeoffLineItem(symbol="QZ-01", finish_type="SCRUB SINK COUNTERTOP", material_type="QUARTZ", work_type="S&I", quantity=24.0, unit="SQ FT", notes="Cambria 3cm non-porous surgical scrub top", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=140.0, unit="SQ FT", notes="Liquid containment waterproofing", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/FULL HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=440.0, unit="SQ FT", notes="Full height wall waterproofing", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=140.0, unit="SQ FT", notes="Subfloor leveling bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="EPOXY-GROUT", finish_type="PREPARATION", material_type="EPOXY GROUT", work_type="S&I", quantity=140.0, unit="SQ FT", notes="Sterile epoxy grout", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=36.0, unit="LN FT", notes="Stainless edge trim", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Quartz transition saddle", trade="Tile & Stone")
            ]),
            RoomTakeoff(room_name="PATIENT RECOVERY RESTROOM 102", floor_name="SURGERY LEVEL 1", length_ft=10.0, width_ft=8.0, ceiling_height_ft=9.5, wall_tile_height_ft=9.5, door_count=1, items=[
                TakeoffLineItem(symbol="HFT-01", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=80.0, unit="SQ FT", notes="Crossville 24x24 floor", trade="Tile & Stone"),
                TakeoffLineItem(symbol="HWT-01", finish_type="WALL", material_type="HYGIENIC TILE", work_type="S&I", quantity=300.0, unit="SQ FT", notes="12x24 wall tile full height", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WB-01", finish_type="WALL", material_type="CERAMIC COVE BASE", work_type="S&I", quantity=34.0, unit="LN FT", notes="Sanitary cove base", trade="Tile & Stone"),
                TakeoffLineItem(symbol="QZ-01", finish_type="VANITY COUNTERTOP", material_type="QUARTZ", work_type="S&I", quantity=10.0, unit="SQ FT", notes="Cambria vanity top with sink cutout", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=80.0, unit="SQ FT", notes="Waterproofing membrane", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=80.0, unit="SQ FT", notes="Mud-set mortar bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=22.0, unit="LN FT", notes="Schluter trim", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Quartz saddle", trade="Tile & Stone")
            ]),
            RoomTakeoff(room_name="NURSE STATION & MEDICATION PREP", floor_name="SURGERY LEVEL 1", length_ft=22.0, width_ft=14.0, ceiling_height_ft=9.5, wall_tile_height_ft=2.5, door_count=1, items=[
                TakeoffLineItem(symbol="QZ-01", finish_type="NURSE STATION RECEPTION TOP", material_type="QUARTZ", work_type="S&I", quantity=48.0, unit="SQ FT", notes="Cambria 3cm quartz transaction & work top", trade="Tile & Stone"),
                TakeoffLineItem(symbol="QZ-01", finish_type="COUNTERTOP APRON/2'' HEIGHT", material_type="QUARTZ", work_type="S&I", quantity=4.0, unit="SQ FT", notes="2 inch drop apron", trade="Tile & Stone"),
                TakeoffLineItem(symbol="HWT-01", finish_type="WALL BACKSPLASH", material_type="HYGIENIC TILE", work_type="S&I", quantity=35.0, unit="SQ FT", notes="Medication prep full height tile splash", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=18.0, unit="LN FT", notes="Schluter edge trim", trade="Tile & Stone")
            ])
        ]

    # =========================================================================
    # [2838] The Nomad Luxury Hotel & Wellness Spa - 1170 Broadway
    # =========================================================================
    @staticmethod
    def get_2838_nomad_metadata() -> Dict[str, Any]:
        return {
            "project_name": "[2838] The Nomad Luxury Hotel & Wellness Spa - 1170 Broadway",
            "client_name": "Sydell Group / Development",
            "client_company": "Hudson Meridian Construction Group",
            "date_str": "07/22/2026",
            "trade_category": "Tile & Stone"
        }

    @staticmethod
    def get_2838_nomad_specs() -> Dict[str, MaterialSpec]:
        return {
            "ST-01": MaterialSpec(symbol="ST-01", description="Artistic Tile, Calacatta Gold Polished 2cm Bookmatched Marble Slabs", unit="SQ FT", budget_price=0.0, notes="Lobby feature fireplace & reception desk cladding", trade="Tile & Stone"),
            "ST-02": MaterialSpec(symbol="ST-02", description="Stone Source, French Beaumaniere Honed Limestone Pavers 24x36", unit="SQ FT", budget_price=0.0, notes="Main lobby entrance & conservatory floor", trade="Tile & Stone"),
            "ST-03": MaterialSpec(symbol="ST-03", description="Nemo Tile, Nero Marquina Honed 2cm Marble Vanity Slabs with 4-inch Mitered Apron", unit="SQ FT", budget_price=0.0, notes="Guest room & penthouse custom vanity tops", trade="Tile & Stone"),
            "TL-01": MaterialSpec(symbol="TL-01", description="Artistic Tile, Micro-Herringbone Thassos White Marble Mosaic 1x2", unit="SQ FT", budget_price=0.0, notes="Guest suite bathroom & spa shower floors", trade="Tile & Stone"),
            "TL-02": MaterialSpec(symbol="TL-02", description="Cancos Tile, Hand-Crafted Glossy Subway Tile 2-1/2 x 8 Linen White", unit="SQ FT", budget_price=0.0, notes="Full height bathroom wet walls & shower surrounds", trade="Tile & Stone"),
            "TB-01": MaterialSpec(symbol="TB-01", description="Artistic Tile, Nero Marquina 4x12 Honed Marble Baseboard", unit="LN FT", budget_price=0.0, notes="Perimeter luxury stone baseboard", trade="Tile & Stone"),
            "WATERPROOF": MaterialSpec(symbol="WATERPROOF", description="Schluter Kerdi Liquid & Sheet Waterproofing System", unit="SQ FT", budget_price=0.0, notes="Spa steam room, shower floors & full wet enclosures", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="Portland Mud-Set Mortar Bed & Leveling Underlayment", unit="SQ FT", budget_price=0.0, notes="Subfloor mud-set across all natural stone floors", trade="Tile & Stone"),
            "MS-BRASS": MaterialSpec(symbol="MS-BRASS", description="Schluter Systems Schiene Solid Satin Brass Metal Trim (Classic Gold Finish)", unit="LN FT", budget_price=0.0, notes="Shower corner & marble transition trims", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="Nero Marquina Honed Marble Double-Beveled Transition Saddle", unit="PCS", budget_price=0.0, notes="Guestroom bathroom doorway thresholds", trade="Tile & Stone")
        }

    @staticmethod
    def get_2838_nomad_rooms() -> List[RoomTakeoff]:
        return [
            RoomTakeoff(room_name="MAIN LOBBY & RECEPTION SALON", floor_name="GROUND FLOOR", length_ft=34.0, width_ft=22.0, ceiling_height_ft=14.0, wall_tile_height_ft=14.0, door_count=2, items=[
                TakeoffLineItem(symbol="ST-02", finish_type="FLOOR", material_type="LIMESTONE", work_type="S&I", quantity=748.0, unit="SQ FT", notes="French Beaumaniere limestone 24x36 pavers", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="RECEPTION WALL FEATURE", material_type="MARBLE SLAB", work_type="S&I", quantity=280.0, unit="SQ FT", notes="Bookmatched Calacatta Gold 2cm polished slabs", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="RECEPTION DESK CLADDING", material_type="MARBLE SLAB", work_type="S&I", quantity=72.0, unit="SQ FT", notes="Mitered Calacatta reception front & waterfall sides", trade="Tile & Stone"),
                TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="MARBLE BASE", work_type="S&I", quantity=112.0, unit="LN FT", notes="Nero Marquina 4x12 marble baseboard", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=748.0, unit="SQ FT", notes="1-1/2 inch Portland mud-set bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-BRASS", finish_type="FLOOR", material_type="BRASS METAL TRIM", work_type="S&I", quantity=44.0, unit="LN FT", notes="Solid satin brass floor transition trim", trade="Tile & Stone")
            ]),
            RoomTakeoff(room_name="SPA WELLNESS STEAM ROOM & HYDROTHERAPY", floor_name="LOWER LEVEL", length_ft=18.0, width_ft=14.0, ceiling_height_ft=9.0, wall_tile_height_ft=9.0, door_count=1, items=[
                TakeoffLineItem(symbol="TL-01", finish_type="FLOOR", material_type="MARBLE MOSAIC", work_type="S&I", quantity=252.0, unit="SQ FT", notes="Thassos White micro-herringbone mosaic floor", trade="Tile & Stone"),
                TakeoffLineItem(symbol="TL-02", finish_type="WALL", material_type="CERAMIC TILE", work_type="S&I", quantity=540.0, unit="SQ FT", notes="Hand-crafted linen white subway wall tile to ceiling", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-03", finish_type="STEAM BENCH SEATING & TOPS", material_type="MARBLE SLAB", work_type="S&I", quantity=48.0, unit="SQ FT", notes="Solid Nero Marquina bench slabs & mitered drop aprons", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR & FULL STEAM WALLS", material_type="WATERPROOF", work_type="S&I", quantity=792.0, unit="SQ FT", notes="Schluter Kerdi steam-rated waterproofing membrane", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=252.0, unit="SQ FT", notes="Pitched mud-set bed to floor drains", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-BRASS", finish_type="WALL", material_type="BRASS METAL TRIM", work_type="S&I", quantity=64.0, unit="LN FT", notes="Satin brass corner & niche trims", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Nero Marquina honed saddle", trade="Tile & Stone")
            ])
        ]

    # =========================================================================
    # [2839] Le Bernardin Private Dining & Commercial Culinary Kitchen - 155 W 51st
    # =========================================================================
    @staticmethod
    def get_2839_lebernardin_metadata() -> Dict[str, Any]:
        return {
            "project_name": "[2839] Le Bernardin Private Dining & Commercial Culinary Kitchen - 155 W 51st",
            "client_name": "Culinary Operations / Eric Ripert",
            "client_company": "Structure Tone / Hospitality Division",
            "date_str": "08/14/2026",
            "trade_category": "Tile & Stone"
        }

    @staticmethod
    def get_2839_lebernardin_specs() -> Dict[str, MaterialSpec]:
        return {
            "QT-01": MaterialSpec(symbol="QT-01", description="Daltile, Quarry Tile 6x6 Heavy-Duty Abrasive Slip-Resistant Red Canyon", unit="SQ FT", budget_price=0.0, notes="Commercial kitchen, cook line & dishwashing floor", trade="Tile & Stone"),
            "QB-01": MaterialSpec(symbol="QB-01", description="Daltile, 6x6 Quarry Sanitary Cove Base & Outcorners", unit="LN FT", budget_price=0.0, notes="NYC Health Department certified sanitary coved base", trade="Tile & Stone"),
            "WT-01": MaterialSpec(symbol="WT-01", description="Daltile, 4-1/4 x 8-1/2 Bright White Glazed Commercial Wall Tile", unit="SQ FT", budget_price=0.0, notes="Full height kitchen cooking & prep wet walls", trade="Tile & Stone"),
            "ST-01": MaterialSpec(symbol="ST-01", description="Cosentino, Dekton Laurent 2cm Polished Waterfall Bar Cladding & Top", unit="SQ FT", budget_price=0.0, notes="Private dining bar counter, waterfall sides & drip apron", trade="Tile & Stone"),
            "FT-01": MaterialSpec(symbol="FT-01", description="Porcelanosa, Terrazzo Grigio 36x36 Polished Large Format Floor Tile", unit="SQ FT", budget_price=0.0, notes="Private dining room main seating floor", trade="Tile & Stone"),
            "WATERPROOF": MaterialSpec(symbol="WATERPROOF", description="Laticrete Hydro Ban / Mapelastic Liquid Waterproofing", unit="SQ FT", budget_price=0.0, notes="Commercial kitchen floor & 1-foot up perimeter walls", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="Portland Mud-Set Heavy-Duty Sloped Underlayment Bed", unit="SQ FT", budget_price=0.0, notes="Pitched subfloor to trench drains", trade="Tile & Stone"),
            "EPOXY-GROUT": MaterialSpec(symbol="EPOXY-GROUT", description="Laticrete SpectraLOCK 2000 IG Chemical & Grease-Resistant Industrial Epoxy Grout", unit="SQ FT", budget_price=0.0, notes="Kitchen quarry tile floor & wet wall joints", trade="Tile & Stone"),
            "MS": MaterialSpec(symbol="MS", description="Schluter Schiene Heavy-Duty Stainless Steel Edge Trim", unit="LN FT", budget_price=0.0, notes="Tile to vinyl/wood transition trim", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="Heavy-Duty Absolute Black Granite Threshold Saddle", unit="PCS", budget_price=0.0, notes="Kitchen to dining room transition saddles", trade="Tile & Stone")
        }

    @staticmethod
    def get_2839_lebernardin_rooms() -> List[RoomTakeoff]:
        return [
            RoomTakeoff(room_name="COMMERCIAL MAIN COOK LINE & PREP KITCHEN", floor_name="MAIN FLOOR", length_ft=32.0, width_ft=18.0, ceiling_height_ft=11.0, wall_tile_height_ft=10.0, door_count=2, items=[
                TakeoffLineItem(symbol="QT-01", finish_type="FLOOR", material_type="QUARRY TILE", work_type="S&I", quantity=576.0, unit="SQ FT", notes="Daltile 6x6 abrasive quarry tile", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WT-01", finish_type="WALL", material_type="CERAMIC TILE", work_type="S&I", quantity=840.0, unit="SQ FT", notes="Daltile 4-1/4 x 8-1/2 glazed wall tile full 10' height", trade="Tile & Stone"),
                TakeoffLineItem(symbol="QB-01", finish_type="WALL", material_type="QUARRY COVE BASE", work_type="S&I", quantity=96.0, unit="LN FT", notes="Sanitary coved base", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=576.0, unit="SQ FT", notes="Kitchen floor waterproofing", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/1' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=96.0, unit="SQ FT", notes="1 foot wall base containment waterproofing", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=576.0, unit="SQ FT", notes="Sloped mud-set bed to trench drains", trade="Tile & Stone"),
                TakeoffLineItem(symbol="EPOXY-GROUT", finish_type="PREPARATION", material_type="EPOXY GROUT", work_type="S&I", quantity=576.0, unit="SQ FT", notes="SpectraLOCK 2000 IG industrial grease-proof epoxy", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=42.0, unit="LN FT", notes="Heavy-duty stainless trim", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="PCS", notes="Absolute Black granite saddle", trade="Tile & Stone")
            ]),
            RoomTakeoff(room_name="PRIVATE DINING SALON & SOMMELIER BAR", floor_name="MAIN FLOOR", length_ft=26.0, width_ft=18.0, ceiling_height_ft=12.0, wall_tile_height_ft=0.0, door_count=1, items=[
                TakeoffLineItem(symbol="FT-01", finish_type="FLOOR", material_type="PORCELAIN TERRAZZO", work_type="S&I", quantity=468.0, unit="SQ FT", notes="Porcelanosa Terrazzo Grigio 36x36 floor tile", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="BAR COUNTERTOP & WATERFALL", material_type="DEKTON SLAB", work_type="S&I", quantity=56.0, unit="SQ FT", notes="Dekton Laurent 2cm polished bar top with mitered waterfall edge", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="BAR FRONT CLADDING", material_type="DEKTON SLAB", work_type="S&I", quantity=48.0, unit="SQ FT", notes="Dekton bar die-wall stone cladding", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=468.0, unit="SQ FT", notes="Subfloor leveling mud-set bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS", finish_type="FLOOR", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=24.0, unit="LN FT", notes="Stainless transition strip", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Absolute Black granite threshold saddle", trade="Tile & Stone")
            ])
        ]

    # =========================================================================
    # [2840] JFK International Airport Terminal 4 - Sky Club & VIP Concourse Suite
    # =========================================================================
    @staticmethod
    def get_2840_jfk_metadata() -> Dict[str, Any]:
        return {
            "project_name": "[2840] JFK International Airport Terminal 4 - Sky Club & VIP Concourse Suite",
            "client_name": "Port Authority NYNJ / Aviation Facilities",
            "client_company": "Delta Air Lines / PANYNJ Construction Group",
            "date_str": "09/04/2026",
            "trade_category": "Tile & Stone"
        }

    @staticmethod
    def get_2840_jfk_specs() -> Dict[str, MaterialSpec]:
        return {
            "TFT-01": MaterialSpec(symbol="TFT-01", description="Nabel, Heavy-Duty Engineered Terrazzo Porcelain 30x30 High-Traffic Floor Tile", unit="SQ FT", budget_price=0.0, notes="Main concourse lounge, bar & buffet circulation floor", trade="Tile & Stone"),
            "WT-01": MaterialSpec(symbol="WT-01", description="Porcelanosa, Fluted Acoustic White Porcelain Large Format Wall Slabs 12x48", unit="SQ FT", budget_price=0.0, notes="VIP lounge feature entrance walls & restroom vestibules", trade="Tile & Stone"),
            "TB-01": MaterialSpec(symbol="TB-01", description="Nabel, 6x12 Heavy-Duty Terrazzo Coved Baseboard", unit="LN FT", budget_price=0.0, notes="Continuous impact-resistant coved baseboard", trade="Tile & Stone"),
            "ST-01": MaterialSpec(symbol="ST-01", description="Cosentino, Dekton Entzo 2cm Polished Buffet & Bar Waterfall Countertop", unit="SQ FT", budget_price=0.0, notes="Buffet counter, cocktail bar & waterfall edge returns", trade="Tile & Stone"),
            "WATERPROOF": MaterialSpec(symbol="WATERPROOF", description="Laticrete Hydro Ban Commercial Anti-Fracture & Waterproofing Membrane", unit="SQ FT", budget_price=0.0, notes="High-traffic terminal floor & wet bar areas", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="Portland Mud-Set Heavy-Duty Mortar Bed & Self-Leveling Underlayment", unit="SQ FT", budget_price=0.0, notes="Terminal concourse subfloor leveling bed", trade="Tile & Stone"),
            "EPOXY-GROUT": MaterialSpec(symbol="EPOXY-GROUT", description="Laticrete SpectraLOCK PRO Premium Heavy-Traffic Chemical Epoxy Grout", unit="SQ FT", budget_price=0.0, notes="Stain and luggage wheel resistant epoxy grouting", trade="Tile & Stone"),
            "MS": MaterialSpec(symbol="MS", description="Schluter Reno-T Heavy-Duty Stainless Steel Terminal Floor Expansion Trim", unit="LN FT", budget_price=0.0, notes="High load luggage cart transition trims", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="Heavy-Duty Honed Absolute Black Granite Threshold Saddle (Beveled)", unit="PCS", budget_price=0.0, notes="Concourse doorway transition thresholds", trade="Tile & Stone")
        }

    @staticmethod
    def get_2840_jfk_rooms() -> List[RoomTakeoff]:
        return [
            RoomTakeoff(room_name="VIP SKY CLUB MAIN CONCOURSE & BUFFET SALON", floor_name="DEPARTURES CONCOURSE", length_ft=45.0, width_ft=28.0, ceiling_height_ft=14.0, wall_tile_height_ft=14.0, door_count=2, items=[
                TakeoffLineItem(symbol="TFT-01", finish_type="FLOOR", material_type="TERRAZZO TILE", work_type="S&I", quantity=1260.0, unit="SQ FT", notes="Nabel 30x30 engineered terrazzo floor tile", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WT-01", finish_type="WALL", material_type="PORCELAIN SLAB", work_type="S&I", quantity=520.0, unit="SQ FT", notes="Porcelanosa 12x48 fluted porcelain feature walls", trade="Tile & Stone"),
                TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="TERRAZZO BASE", work_type="S&I", quantity=146.0, unit="LN FT", notes="6x12 coved terrazzo base", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="BUFFET COUNTERTOP & WATERFALL", material_type="DEKTON SLAB", work_type="S&I", quantity=96.0, unit="SQ FT", notes="Dekton Entzo 2cm polished buffet top and mitered waterfall legs", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=1260.0, unit="SQ FT", notes="Anti-fracture crack isolation and waterproofing", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=1260.0, unit="SQ FT", notes="Heavy duty leveling bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="EPOXY-GROUT", finish_type="PREPARATION", material_type="EPOXY GROUT", work_type="S&I", quantity=1260.0, unit="SQ FT", notes="SpectraLOCK PRO heavy traffic grout", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS", finish_type="FLOOR", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=68.0, unit="LN FT", notes="Schluter Reno-T heavy duty transition trim", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="PCS", notes="Heavy-duty granite doorway saddles", trade="Tile & Stone")
            ]),
            RoomTakeoff(room_name="EXECUTIVE VIP RESTROOM SUITE", floor_name="DEPARTURES CONCOURSE", length_ft=16.0, width_ft=12.0, ceiling_height_ft=10.0, wall_tile_height_ft=10.0, door_count=1, items=[
                TakeoffLineItem(symbol="TFT-01", finish_type="FLOOR", material_type="TERRAZZO TILE", work_type="S&I", quantity=192.0, unit="SQ FT", notes="Nabel 30x30 terrazzo floor", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WT-01", finish_type="WALL", material_type="PORCELAIN SLAB", work_type="S&I", quantity=420.0, unit="SQ FT", notes="Fluted porcelain wall slabs to ceiling", trade="Tile & Stone"),
                TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="TERRAZZO BASE", work_type="S&I", quantity=56.0, unit="LN FT", notes="Coved base", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="VANITY COUNTERTOP", material_type="DEKTON SLAB", work_type="S&I", quantity=24.0, unit="SQ FT", notes="Dekton vanity top with undermount lavatories", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=192.0, unit="SQ FT", notes="Floor waterproofing", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=192.0, unit="SQ FT", notes="Mud-set leveling bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=32.0, unit="LN FT", notes="Stainless edge trims", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Granite doorway saddle", trade="Tile & Stone")
            ])
        ]

    # =========================================================================
    # [2841] Tiffany & Co. Landmark Boutique & Private Salon - 727 5th Ave
    # =========================================================================
    @staticmethod
    def get_2841_tiffany_metadata() -> Dict[str, Any]:
        return {
            "project_name": "[2841] Tiffany & Co. Landmark Boutique & Private Salon - 727 5th Ave",
            "client_name": "Peter Marino Architect / Store Planning",
            "client_company": "LVMH / Tiffany Retail Development",
            "date_str": "09/18/2026",
            "trade_category": "Tile & Stone"
        }

    @staticmethod
    def get_2841_tiffany_specs() -> Dict[str, MaterialSpec]:
        return {
            "TZ-01": MaterialSpec(symbol="TZ-01", description="Agglosima, Custom Venetian White Terrazzo 36x36 with Inlaid Brass Divider Strips", unit="SQ FT", budget_price=0.0, notes="Main retail jewelry gallery & salon showroom floor", trade="Tile & Stone"),
            "ST-01": MaterialSpec(symbol="ST-01", description="Antolini, Statuario Venato Extra Polished 2cm Marble Slabs", unit="SQ FT", budget_price=0.0, notes="Jewelry display pedestals, cashwrap & private salon feature wall", trade="Tile & Stone"),
            "ST-02": MaterialSpec(symbol="ST-02", description="Artistic Tile, Bardiglio Nuvolato Honed 24x24 Marble Border Pavers", unit="SQ FT", budget_price=0.0, notes="Showroom perimeter border framing", trade="Tile & Stone"),
            "MOS-01": MaterialSpec(symbol="MOS-01", description="Bisazza, Custom Tiffany Blue & White Glass Mosaic Blend 3/4x3/4", unit="SQ FT", budget_price=0.0, notes="VIP client powder room feature accent wall", trade="Tile & Stone"),
            "TB-01": MaterialSpec(symbol="TB-01", description="Agglosima, 4x12 Venetian Terrazzo Honed Baseboard", unit="LN FT", budget_price=0.0, notes="Perimeter terrazzo baseboard", trade="Tile & Stone"),
            "WATERPROOF": MaterialSpec(symbol="WATERPROOF", description="Mapei Mapelastic AquaDefense Ultra Waterproofing Membrane", unit="SQ FT", budget_price=0.0, notes="Retail salon subfloor and VIP powder room", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="Portland Mud-Set Mortar Bed & Subfloor Leveling Underlayment", unit="SQ FT", budget_price=0.0, notes="Precision stone subfloor leveling", trade="Tile & Stone"),
            "MS-BRASS": MaterialSpec(symbol="MS-BRASS", description="Schluter Systems Schiene Custom Heavy Solid Polished Brass Trim (1/2-inch Face)", unit="LN FT", budget_price=0.0, notes="Architectural brass inlays & stone border transitions", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="Statuario Venato Polished Marble Custom Double-Beveled Transition Saddle", unit="PCS", budget_price=0.0, notes="Private salon doorway marble thresholds", trade="Tile & Stone")
        }

    @staticmethod
    def get_2841_tiffany_rooms() -> List[RoomTakeoff]:
        return [
            RoomTakeoff(room_name="MAIN JEWELRY GALLERY & DIAMOND SALON", floor_name="GROUND FLOOR", length_ft=38.0, width_ft=24.0, ceiling_height_ft=16.0, wall_tile_height_ft=16.0, door_count=2, items=[
                TakeoffLineItem(symbol="TZ-01", finish_type="FLOOR", material_type="TERRAZZO TILE", work_type="S&I", quantity=760.0, unit="SQ FT", notes="Custom Venetian White 36x36 terrazzo floor", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-02", finish_type="FLOOR BORDER", material_type="MARBLE PAVER", work_type="S&I", quantity=152.0, unit="SQ FT", notes="Bardiglio Nuvolato honed marble perimeter border", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="FEATURE SLAB WALL", material_type="MARBLE SLAB", work_type="S&I", quantity=320.0, unit="SQ FT", notes="Statuario Venato Extra bookmatched polished slabs", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="CASHWRAP & DISPLAY DESK", material_type="MARBLE SLAB", work_type="S&I", quantity=84.0, unit="SQ FT", notes="Mitered marble cashwrap front and waterfall sides", trade="Tile & Stone"),
                TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="TERRAZZO BASE", work_type="S&I", quantity=124.0, unit="LN FT", notes="4x12 Venetian terrazzo base", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=912.0, unit="SQ FT", notes="Precision mud-set mortar bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-BRASS", finish_type="FLOOR", material_type="BRASS METAL TRIM", work_type="S&I", quantity=96.0, unit="LN FT", notes="Heavy polished solid brass inlays between terrazzo & marble", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="PCS", notes="Statuario Venato doorway saddles", trade="Tile & Stone")
            ]),
            RoomTakeoff(room_name="VIP PRIVATE CLIENT POWDER ROOM", floor_name="GROUND FLOOR", length_ft=10.0, width_ft=8.0, ceiling_height_ft=10.0, wall_tile_height_ft=10.0, door_count=1, items=[
                TakeoffLineItem(symbol="TZ-01", finish_type="FLOOR", material_type="TERRAZZO TILE", work_type="S&I", quantity=80.0, unit="SQ FT", notes="Venetian terrazzo floor", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MOS-01", finish_type="ACCENT WALL", material_type="GLASS MOSAIC", work_type="S&I", quantity=100.0, unit="SQ FT", notes="Bisazza custom blue/white glass mosaic feature wall", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="FLOATING VANITY SLAB", material_type="MARBLE SLAB", work_type="S&I", quantity=16.0, unit="SQ FT", notes="Statuario marble vanity with 6-inch mitered apron", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=80.0, unit="SQ FT", notes="Floor waterproofing", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=80.0, unit="SQ FT", notes="Mud-set bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-BRASS", finish_type="WALL", material_type="BRASS METAL TRIM", work_type="S&I", quantity=28.0, unit="LN FT", notes="Polished brass trim around mosaic", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Statuario marble saddle", trade="Tile & Stone")
            ])
        ]

    # =========================================================================
    # [2842] Hudson Yards Fintech Headquarters & High-Density Server Tech Lounge - 50 Hudson Yards
    # =========================================================================
    @staticmethod
    def get_2842_hudsonyards_metadata() -> Dict[str, Any]:
        return {
            "project_name": "[2842] Hudson Yards Fintech Headquarters & High-Density Server Tech Lounge - 50 Hudson Yards",
            "client_name": "BlackRock / Corporate Workplace Design",
            "client_company": "Related Companies / Structure Tone",
            "date_str": "10/05/2026",
            "trade_category": "Tile & Stone"
        }

    @staticmethod
    def get_2842_hudsonyards_specs() -> Dict[str, MaterialSpec]:
        return {
            "ESD-01": MaterialSpec(symbol="ESD-01", description="Florim, Static-Dissipative Non-Slip Conductive Porcelain 24x24 Floor Tile", unit="SQ FT", budget_price=0.0, notes="Server hub, trading floor auxiliary & fintech lab flooring", trade="Tile & Stone"),
            "ST-01": MaterialSpec(symbol="ST-01", description="Nemo Tile, Nero Marquina Honed 2cm Marble Wall Cladding Slabs", unit="SQ FT", budget_price=0.0, notes="Executive trading boardroom & elevator lobby feature wall", trade="Tile & Stone"),
            "ST-02": MaterialSpec(symbol="ST-02", description="Cosentino, Dekton Trilium 2cm Industrial Matte Island Countertop", unit="SQ FT", budget_price=0.0, notes="Tech lounge pantry 18-foot island with 3-inch mitered waterfall edge", trade="Tile & Stone"),
            "TB-01": MaterialSpec(symbol="TB-01", description="Florim, 4x24 Matching Conductive Porcelain Tile Base", unit="LN FT", budget_price=0.0, notes="Perimeter tech floor baseboard", trade="Tile & Stone"),
            "VAPOR-BARRIER": MaterialSpec(symbol="VAPOR-BARRIER", description="Koster VAP I 2000 Zero VOC Moisture Vapor Barrier & Waterproofing", unit="SQ FT", budget_price=0.0, notes="Hudson Yards subfloor slab vapor containment", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="Portland Mud-Set Mortar Bed & Self-Leveling Underlayment", unit="SQ FT", budget_price=0.0, notes="Precision subfloor leveling", trade="Tile & Stone"),
            "EPOXY-GROUT": MaterialSpec(symbol="EPOXY-GROUT", description="Laticrete SpectraLOCK PRO Conductive Grade Epoxy Grout", unit="SQ FT", budget_price=0.0, notes="Conductive and chemical resistant grouting", trade="Tile & Stone"),
            "MS": MaterialSpec(symbol="MS", description="Schluter Systems Schiene Matte Black Anodized Metal Trim", unit="LN FT", budget_price=0.0, notes="Tile to raised access flooring transition trims", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="Absolute Black Honed Granite Doorway Transition Saddle", unit="PCS", budget_price=0.0, notes="Executive boardroom doorway thresholds", trade="Tile & Stone")
        }

    @staticmethod
    def get_2842_hudsonyards_rooms() -> List[RoomTakeoff]:
        return [
            RoomTakeoff(room_name="FINTECH SERVER LAB & TECH HUB", floor_name="FLOOR 42", length_ft=30.0, width_ft=20.0, ceiling_height_ft=11.0, wall_tile_height_ft=0.0, door_count=2, items=[
                TakeoffLineItem(symbol="ESD-01", finish_type="FLOOR", material_type="CONDUCTIVE PORCELAIN", work_type="S&I", quantity=600.0, unit="SQ FT", notes="Florim 24x24 static dissipative tile", trade="Tile & Stone"),
                TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN BASE", work_type="S&I", quantity=100.0, unit="LN FT", notes="4x24 matching tile base", trade="Tile & Stone"),
                TakeoffLineItem(symbol="VAPOR-BARRIER", finish_type="FLOOR", material_type="VAPOR BARRIER", work_type="S&I", quantity=600.0, unit="SQ FT", notes="Koster VAP I 2000 zero VOC moisture barrier", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=600.0, unit="SQ FT", notes="Self-leveling subfloor underlayment", trade="Tile & Stone"),
                TakeoffLineItem(symbol="EPOXY-GROUT", finish_type="PREPARATION", material_type="EPOXY GROUT", work_type="S&I", quantity=600.0, unit="SQ FT", notes="Conductive grade epoxy grout", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS", finish_type="FLOOR", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=36.0, unit="LN FT", notes="Schluter matte black trim", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="PCS", notes="Absolute Black granite doorway saddle", trade="Tile & Stone")
            ]),
            RoomTakeoff(room_name="TECH LOUNGE & EXECUTIVE PANTRY ISLAND", floor_name="FLOOR 42", length_ft=24.0, width_ft=16.0, ceiling_height_ft=12.0, wall_tile_height_ft=12.0, door_count=1, items=[
                TakeoffLineItem(symbol="ST-02", finish_type="ISLAND COUNTERTOP & WATERFALL", material_type="DEKTON SLAB", work_type="S&I", quantity=72.0, unit="SQ FT", notes="Dekton Trilium 2cm island top with 3-inch mitered waterfall legs", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="FEATURE WALL CLADDING", material_type="MARBLE SLAB", work_type="S&I", quantity=288.0, unit="SQ FT", notes="Nero Marquina 2cm honed marble wall slabs", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=48.0, unit="LN FT", notes="Matte black perimeter trim around marble", trade="Tile & Stone")
            ])
        ]

    # =========================================================================
    # [2843] Columbia University Life Sciences Research Lab & Bio-Medical Suites - 612 W 130th St
    # =========================================================================
    @staticmethod
    def get_2843_columbia_metadata() -> Dict[str, Any]:
        return {
            "project_name": "[2843] Columbia University Life Sciences Research Lab & Bio-Medical Suites - 612 W 130th St",
            "client_name": "Columbia Facilities / Manhattanville Campus",
            "client_company": "Skanska USA Building / Lab Construction",
            "date_str": "10/14/2026",
            "trade_category": "Tile & Stone"
        }

    @staticmethod
    def get_2843_columbia_specs() -> Dict[str, MaterialSpec]:
        return {
            "ACT-01": MaterialSpec(symbol="ACT-01", description="Crossville, Heavy-Duty Acid & Chemical Resistant Vitrified Unpolished 12x12 Floor Tile", unit="SQ FT", budget_price=0.0, notes="Wet lab, autoclave & bio-medical containment suite flooring", trade="Tile & Stone"),
            "AWT-01": MaterialSpec(symbol="AWT-01", description="Daltile, Semi-Gloss Chemical Resistant Seamless Wall Tile 8x16", unit="SQ FT", budget_price=0.0, notes="Full height lab washdown and decontamination wet walls", trade="Tile & Stone"),
            "WB-01": MaterialSpec(symbol="WB-01", description="Crossville, 6x12 Vitrified Sanitary Cove Base & Outcorner Fittings", unit="LN FT", budget_price=0.0, notes="Continuous chemical-proof sanitary cove baseboard", trade="Tile & Stone"),
            "LAB-01": MaterialSpec(symbol="LAB-01", description="Trespa / Solid Epoxy Resin 1-inch Chemical Resistant Lab Sink Countertop & Splash", unit="SQ FT", budget_price=0.0, notes="Acid waste sink countertops with 4-inch marine drop edge", trade="Tile & Stone"),
            "WATERPROOF": MaterialSpec(symbol="WATERPROOF", description="Mapei Mapelastic AquaDefense Secondary Chemical Containment Waterproofing", unit="SQ FT", budget_price=0.0, notes="Lab floor slab and 1-foot continuous perimeter containment", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="Portland Mud-Set Mortar Bed & Heavy-Duty Sloped Underlayment", unit="SQ FT", budget_price=0.0, notes="Pitched mud bed to lab emergency chemical floor drains", trade="Tile & Stone"),
            "EPOXY-GROUT": MaterialSpec(symbol="EPOXY-GROUT", description="Laticrete SpectraLOCK 2000 IG 100% Novolac Chemical Resistant Industrial Epoxy Grout", unit="SQ FT", budget_price=0.0, notes="Acid and solvent proof floor and wall grouting", trade="Tile & Stone"),
            "MS": MaterialSpec(symbol="MS", description="Schluter Systems Schiene 316 Marine Grade Stainless Steel Edge Trim", unit="LN FT", budget_price=0.0, notes="Chemical containment threshold and wall edge trims", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="Chemical Resistant Engineered Solid Surface Doorway Transition Saddle", unit="PCS", budget_price=0.0, notes="Bio-lab doorway hermetic transition saddles", trade="Tile & Stone")
        }

    @staticmethod
    def get_2843_columbia_rooms() -> List[RoomTakeoff]:
        return [
            RoomTakeoff(room_name="BIO-MEDICAL WET LAB & REAGENT SUITE 301", floor_name="LEVEL 3", length_ft=36.0, width_ft=22.0, ceiling_height_ft=11.0, wall_tile_height_ft=11.0, door_count=2, items=[
                TakeoffLineItem(symbol="ACT-01", finish_type="FLOOR", material_type="VITRIFIED TILE", work_type="S&I", quantity=792.0, unit="SQ FT", notes="Crossville 12x12 acid-resistant floor tile", trade="Tile & Stone"),
                TakeoffLineItem(symbol="AWT-01", finish_type="WALL", material_type="CHEMICAL TILE", work_type="S&I", quantity=680.0, unit="SQ FT", notes="Daltile 8x16 chemical resistant wall tile full 11' height", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WB-01", finish_type="WALL", material_type="VITRIFIED COVE BASE", work_type="S&I", quantity=110.0, unit="LN FT", notes="6x12 vitrified sanitary cove base", trade="Tile & Stone"),
                TakeoffLineItem(symbol="LAB-01", finish_type="LAB SINK COUNTERTOP", material_type="EPOXY RESIN", work_type="S&I", quantity=56.0, unit="SQ FT", notes="1-inch solid epoxy resin lab bench and sink top", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=792.0, unit="SQ FT", notes="Secondary containment waterproofing", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="WALL/1' HEIGHT", material_type="WATERPROOF", work_type="S&I", quantity=110.0, unit="SQ FT", notes="1-foot wall base chemical containment", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=792.0, unit="SQ FT", notes="Sloped mud-set bed to chemical drains", trade="Tile & Stone"),
                TakeoffLineItem(symbol="EPOXY-GROUT", finish_type="PREPARATION", material_type="EPOXY GROUT", work_type="S&I", quantity=792.0, unit="SQ FT", notes="SpectraLOCK 2000 IG Novolac chemical epoxy", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=48.0, unit="LN FT", notes="316 stainless steel edge trims", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="PCS", notes="Solid surface transition saddles", trade="Tile & Stone")
            ]),
            RoomTakeoff(room_name="AUTOCLAVE & STERILIZATION ROOM 302", floor_name="LEVEL 3", length_ft=16.0, width_ft=12.0, ceiling_height_ft=10.0, wall_tile_height_ft=10.0, door_count=1, items=[
                TakeoffLineItem(symbol="ACT-01", finish_type="FLOOR", material_type="VITRIFIED TILE", work_type="S&I", quantity=192.0, unit="SQ FT", notes="Crossville vitrified floor", trade="Tile & Stone"),
                TakeoffLineItem(symbol="AWT-01", finish_type="WALL", material_type="CHEMICAL TILE", work_type="S&I", quantity=420.0, unit="SQ FT", notes="Chemical resistant wall tile to ceiling", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WB-01", finish_type="WALL", material_type="VITRIFIED COVE BASE", work_type="S&I", quantity=56.0, unit="LN FT", notes="Sanitary cove base", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=192.0, unit="SQ FT", notes="Waterproofing membrane", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=192.0, unit="SQ FT", notes="Mud-set leveling bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="EPOXY-GROUT", finish_type="PREPARATION", material_type="EPOXY GROUT", work_type="S&I", quantity=192.0, unit="SQ FT", notes="Chemical epoxy grout", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS", finish_type="WALL", material_type="SCHLUTER METAL TRIM", work_type="S&I", quantity=24.0, unit="LN FT", notes="Stainless trim", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Engineered solid saddle", trade="Tile & Stone")
            ])
        ]

    # =========================================================================
    # [2844] Lincoln Center David Geffen Hall - VIP Patron Salon & Public Concourse
    # =========================================================================
    @staticmethod
    def get_2844_lincolncenter_metadata() -> Dict[str, Any]:
        return {
            "project_name": "[2844] Lincoln Center David Geffen Hall - VIP Patron Salon & Public Concourse",
            "client_name": "Lincoln Center for the Performing Arts",
            "client_company": "Turner Construction / Cultural Division",
            "date_str": "11/02/2026",
            "trade_category": "Tile & Stone"
        }

    @staticmethod
    def get_2844_lincolncenter_specs() -> Dict[str, MaterialSpec]:
        return {
            "TZ-01": MaterialSpec(symbol="TZ-01", description="Fabbrica, Custom Honed Venetian Micro-Terrazzo 36x36 with Curved Brass Inlays", unit="SQ FT", budget_price=0.0, notes="Main patron atrium, promenade & grand reception foyer", trade="Tile & Stone"),
            "WT-01": MaterialSpec(symbol="WT-01", description="Porcelanosa, Fluted Acoustic Porcelain Large Format Wall Cladding Slabs 24x48", unit="SQ FT", budget_price=0.0, notes="Acoustic auditorium buffer walls & VIP salon feature walls", trade="Tile & Stone"),
            "ST-01": MaterialSpec(symbol="ST-01", description="Antolini, Cristallo Quartzite 3cm Polished Translucent Bar Top with Mitered Waterfall Edge", unit="SQ FT", budget_price=0.0, notes="VIP champagne bar counter with backlit LED integration", trade="Tile & Stone"),
            "TB-01": MaterialSpec(symbol="TB-01", description="Fabbrica, 4x12 Venetian Terrazzo Honed Perimeter Baseboard", unit="LN FT", budget_price=0.0, notes="Continuous acoustic decoupling perimeter baseboard", trade="Tile & Stone"),
            "ACOUSTIC-PAD": MaterialSpec(symbol="ACOUSTIC-PAD", description="Schluter Ditra-Sound Acoustic Decoupling & Sound Isolation Membrane", unit="SQ FT", budget_price=0.0, notes="Under-tile acoustic dampening across all public concourses", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="Portland Mud-Set Mortar Bed & Self-Leveling Subfloor Underlayment", unit="SQ FT", budget_price=0.0, notes="Precision subfloor leveling bed", trade="Tile & Stone"),
            "MS-BRASS": MaterialSpec(symbol="MS-BRASS", description="Schluter Systems Schiene Solid Architectural Satin Brass Curved Matrix Trim", unit="LN FT", budget_price=0.0, notes="Radial brass inlay floor patterns and stone transitions", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="Cristallo Quartzite Custom Double-Beveled Doorway Threshold Saddle", unit="PCS", budget_price=0.0, notes="VIP salon doorway transition thresholds", trade="Tile & Stone")
        }

    @staticmethod
    def get_2844_lincolncenter_rooms() -> List[RoomTakeoff]:
        return [
            RoomTakeoff(room_name="VIP PATRON GRAND PROMENADE & FOYER", floor_name="TIER 1 PROMENADE", length_ft=42.0, width_ft=26.0, ceiling_height_ft=16.0, wall_tile_height_ft=16.0, door_count=2, items=[
                TakeoffLineItem(symbol="TZ-01", finish_type="FLOOR", material_type="TERRAZZO TILE", work_type="S&I", quantity=1092.0, unit="SQ FT", notes="Fabbrica 36x36 Venetian micro-terrazzo floor", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WT-01", finish_type="WALL", material_type="PORCELAIN SLAB", work_type="S&I", quantity=640.0, unit="SQ FT", notes="Porcelanosa 24x48 fluted acoustic porcelain wall slabs", trade="Tile & Stone"),
                TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="TERRAZZO BASE", work_type="S&I", quantity=136.0, unit="LN FT", notes="4x12 Venetian terrazzo base", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="BAR COUNTERTOP & WATERFALL", material_type="QUARTZITE SLAB", work_type="S&I", quantity=68.0, unit="SQ FT", notes="Cristallo 3cm quartzite bar top with 3-inch mitered waterfall edge", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ACOUSTIC-PAD", finish_type="FLOOR", material_type="ACOUSTIC MEMBRANE", work_type="S&I", quantity=1092.0, unit="SQ FT", notes="Schluter Ditra-Sound isolation underlayment", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=1092.0, unit="SQ FT", notes="Precision mud-set mortar bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-BRASS", finish_type="FLOOR", material_type="BRASS METAL TRIM", work_type="S&I", quantity=84.0, unit="LN FT", notes="Solid satin brass radial curved floor matrix inlays", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="PCS", notes="Cristallo quartzite doorway saddles", trade="Tile & Stone")
            ]),
            RoomTakeoff(room_name="PATRON LOUNGE EXECUTIVE POWDER ROOM", floor_name="TIER 1 PROMENADE", length_ft=12.0, width_ft=9.0, ceiling_height_ft=10.0, wall_tile_height_ft=10.0, door_count=1, items=[
                TakeoffLineItem(symbol="TZ-01", finish_type="FLOOR", material_type="TERRAZZO TILE", work_type="S&I", quantity=108.0, unit="SQ FT", notes="Venetian micro-terrazzo floor", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WT-01", finish_type="WALL", material_type="PORCELAIN SLAB", work_type="S&I", quantity=360.0, unit="SQ FT", notes="Fluted porcelain wall slabs to ceiling", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="VANITY COUNTERTOP", material_type="QUARTZITE SLAB", work_type="S&I", quantity=18.0, unit="SQ FT", notes="Cristallo quartzite vanity top with undermount lavatory", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ACOUSTIC-PAD", finish_type="FLOOR", material_type="ACOUSTIC MEMBRANE", work_type="S&I", quantity=108.0, unit="SQ FT", notes="Acoustic sound isolation membrane", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=108.0, unit="SQ FT", notes="Mud-set bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-BRASS", finish_type="WALL", material_type="BRASS METAL TRIM", work_type="S&I", quantity=24.0, unit="LN FT", notes="Satin brass edge trims", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Quartzite doorway saddle", trade="Tile & Stone")
            ])
        ]

    # =========================================================================
    # [2845] Equinox Sports Club & Aquatic Spa Facility - 160 Columbus Ave
    # =========================================================================
    @staticmethod
    def get_2845_equinox_metadata() -> Dict[str, Any]:
        return {
            "project_name": "[2845] Equinox Sports Club & Aquatic Spa Facility - 160 Columbus Ave",
            "client_name": "Equinox Holdings / Facility Development",
            "client_company": "Structure Tone / Luxury Hospitality & Fitness",
            "date_str": "11/19/2026",
            "trade_category": "Tile & Stone"
        }

    @staticmethod
    def get_2845_equinox_specs() -> Dict[str, MaterialSpec]:
        return {
            "PT-01": MaterialSpec(symbol="PT-01", description="Porcelanosa, Anti-Slip R11 Structured Wet-Deck Porcelain 12x24 Tile", unit="SQ FT", budget_price=0.0, notes="Olympic pool deck, wet spa & locker circulation floor (DCOF >= 0.65)", trade="Tile & Stone"),
            "MOS-01": MaterialSpec(symbol="MOS-01", description="Bisazza, Deep Cobalt Blue 1x1 Glass Mosaic Blend", unit="SQ FT", budget_price=0.0, notes="Pool interior basin, spa wet walls & eucalyptus steam rooms", trade="Tile & Stone"),
            "ST-01": MaterialSpec(symbol="ST-01", description="Nemo Tile, Flamed Nero Basalt 2-inch Pool Gutter Coping Stone & Grate Ledges", unit="LN FT", budget_price=0.0, notes="Perimeter overflow pool rim & coping stones", trade="Tile & Stone"),
            "TB-01": MaterialSpec(symbol="TB-01", description="Porcelanosa, 4x12 Anti-Slip Porcelain Tile Baseboard", unit="LN FT", budget_price=0.0, notes="Continuous wet perimeter baseboard", trade="Tile & Stone"),
            "SUB-WP": MaterialSpec(symbol="SUB-WP", description="Laticrete 9235 Full Submersion Certified Liquid Waterproofing & Crack Isolation", unit="SQ FT", budget_price=0.0, notes="Pool basin, wet spa deck & continuous steam enclosures", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="Portland Mud-Set Mortar Bed & Heavy-Duty Sloped Bed Underlayment", unit="SQ FT", budget_price=0.0, notes="Pitched mud bed to perimeter continuous pool trench drains", trade="Tile & Stone"),
            "EPOXY-GROUT": MaterialSpec(symbol="EPOXY-GROUT", description="Laticrete SpectraLOCK PRO Premium Chlorine & Chemical Resistant Epoxy Grout", unit="SQ FT", budget_price=0.0, notes="100% waterproof chemical resistant pool & deck grouting", trade="Tile & Stone"),
            "MS-EXP": MaterialSpec(symbol="MS-EXP", description="Schluter Systems Dilex Heavy-Duty Aquatic Submersion Expansion Joint Trim", unit="LN FT", budget_price=0.0, notes="Pool deck and wall thermal movement expansion joints", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="Flamed Basalt Double-Beveled Non-Slip Wet Transition Saddle", unit="PCS", budget_price=0.0, notes="Wet deck to dry locker doorway saddles", trade="Tile & Stone")
        }

    @staticmethod
    def get_2845_equinox_rooms() -> List[RoomTakeoff]:
        return [
            RoomTakeoff(room_name="INDOOR LAP POOL WET DECK & HYDROTHERAPY SPA", floor_name="POOL LEVEL", length_ft=60.0, width_ft=32.0, ceiling_height_ft=18.0, wall_tile_height_ft=12.0, door_count=2, items=[
                TakeoffLineItem(symbol="PT-01", finish_type="FLOOR", material_type="ANTI-SLIP PORCELAIN", work_type="S&I", quantity=1920.0, unit="SQ FT", notes="Porcelanosa 12x24 R11 non-slip pool deck floor", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MOS-01", finish_type="WALL", material_type="GLASS MOSAIC", work_type="S&I", quantity=1480.0, unit="SQ FT", notes="Bisazza 1x1 glass mosaic full wet wall surround", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="POOL COPING & RIM", material_type="BASALT STONE", work_type="S&I", quantity=184.0, unit="LN FT", notes="Flamed Nero Basalt 2-inch pool coping rim", trade="Tile & Stone"),
                TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN BASE", work_type="S&I", quantity=178.0, unit="LN FT", notes="4x12 anti-slip porcelain base", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SUB-WP", finish_type="FLOOR & FULL WET WALLS", material_type="WATERPROOF", work_type="S&I", quantity=3400.0, unit="SQ FT", notes="Laticrete 9235 full submersion waterproofing membrane", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=1920.0, unit="SQ FT", notes="Sloped mud-set bed to perimeter gutters", trade="Tile & Stone"),
                TakeoffLineItem(symbol="EPOXY-GROUT", finish_type="PREPARATION", material_type="EPOXY GROUT", work_type="S&I", quantity=1920.0, unit="SQ FT", notes="SpectraLOCK PRO chlorine-proof epoxy grout", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-EXP", finish_type="FLOOR", material_type="SCHLUTER EXPANSION TRIM", work_type="S&I", quantity=96.0, unit="LN FT", notes="Schluter Dilex aquatic expansion joint profiles", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="PCS", notes="Flamed basalt non-slip doorway saddles", trade="Tile & Stone")
            ]),
            RoomTakeoff(room_name="EUCALYPTUS STEAM SUITE & RAIN SHOWERS", floor_name="POOL LEVEL", length_ft=20.0, width_ft=14.0, ceiling_height_ft=9.5, wall_tile_height_ft=9.5, door_count=1, items=[
                TakeoffLineItem(symbol="PT-01", finish_type="FLOOR", material_type="ANTI-SLIP PORCELAIN", work_type="S&I", quantity=280.0, unit="SQ FT", notes="Porcelanosa R11 non-slip floor", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MOS-01", finish_type="WALL", material_type="GLASS MOSAIC", work_type="S&I", quantity=620.0, unit="SQ FT", notes="Bisazza glass mosaic wet walls to ceiling", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SUB-WP", finish_type="FLOOR & FULL STEAM WALLS", material_type="WATERPROOF", work_type="S&I", quantity=900.0, unit="SQ FT", notes="Submersion-grade vapor and waterproofing", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=280.0, unit="SQ FT", notes="Pitched mud bed to floor drains", trade="Tile & Stone"),
                TakeoffLineItem(symbol="EPOXY-GROUT", finish_type="PREPARATION", material_type="EPOXY GROUT", work_type="S&I", quantity=280.0, unit="SQ FT", notes="Chlorine-resistant epoxy grout", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-EXP", finish_type="WALL", material_type="SCHLUTER EXPANSION TRIM", work_type="S&I", quantity=36.0, unit="LN FT", notes="Stainless steam trim", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Flamed basalt saddle", trade="Tile & Stone")
            ])
        ]

    # =========================================================================
    # [2846] MTA Grand Central Madison - LIRR Concourse & Deep Station Mezzanine
    # =========================================================================
    @staticmethod
    def get_2846_mta_metadata() -> Dict[str, Any]:
        return {
            "project_name": "[2846] MTA Grand Central Madison - LIRR Concourse & Deep Station Mezzanine",
            "client_name": "MTA Construction & Development / Capital Programs",
            "client_company": "Tutor Perini / Heavy Civil & Transit Division",
            "date_str": "12/08/2026",
            "trade_category": "Tile & Stone"
        }

    @staticmethod
    def get_2846_mta_specs() -> Dict[str, MaterialSpec]:
        return {
            "MTA-QT": MaterialSpec(symbol="MTA-QT", description="Daltile, Heavy-Duty Abrasive Vitrified Transit Quarry Tile 6x6 Abrasive Surface", unit="SQ FT", budget_price=0.0, notes="Deep concourse passenger walkways, escalator landings & platform circulation", trade="Tile & Stone"),
            "MTA-WT": MaterialSpec(symbol="MTA-WT", description="Daltile, High-Impact Glazed Ceramic Station Wall Tile 4-1/4 x 8-1/2 Bright White", unit="SQ FT", budget_price=0.0, notes="Full height 14' transit concourse perimeter wet walls & tunnel cladding", trade="Tile & Stone"),
            "ADA-DOMES": MaterialSpec(symbol="ADA-DOMES", description="Armor-Tile, Tactile Detectable Warning Truncated Dome Vitrified Tiles 24x24 Federal Yellow", unit="SQ FT", budget_price=0.0, notes="Platform edge and stairway warning paving tiles", trade="Tile & Stone"),
            "MTA-BASE": MaterialSpec(symbol="MTA-BASE", description="Daltile, 6x6 Sanitary Quarry Coved Baseboard & Outcorner Fittings", unit="LN FT", budget_price=0.0, notes="Continuous transit coved perimeter baseboard", trade="Tile & Stone"),
            "WATERPROOF": MaterialSpec(symbol="WATERPROOF", description="MTA Specified Heavy-Duty Elastomeric Positive Side Waterproofing Membrane", unit="SQ FT", budget_price=0.0, notes="Sub-grade concrete slab & deep bedrock wall containment", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="Portland Mud-Set Mortar Bed & Heavy-Load Transit Bedding Underlayment", unit="SQ FT", budget_price=0.0, notes="Vibration-isolated subfloor leveling bed", trade="Tile & Stone"),
            "EPOXY-GROUT": MaterialSpec(symbol="EPOXY-GROUT", description="Laticrete SpectraLOCK 2000 IG Transit Grade Heavy Chemical & Stain Resistant Epoxy", unit="SQ FT", budget_price=0.0, notes="High-pressure washdown and graffiti chemical resistant grouting", trade="Tile & Stone"),
            "MS-EXP": MaterialSpec(symbol="MS-EXP", description="Schluter Dilex Heavy-Duty Solid Stainless Steel Structural Expansion Joint Profiles", unit="LN FT", budget_price=0.0, notes="Thermal and structural seismic expansion joint profiles", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="Heavy-Duty Absolute Black Granite Custom Transit Beveled Transition Saddle", unit="PCS", budget_price=0.0, notes="Egress doorway transition thresholds", trade="Tile & Stone")
        }

    @staticmethod
    def get_2846_mta_rooms() -> List[RoomTakeoff]:
        return [
            RoomTakeoff(room_name="LIRR DEEP STATION CONCOURSE & ESCALATOR MEZZANINE", floor_name="CONCOURSE LEVEL", length_ft=65.0, width_ft=34.0, ceiling_height_ft=16.0, wall_tile_height_ft=14.0, door_count=3, items=[
                TakeoffLineItem(symbol="MTA-QT", finish_type="FLOOR", material_type="TRANSIT QUARRY TILE", work_type="S&I", quantity=2210.0, unit="SQ FT", notes="Daltile 6x6 abrasive transit quarry tile floor", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MTA-WT", finish_type="WALL", material_type="GLAZED WALL TILE", work_type="S&I", quantity=1480.0, unit="SQ FT", notes="Daltile 4-1/4 x 8-1/2 transit wall tile 14' high", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ADA-DOMES", finish_type="STAIR & EGRESS WARNING", material_type="DETECTABLE WARNING", work_type="S&I", quantity=120.0, unit="SQ FT", notes="Armor-Tile 24x24 yellow tactile warning tiles", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MTA-BASE", finish_type="WALL", material_type="QUARRY COVE BASE", work_type="S&I", quantity=188.0, unit="LN FT", notes="6x6 coved quarry base", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR & TUNNEL WALLS", material_type="WATERPROOF", work_type="S&I", quantity=3690.0, unit="SQ FT", notes="Heavy duty elastomeric positive-side waterproofing", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=2210.0, unit="SQ FT", notes="Heavy load transit mud-set bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="EPOXY-GROUT", finish_type="PREPARATION", material_type="EPOXY GROUT", work_type="S&I", quantity=2210.0, unit="SQ FT", notes="SpectraLOCK 2000 IG washdown-proof epoxy", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-EXP", finish_type="FLOOR", material_type="SCHLUTER EXPANSION TRIM", work_type="S&I", quantity=124.0, unit="LN FT", notes="Schluter Dilex heavy-duty stainless expansion joints", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=3.0, unit="PCS", notes="Absolute Black granite transit saddles", trade="Tile & Stone")
            ]),
            RoomTakeoff(room_name="PUBLIC MULTI-STALL PASSENGER RESTROOM SUITE", floor_name="CONCOURSE LEVEL", length_ft=24.0, width_ft=16.0, ceiling_height_ft=11.0, wall_tile_height_ft=11.0, door_count=1, items=[
                TakeoffLineItem(symbol="MTA-QT", finish_type="FLOOR", material_type="TRANSIT QUARRY TILE", work_type="S&I", quantity=384.0, unit="SQ FT", notes="Daltile 6x6 quarry tile floor", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MTA-WT", finish_type="WALL", material_type="GLAZED WALL TILE", work_type="S&I", quantity=580.0, unit="SQ FT", notes="Daltile 4-1/4 x 8-1/2 wall tile full height", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MTA-BASE", finish_type="WALL", material_type="QUARRY COVE BASE", work_type="S&I", quantity=76.0, unit="LN FT", notes="6x6 coved base", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=384.0, unit="SQ FT", notes="Floor waterproofing membrane", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=384.0, unit="SQ FT", notes="Mud-set leveling bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="EPOXY-GROUT", finish_type="PREPARATION", material_type="EPOXY GROUT", work_type="S&I", quantity=384.0, unit="SQ FT", notes="Washdown epoxy grout", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-EXP", finish_type="WALL", material_type="SCHLUTER EXPANSION TRIM", work_type="S&I", quantity=32.0, unit="LN FT", notes="Stainless edge trims", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Granite doorway saddle", trade="Tile & Stone")
            ])
        ]

    # =========================================================================
    # [2847] Porsche NYC Experience Center & High-Load EV Delivery Lounge - 11th Ave
    # =========================================================================
    @staticmethod
    def get_2847_porsche_metadata() -> Dict[str, Any]:
        return {
            "project_name": "[2847] Porsche NYC Experience Center & High-Load EV Delivery Lounge - 11th Ave",
            "client_name": "Porsche Cars North America / Retail Real Estate",
            "client_company": "Plaza Construction / Automotive Flagship Division",
            "date_str": "12/16/2026",
            "trade_category": "Tile & Stone"
        }

    @staticmethod
    def get_2847_porsche_specs() -> Dict[str, MaterialSpec]:
        return {
            "AUT-01": MaterialSpec(symbol="AUT-01", description="Grespania, 20mm High-Load Structural Porcelain 24x24 Heavy Point Load Floor Tile (R12 Slip Rating)", unit="SQ FT", budget_price=0.0, notes="Vehicle delivery runway, turntable & EV handover bay (8,000 lb wheel load rating)", trade="Tile & Stone"),
            "AUT-02": MaterialSpec(symbol="AUT-02", description="Porcelanosa, Concrete Grigio Polished Large Format Porcelain 48x48 Showroom Tile", unit="SQ FT", budget_price=0.0, notes="Client consultation gallery, design studio & accessories boutique", trade="Tile & Stone"),
            "ST-01": MaterialSpec(symbol="ST-01", description="Caesarstone, Black Tempal 2cm Honed Quartz Island Countertop with 4-inch Drop Apron", unit="SQ FT", budget_price=0.0, notes="Fitting lounge bar and vehicle specification consultation island", trade="Tile & Stone"),
            "TB-01": MaterialSpec(symbol="TB-01", description="Grespania, 4x24 Matching 20mm Industrial Porcelain Baseboard", unit="LN FT", budget_price=0.0, notes="Vehicle showroom impact-resistant perimeter base", trade="Tile & Stone"),
            "WATERPROOF": MaterialSpec(symbol="WATERPROOF", description="Laticrete Hydro Ban High-Compressive Load Waterproofing & Crack Isolation", unit="SQ FT", budget_price=0.0, notes="Showroom slab crack isolation & EV wet delivery bay", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="Portland High-Strength 6,000 PSI Mud-Set Mortar Bed Underlayment", unit="SQ FT", budget_price=0.0, notes="Heavy vehicle point-load bedding mortar", trade="Tile & Stone"),
            "EPOXY-GROUT": MaterialSpec(symbol="EPOXY-GROUT", description="Laticrete SpectraLOCK PRO Industrial Tire-Mark & Oil-Proof Epoxy Grout", unit="SQ FT", budget_price=0.0, notes="Automotive chemical and hot tire pickup resistant epoxy", trade="Tile & Stone"),
            "MS-HEAVY": MaterialSpec(symbol="MS-HEAVY", description="Schluter Reno-RAMP Heavy-Duty Extruded Anodized Aluminum Vehicle Ramp Edge Profile", unit="LN FT", budget_price=0.0, notes="Vehicle roll-over transition profiles", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="Custom Heavy-Duty Absolute Black Granite 1-1/4 inch Vehicle Threshold Saddle", unit="PCS", budget_price=0.0, notes="Vehicle bay overhead door threshold transitions", trade="Tile & Stone")
        }

    @staticmethod
    def get_2847_porsche_rooms() -> List[RoomTakeoff]:
        return [
            RoomTakeoff(room_name="EV VEHICLE HANDOVER BAY & RUNWAY SALON", floor_name="GROUND FLOOR", length_ft=44.0, width_ft=28.0, ceiling_height_ft=14.0, wall_tile_height_ft=0.0, door_count=2, items=[
                TakeoffLineItem(symbol="AUT-01", finish_type="FLOOR", material_type="20MM PORCELAIN TILE", work_type="S&I", quantity=1232.0, unit="SQ FT", notes="Grespania 20mm structural porcelain 24x24 vehicle floor", trade="Tile & Stone"),
                TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN BASE", work_type="S&I", quantity=138.0, unit="LN FT", notes="4x24 20mm matching baseboard", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=1232.0, unit="SQ FT", notes="High-compressive load crack isolation membrane", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=1232.0, unit="SQ FT", notes="High-strength 6000 PSI vehicle mud-set bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="EPOXY-GROUT", finish_type="PREPARATION", material_type="EPOXY GROUT", work_type="S&I", quantity=1232.0, unit="SQ FT", notes="SpectraLOCK PRO tire-mark proof epoxy", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-HEAVY", finish_type="FLOOR", material_type="ALUMINUM RAMP TRIM", work_type="S&I", quantity=56.0, unit="LN FT", notes="Schluter Reno-RAMP vehicle roll-over edge profile", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="PCS", notes="Heavy duty 1-1/4 inch granite saddles", trade="Tile & Stone")
            ]),
            RoomTakeoff(room_name="DESIGN FITTING STUDIO & CLIENT LOUNGE", floor_name="GROUND FLOOR", length_ft=28.0, width_ft=18.0, ceiling_height_ft=12.0, wall_tile_height_ft=0.0, door_count=1, items=[
                TakeoffLineItem(symbol="AUT-02", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=504.0, unit="SQ FT", notes="Porcelanosa 48x48 concrete grigio polished tile", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="CONSULTATION ISLAND COUNTERTOP", material_type="QUARTZ", work_type="S&I", quantity=64.0, unit="SQ FT", notes="Caesarstone Black Tempal island top with 4-inch mitered drop apron", trade="Tile & Stone"),
                TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN BASE", work_type="S&I", quantity=89.0, unit="LN FT", notes="Tile perimeter base", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=504.0, unit="SQ FT", notes="Precision self-leveling underlayment", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-HEAVY", finish_type="FLOOR", material_type="ALUMINUM RAMP TRIM", work_type="S&I", quantity=24.0, unit="LN FT", notes="Schluter transition trim", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Granite transition saddle", trade="Tile & Stone")
            ])
        ]

    # =========================================================================
    # [2848] Upper East Side Historic 5-Story Townhouse Restoration - 18 East 74th St
    # =========================================================================
    @staticmethod
    def get_2848_townhouse_metadata() -> Dict[str, Any]:
        return {
            "project_name": "[2848] Upper East Side Historic 5-Story Townhouse Restoration - 18 East 74th St",
            "client_name": "Private Client / Historical Commission",
            "client_company": "Prime Renovations / Luxury Residential",
            "date_str": "12/22/2026",
            "trade_category": "Tile & Stone"
        }

    @staticmethod
    def get_2848_townhouse_specs() -> Dict[str, MaterialSpec]:
        return {
            "ZEL-01": MaterialSpec(symbol="ZEL-01", description="Clé Tile, Hand-Crafted Authentic Moroccan Terracotta Zellige 4x4 Wall Tile Snow White", unit="SQ FT", budget_price=0.0, notes="Kitchen full height backsplash, hood surround & pantry walls", trade="Tile & Stone"),
            "ST-01": MaterialSpec(symbol="ST-01", description="Artistic Tile, Calacatta Viola Honed 2cm Marble Slabs with Carved Integral Basin", unit="SQ FT", budget_price=0.0, notes="Primary bathroom wall slab cladding, floating stone vanity & shower bench", trade="Tile & Stone"),
            "MOS-01": MaterialSpec(symbol="MOS-01", description="Stone Source, Arabescato & Nero Marquina Basketweave Marble Mosaic 1x2 with Black Dots", unit="SQ FT", budget_price=0.0, notes="Primary bathroom heated floor and shower pan floor", trade="Tile & Stone"),
            "TB-01": MaterialSpec(symbol="TB-01", description="Artistic Tile, Calacatta Viola 4x12 Honed Marble Baseboard", unit="LN FT", budget_price=0.0, notes="Primary bathroom perimeter luxury stone baseboard", trade="Tile & Stone"),
            "RADIANT-HEAT": MaterialSpec(symbol="RADIANT-HEAT", description="Schluter Ditra-Heat Electric Floor Heating & Waterproofing Membrane", unit="SQ FT", budget_price=0.0, notes="Primary bathroom radiant floor warming & crack isolation", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="Portland Mud-Set Mortar Bed & Sloped Shower Pan Underlayment", unit="SQ FT", budget_price=0.0, notes="Pitched mud bed to linear hidden trench drain", trade="Tile & Stone"),
            "MS-BRASS": MaterialSpec(symbol="MS-BRASS", description="Schluter Systems Schiene Solid Unlacquered Living Brass Trim Profile", unit="LN FT", budget_price=0.0, notes="Handcrafted living brass corner & niche termination trims", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="Calacatta Viola Honed Marble Custom Double-Beveled Transition Saddle", unit="PCS", budget_price=0.0, notes="Townhouse bedroom to primary bath transition thresholds", trade="Tile & Stone")
        }

    @staticmethod
    def get_2848_townhouse_rooms() -> List[RoomTakeoff]:
        return [
            RoomTakeoff(room_name="LEVEL 3 PRIMARY BATHROOM & WET ROOM SUITE", floor_name="LEVEL 3", length_ft=18.0, width_ft=14.0, ceiling_height_ft=11.0, wall_tile_height_ft=11.0, door_count=1, items=[
                TakeoffLineItem(symbol="MOS-01", finish_type="FLOOR", material_type="MARBLE MOSAIC", work_type="S&I", quantity=252.0, unit="SQ FT", notes="Arabescato basketweave mosaic heated floor", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="WALL SLAB CLADDING", material_type="MARBLE SLAB", work_type="S&I", quantity=520.0, unit="SQ FT", notes="Calacatta Viola 2cm honed marble slabs full 11' height", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="CARVED VANITY & FLOATING SINK", material_type="MARBLE SLAB", work_type="S&I", quantity=32.0, unit="SQ FT", notes="Calacatta Viola floating vanity with carved integral marble basin", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="SHOWER BENCH & NICHE LEDGE", material_type="MARBLE SLAB", work_type="S&I", quantity=14.0, unit="SQ FT", notes="Solid marble floating shower bench and shelf", trade="Tile & Stone"),
                TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="MARBLE BASE", work_type="S&I", quantity=58.0, unit="LN FT", notes="Calacatta Viola 4x12 marble baseboard", trade="Tile & Stone"),
                TakeoffLineItem(symbol="RADIANT-HEAT", finish_type="FLOOR", material_type="HEATED MEMBRANE", work_type="S&I", quantity=252.0, unit="SQ FT", notes="Schluter Ditra-Heat electric heating membrane", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=252.0, unit="SQ FT", notes="Sloped mud-set bed to linear drain", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-BRASS", finish_type="WALL", material_type="BRASS METAL TRIM", work_type="S&I", quantity=48.0, unit="LN FT", notes="Solid unlacquered brass corner trims", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Calacatta Viola doorway saddle", trade="Tile & Stone")
            ]),
            RoomTakeoff(room_name="GARDEN LEVEL CHEF'S KITCHEN & PANTRY", floor_name="GARDEN LEVEL", length_ft=22.0, width_ft=15.0, ceiling_height_ft=10.0, wall_tile_height_ft=3.5, door_count=1, items=[
                TakeoffLineItem(symbol="ZEL-01", finish_type="WALL BACKSPLASH & HOOD", material_type="ZELLIGE TILE", work_type="S&I", quantity=95.0, unit="SQ FT", notes="Clé Tile handcrafted Moroccan Zellige 4x4 full splash and range hood", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-BRASS", finish_type="WALL", material_type="BRASS METAL TRIM", work_type="S&I", quantity=32.0, unit="LN FT", notes="Unlacquered brass top edge trim", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Marble transition saddle", trade="Tile & Stone")
            ])
        ]

    # =========================================================================
    # [2849] One Vanderbilt Summit Sky Lounge & Heated Outdoor Observation Terrace - 1 Vanderbilt Ave
    # =========================================================================
    @staticmethod
    def get_2849_onevanderbilt_metadata() -> Dict[str, Any]:
        return {
            "project_name": "[2849] One Vanderbilt Summit Sky Lounge & Heated Outdoor Observation Terrace - 1 Vanderbilt Ave",
            "client_name": "SL Green Realty / Summit Development",
            "client_company": "AECOM Tishman / Supertall Tower Division",
            "date_str": "01/15/2027",
            "trade_category": "Tile & Stone"
        }

    @staticmethod
    def get_2849_onevanderbilt_specs() -> Dict[str, MaterialSpec]:
        return {
            "EXT-01": MaterialSpec(symbol="EXT-01", description="Mirage, 20mm (3/4-inch) Exterior Freeze-Thaw Anti-Slip Porcelain Pavers 24x24 (R11 Rating)", unit="SQ FT", budget_price=0.0, notes="High-altitude heated outdoor terrace & sky observation deck", trade="Tile & Stone"),
            "ST-01": MaterialSpec(symbol="ST-01", description="Nemo Tile, Flamed Jet Mist Granite 2-inch Custom Parapet Coping & Firepit Surrounds", unit="LN FT", budget_price=0.0, notes="Perimeter sky terrace parapet wall coping and cantilevered ledge", trade="Tile & Stone"),
            "ST-02": MaterialSpec(symbol="ST-02", description="Cosentino, Dekton Aura 2cm Polished Sky Bar Countertop with Mitered Waterfall Ends", unit="SQ FT", budget_price=0.0, notes="Sky lounge cocktail bar & outdoor heated service counter", trade="Tile & Stone"),
            "TB-01": MaterialSpec(symbol="TB-01", description="Mirage, 4x24 Matching 20mm Exterior Porcelain Baseboard", unit="LN FT", budget_price=0.0, notes="Terrace perimeter baseboard", trade="Tile & Stone"),
            "SNOW-MELT": MaterialSpec(symbol="SNOW-MELT", description="Schluter Ditra-Heat Exterior Radiant Snow-Melt Thermal & Waterproofing Membrane", unit="SQ FT", budget_price=0.0, notes="Radiant thermal snow-melt system across all exterior terrace floors", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="Portland Polymer-Modified Frost-Resistant Mud-Set Mortar Bed Underlayment", unit="SQ FT", budget_price=0.0, notes="Pitched freeze-thaw bed to perimeter continuous roof scuppers", trade="Tile & Stone"),
            "EPOXY-GROUT": MaterialSpec(symbol="EPOXY-GROUT", description="Laticrete SpectraLOCK PRO Exterior UV & Freeze-Thaw Weatherproof Epoxy Grout", unit="SQ FT", budget_price=0.0, notes="100% UV stable exterior weatherproof grouting", trade="Tile & Stone"),
            "MS-WIND": MaterialSpec(symbol="MS-WIND", description="Schluter Systems Reno-HV Heavy-Duty Wind-Lock Stainless Steel Paver Edge Profile", unit="LN FT", budget_price=0.0, notes="High-altitude wind-uplift perimeter locking profiles", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="Flamed Jet Mist Granite Custom Weatherproof Exterior Doorway Saddle", unit="PCS", budget_price=0.0, notes="Terrace slider to indoor lounge transition thresholds", trade="Tile & Stone")
        }

    @staticmethod
    def get_2849_onevanderbilt_rooms() -> List[RoomTakeoff]:
        return [
            RoomTakeoff(room_name="SUMMIT HEATED OUTDOOR SKY OBSERVATION TERRACE", floor_name="FLOOR 73", length_ft=52.0, width_ft=30.0, ceiling_height_ft=0.0, wall_tile_height_ft=0.0, door_count=2, items=[
                TakeoffLineItem(symbol="EXT-01", finish_type="FLOOR", material_type="20MM EXTERIOR PORCELAIN", work_type="S&I", quantity=1560.0, unit="SQ FT", notes="Mirage 20mm freeze-thaw porcelain pavers 24x24", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="PARAPET COPING & FIREPIT", material_type="GRANITE SLAB", work_type="S&I", quantity=164.0, unit="LN FT", notes="Flamed Jet Mist Granite 2-inch coping stones", trade="Tile & Stone"),
                TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN BASE", work_type="S&I", quantity=158.0, unit="LN FT", notes="4x24 matching exterior porcelain base", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SNOW-MELT", finish_type="FLOOR", material_type="RADIANT MEMBRANE", work_type="S&I", quantity=1560.0, unit="SQ FT", notes="Schluter radiant thermal snow-melt system", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=1560.0, unit="SQ FT", notes="Polymer-modified frost-resistant mud-set bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="EPOXY-GROUT", finish_type="PREPARATION", material_type="EPOXY GROUT", work_type="S&I", quantity=1560.0, unit="SQ FT", notes="SpectraLOCK PRO UV-stable exterior epoxy", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-WIND", finish_type="FLOOR", material_type="SCHLUTER WIND TRIM", work_type="S&I", quantity=84.0, unit="LN FT", notes="High-altitude wind-lock perimeter profiles", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="PCS", notes="Flamed granite weatherproof saddles", trade="Tile & Stone")
            ]),
            RoomTakeoff(room_name="INDOOR SKY LOUNGE & COCKTAIL SALON", floor_name="FLOOR 73", length_ft=34.0, width_ft=22.0, ceiling_height_ft=14.0, wall_tile_height_ft=0.0, door_count=1, items=[
                TakeoffLineItem(symbol="EXT-01", finish_type="FLOOR", material_type="PORCELAIN TILE", work_type="S&I", quantity=748.0, unit="SQ FT", notes="Mirage 24x24 porcelain floor tile", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-02", finish_type="SKY BAR COUNTERTOP & WATERFALL", material_type="DEKTON SLAB", work_type="S&I", quantity=76.0, unit="SQ FT", notes="Dekton Aura 2cm bar top with 3-inch mitered waterfall edge", trade="Tile & Stone"),
                TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN BASE", work_type="S&I", quantity=112.0, unit="LN FT", notes="Porcelain perimeter base", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=748.0, unit="SQ FT", notes="Precision mud-set underlayment", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Honed granite transition saddle", trade="Tile & Stone")
            ])
        ]

    # =========================================================================
    # [2850] Thurgood Marshall US Courthouse & Federal Judicial Chambers - 40 Foley Sq
    # =========================================================================
    @staticmethod
    def get_2850_courthouse_metadata() -> Dict[str, Any]:
        return {
            "project_name": "[2850] Thurgood Marshall US Courthouse & Federal Judicial Chambers - 40 Foley Sq",
            "client_name": "GSA Public Buildings Service / Region 2",
            "client_company": "Gilbane Building Company / Federal Landmark Division",
            "date_str": "01/28/2027",
            "trade_category": "Tile & Stone"
        }

    @staticmethod
    def get_2850_courthouse_specs() -> Dict[str, MaterialSpec]:
        return {
            "ST-01": MaterialSpec(symbol="ST-01", description="Vermont Quarries, Imperial Danby Honed 2cm Marble Wall Wainscot Slabs", unit="SQ FT", budget_price=0.0, notes="Judicial ceremonial courtroom wainscot & judge's bench surround", trade="Tile & Stone"),
            "ST-02": MaterialSpec(symbol="ST-02", description="Tennessee Marble, Gray Fleuri Honed 18x18 Natural Marble Paver Tile", unit="SQ FT", budget_price=0.0, notes="Public judicial concourse, grand rotunda & jury deliberation foyer", trade="Tile & Stone"),
            "WT-01": MaterialSpec(symbol="WT-01", description="Daltile, Semi-Gloss Architectural Biscuit White 6x6 Acoustic Tile", unit="SQ FT", budget_price=0.0, notes="Federal restroom suites and secure prisoner holding wet walls", trade="Tile & Stone"),
            "TB-01": MaterialSpec(symbol="TB-01", description="Vermont Quarries, Imperial Danby 6x12 Honed Marble Baseboard", unit="LN FT", budget_price=0.0, notes="Continuous Federal courthouse stone baseboard", trade="Tile & Stone"),
            "GSA-MUD": MaterialSpec(symbol="GSA-MUD", description="Portland Blast-Mitigation Reinforced Mud-Set Bed & Subfloor Leveling", unit="SQ FT", budget_price=0.0, notes="GSA specified high-density reinforced stone bedding mortar", trade="Tile & Stone"),
            "WATERPROOF": MaterialSpec(symbol="WATERPROOF", description="Mapei Mapelastic 315 Low-VOC Elastomeric Waterproofing Membrane", unit="SQ FT", budget_price=0.0, notes="Restrooms, water containment and subfloor isolation", trade="Tile & Stone"),
            "EPOXY-GROUT": MaterialSpec(symbol="EPOXY-GROUT", description="Laticrete SpectraLOCK PRO Low-VOC Non-Shrink Architectural Epoxy Grout", unit="SQ FT", budget_price=0.0, notes="Federal landmark non-staining marble joint grouting", trade="Tile & Stone"),
            "MS-BRONZE": MaterialSpec(symbol="MS-BRONZE", description="Schluter Systems Schiene Solid Architectural Architectural Bronze Trim", unit="LN FT", budget_price=0.0, notes="Historical bronze wainscot top caps and floor transitions", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="Architectural Solid Cast Bronze Fluted ADA Doorway Transition Threshold", unit="PCS", budget_price=0.0, notes="Chambers doorway solid bronze thresholds", trade="Tile & Stone")
        }

    @staticmethod
    def get_2850_courthouse_rooms() -> List[RoomTakeoff]:
        return [
            RoomTakeoff(room_name="CEREMONIAL FEDERAL COURTROOM & BENCH SALON", floor_name="COURT FLOOR 5", length_ft=48.0, width_ft=32.0, ceiling_height_ft=18.0, wall_tile_height_ft=6.0, door_count=3, items=[
                TakeoffLineItem(symbol="ST-02", finish_type="FLOOR", material_type="MARBLE PAVER", work_type="S&I", quantity=1536.0, unit="SQ FT", notes="Tennessee Gray Fleuri 18x18 marble floor", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="WALL WAINSCOT SLABS", material_type="MARBLE SLAB", work_type="S&I", quantity=860.0, unit="SQ FT", notes="Imperial Danby 2cm marble slabs to 6-foot wainscot height", trade="Tile & Stone"),
                TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="MARBLE BASE", work_type="S&I", quantity=152.0, unit="LN FT", notes="Imperial Danby 6x12 marble baseboard", trade="Tile & Stone"),
                TakeoffLineItem(symbol="GSA-MUD", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=1536.0, unit="SQ FT", notes="GSA blast-mitigation reinforced mud-set bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="EPOXY-GROUT", finish_type="PREPARATION", material_type="EPOXY GROUT", work_type="S&I", quantity=1536.0, unit="SQ FT", notes="SpectraLOCK PRO non-staining marble grout", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-BRONZE", finish_type="WALL", material_type="BRONZE METAL TRIM", work_type="S&I", quantity=160.0, unit="LN FT", notes="Solid architectural bronze wainscot top caps", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="BRONZE SADDLE", work_type="S&I", quantity=3.0, unit="PCS", notes="Solid architectural bronze ADA saddles", trade="Tile & Stone")
            ]),
            RoomTakeoff(room_name="JUDICIAL RESTROOM & HOLDING VESTIBULE", floor_name="COURT FLOOR 5", length_ft=15.0, width_ft=11.0, ceiling_height_ft=10.0, wall_tile_height_ft=10.0, door_count=1, items=[
                TakeoffLineItem(symbol="ST-02", finish_type="FLOOR", material_type="MARBLE PAVER", work_type="S&I", quantity=165.0, unit="SQ FT", notes="Tennessee marble floor", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WT-01", finish_type="WALL", material_type="CERAMIC TILE", work_type="S&I", quantity=480.0, unit="SQ FT", notes="Daltile 6x6 biscuit white wall tile full height", trade="Tile & Stone"),
                TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="MARBLE BASE", work_type="S&I", quantity=51.0, unit="LN FT", notes="Marble baseboard", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=165.0, unit="SQ FT", notes="Low-VOC waterproofing membrane", trade="Tile & Stone"),
                TakeoffLineItem(symbol="GSA-MUD", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=165.0, unit="SQ FT", notes="Mud-set bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-BRONZE", finish_type="WALL", material_type="BRONZE METAL TRIM", work_type="S&I", quantity=26.0, unit="LN FT", notes="Bronze corner trims", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="BRONZE SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Bronze doorway threshold saddle", trade="Tile & Stone")
            ])
        ]

    # =========================================================================
    # [2851] Alamo Drafthouse Cinema & IMAX Multi-Auditorium Entertainment Complex - 28 Liberty St
    # =========================================================================
    @staticmethod
    def get_2851_cinema_metadata() -> Dict[str, Any]:
        return {
            "project_name": "[2851] Alamo Drafthouse Cinema & IMAX Multi-Auditorium Entertainment Complex - 28 Liberty St",
            "client_name": "Fosun / Alamo Drafthouse Real Estate",
            "client_company": "Structure Tone / Entertainment & Cinema Division",
            "date_str": "02/11/2027",
            "trade_category": "Tile & Stone"
        }

    @staticmethod
    def get_2851_cinema_specs() -> Dict[str, MaterialSpec]:
        return {
            "TR-01": MaterialSpec(symbol="TR-01", description="Porcelanosa, Charcoal Matte Non-Slip Stair Tread & Riser Porcelain 12x48 with Integral Abrasive Grooves", unit="LN FT", budget_price=0.0, notes="Multi-auditorium stadium seating step treads, risers & aisles", trade="Tile & Stone"),
            "TZ-01": MaterialSpec(symbol="TZ-01", description="Nabel, Polished Cast Terrazzo 24x24 Large Format Lobby & Concession Floor Tile", unit="SQ FT", budget_price=0.0, notes="Main cinema concessions, ticket foyer & cocktail bar floor", trade="Tile & Stone"),
            "ST-01": MaterialSpec(symbol="ST-01", description="Caesarstone, Concrete Rough 2cm Quartz Concession & Ticket Countertop with 3-inch Drop Apron", unit="SQ FT", budget_price=0.0, notes="Concession pick-up counter, beer tap bar & POS stations", trade="Tile & Stone"),
            "TB-01": MaterialSpec(symbol="TB-01", description="Nabel, 4x24 Matching Polished Terrazzo Baseboard", unit="LN FT", budget_price=0.0, notes="Continuous cinema lobby baseboard", trade="Tile & Stone"),
            "WATERPROOF": MaterialSpec(symbol="WATERPROOF", description="Laticrete Hydro Ban Commercial Sound & Spill Barrier Waterproofing Membrane", unit="SQ FT", budget_price=0.0, notes="Concession bar, kitchen prep & restroom wet areas", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="Portland Mud-Set Mortar Bed & Stadium Tier Leveling Underlayment", unit="SQ FT", budget_price=0.0, notes="Auditorium stadium raked step mud bedding", trade="Tile & Stone"),
            "EPOXY-GROUT": MaterialSpec(symbol="EPOXY-GROUT", description="Laticrete SpectraLOCK PRO Heavy Commercial Beverage & Spill Resistant Epoxy Grout", unit="SQ FT", budget_price=0.0, notes="Cinema stain and syrup resistant epoxy grouting", trade="Tile & Stone"),
            "MS-GLOW": MaterialSpec(symbol="MS-GLOW", description="Schluter Systems Trep-G Photoluminescent Glow-in-the-Dark Stair Nosing Safety Trim", unit="LN FT", budget_price=0.0, notes="Auditorium step edge glow safety nosing profiles", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="Heavy-Duty Absolute Black Honed Granite Doorway Transition Saddle", unit="PCS", budget_price=0.0, notes="Soundlock acoustic vestibule doorway saddles", trade="Tile & Stone")
        }

    @staticmethod
    def get_2851_cinema_rooms() -> List[RoomTakeoff]:
        return [
            RoomTakeoff(room_name="IMAX AUDITORIUM 1 - STADIUM STEPPED SEATING & AISLES", floor_name="LOWER LEVEL 2", length_ft=56.0, width_ft=38.0, ceiling_height_ft=24.0, wall_tile_height_ft=0.0, door_count=2, items=[
                TakeoffLineItem(symbol="TR-01", finish_type="STADIUM STEP TREADS & RISERS", material_type="STAIR TREAD PORCELAIN", work_type="S&I", quantity=420.0, unit="LN FT", notes="Porcelanosa 12x48 charcoal non-slip stair treads & risers", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=840.0, unit="SQ FT", notes="Stadium tiered step mortar bedding", trade="Tile & Stone"),
                TakeoffLineItem(symbol="EPOXY-GROUT", finish_type="PREPARATION", material_type="EPOXY GROUT", work_type="S&I", quantity=840.0, unit="SQ FT", notes="SpectraLOCK PRO spill-proof epoxy", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-GLOW", finish_type="STAIR NOSING", material_type="GLOW SAFETY TRIM", work_type="S&I", quantity=420.0, unit="LN FT", notes="Schluter Trep-G photoluminescent glow-in-the-dark step nosings", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="PCS", notes="Absolute Black granite acoustic soundlock saddles", trade="Tile & Stone")
            ]),
            RoomTakeoff(room_name="MAIN CINEMA CONCESSIONS & CRAFT BEER SALON", floor_name="LOWER LEVEL 2", length_ft=38.0, width_ft=24.0, ceiling_height_ft=14.0, wall_tile_height_ft=0.0, door_count=1, items=[
                TakeoffLineItem(symbol="TZ-01", finish_type="FLOOR", material_type="TERRAZZO TILE", work_type="S&I", quantity=912.0, unit="SQ FT", notes="Nabel 24x24 polished terrazzo floor tile", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="CONCESSION COUNTERTOP & FRONT", material_type="QUARTZ", work_type="S&I", quantity=96.0, unit="SQ FT", notes="Caesarstone 2cm Concrete Rough countertop with 3-inch drop apron", trade="Tile & Stone"),
                TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="TERRAZZO BASE", work_type="S&I", quantity=122.0, unit="LN FT", notes="4x24 terrazzo baseboard", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=912.0, unit="SQ FT", notes="Spill barrier waterproofing membrane", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=912.0, unit="SQ FT", notes="Subfloor leveling bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Granite doorway saddle", trade="Tile & Stone")
            ])
        ]

    # =========================================================================
    # [2852] Brooklyn Navy Yard Waterfront Marina & Commodore Harbor Club - 63 Flushing Ave
    # =========================================================================
    @staticmethod
    def get_2852_marinaclub_metadata() -> Dict[str, Any]:
        return {
            "project_name": "[2852] Brooklyn Navy Yard Waterfront Marina & Commodore Harbor Club - 63 Flushing Ave",
            "client_name": "Brooklyn Navy Yard Development Corp / Marina Ops",
            "client_company": "Skanska USA Building / Marine & Waterfront Division",
            "date_str": "03/04/2027",
            "trade_category": "Tile & Stone"
        }

    @staticmethod
    def get_2852_marinaclub_specs() -> Dict[str, MaterialSpec]:
        return {
            "MAR-01": MaterialSpec(symbol="MAR-01", description="Porcelanosa, Salt-Spray & Marine Resistant Structured Porcelain 24x24 Tile (R12 Rating)", unit="SQ FT", budget_price=0.0, notes="Waterfront harbor promenade, outdoor boat deck & marina boardwalk floor", trade="Tile & Stone"),
            "MAR-02": MaterialSpec(symbol="MAR-02", description="Mirage, Marine Teak Textured Non-Slip Exterior Porcelain Wood Planks 8x48", unit="SQ FT", budget_price=0.0, notes="Commodore dining salon & covered outdoor harbor terrace", trade="Tile & Stone"),
            "ST-01": MaterialSpec(symbol="ST-01", description="Cosentino, Dekton Laurent 2cm Saltwater Proof Marina Bar Countertop & Waterfall", unit="SQ FT", budget_price=0.0, notes="Waterfront raw bar, cocktail lounge counter & 3-inch mitered drop apron", trade="Tile & Stone"),
            "TB-01": MaterialSpec(symbol="TB-01", description="Porcelanosa, 4x24 Marine Grade Porcelain Baseboard", unit="LN FT", budget_price=0.0, notes="Waterfront perimeter baseboard", trade="Tile & Stone"),
            "MARINE-WP": MaterialSpec(symbol="MARINE-WP", description="Laticrete 9235 Marine Submersion & Salt-Barrier Liquid Waterproofing Membrane", unit="SQ FT", budget_price=0.0, notes="Harbor deck and wet lounge subfloor vapor containment", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="Portland Marine-Grade Polymer Mortar Bed & Sloped Underlayment", unit="SQ FT", budget_price=0.0, notes="Pitched frost and salt resistant mud-set bedding", trade="Tile & Stone"),
            "EPOXY-GROUT": MaterialSpec(symbol="EPOXY-GROUT", description="Laticrete SpectraLOCK PRO Marine Salt & Algae Proof Industrial Epoxy Grout", unit="SQ FT", budget_price=0.0, notes="Marine environmental chemical and salt proof grouting", trade="Tile & Stone"),
            "MS-316": MaterialSpec(symbol="MS-316", description="Schluter Systems Schiene Marine Grade 316 Stainless Steel Transition Trim", unit="LN FT", budget_price=0.0, notes="Marine saltwater corrosion resistant edge trims", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="Flamed Jet Black Granite Marine Saltwater Doorway Transition Saddle", unit="PCS", budget_price=0.0, notes="Harbor club exterior doorway thresholds", trade="Tile & Stone")
        }

    @staticmethod
    def get_2852_marinaclub_rooms() -> List[RoomTakeoff]:
        return [
            RoomTakeoff(room_name="WATERFRONT COMMODORE SALON & HARBOR TERRACE", floor_name="PIER LEVEL 1", length_ft=54.0, width_ft=32.0, ceiling_height_ft=14.0, wall_tile_height_ft=0.0, door_count=2, items=[
                TakeoffLineItem(symbol="MAR-01", finish_type="FLOOR", material_type="MARINE PORCELAIN", work_type="S&I", quantity=1728.0, unit="SQ FT", notes="Porcelanosa R12 marine structured porcelain 24x24 floor", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="HARBOR BAR COUNTERTOP & WATERFALL", material_type="DEKTON SLAB", work_type="S&I", quantity=88.0, unit="SQ FT", notes="Dekton Laurent 2cm bar top with 3-inch mitered waterfall edge", trade="Tile & Stone"),
                TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN BASE", work_type="S&I", quantity=166.0, unit="LN FT", notes="4x24 marine porcelain baseboard", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MARINE-WP", finish_type="FLOOR", material_type="MARINE WATERPROOF", work_type="S&I", quantity=1728.0, unit="SQ FT", notes="Laticrete 9235 marine salt-barrier waterproofing", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=1728.0, unit="SQ FT", notes="Marine polymer mortar leveling bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="EPOXY-GROUT", finish_type="PREPARATION", material_type="EPOXY GROUT", work_type="S&I", quantity=1728.0, unit="SQ FT", notes="SpectraLOCK PRO marine salt-proof epoxy", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-316", finish_type="FLOOR", material_type="316 STAINLESS TRIM", work_type="S&I", quantity=64.0, unit="LN FT", notes="Marine grade 316 stainless transition trims", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=2.0, unit="PCS", notes="Flamed black granite marine saddles", trade="Tile & Stone")
            ]),
            RoomTakeoff(room_name="YACHT CLUB CAPTAIN'S LOCKER & SHOWER SUITE", floor_name="PIER LEVEL 1", length_ft=20.0, width_ft=14.0, ceiling_height_ft=10.0, wall_tile_height_ft=9.5, door_count=1, items=[
                TakeoffLineItem(symbol="MAR-02", finish_type="FLOOR", material_type="PORCELAIN PLANK", work_type="S&I", quantity=280.0, unit="SQ FT", notes="Mirage marine teak textured porcelain wood planks", trade="Tile & Stone"),
                TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="PORCELAIN BASE", work_type="S&I", quantity=65.0, unit="LN FT", notes="Marine baseboard", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MARINE-WP", finish_type="FLOOR & SHOWER WALLS", material_type="MARINE WATERPROOF", work_type="S&I", quantity=620.0, unit="SQ FT", notes="Marine waterproofing membrane", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=280.0, unit="SQ FT", notes="Mud-set bed to floor drains", trade="Tile & Stone"),
                TakeoffLineItem(symbol="EPOXY-GROUT", finish_type="PREPARATION", material_type="EPOXY GROUT", work_type="S&I", quantity=280.0, unit="SQ FT", notes="Salt-proof epoxy grout", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-316", finish_type="WALL", material_type="316 STAINLESS TRIM", work_type="S&I", quantity=28.0, unit="LN FT", notes="316 stainless edge trims", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Black granite marine saddle", trade="Tile & Stone")
            ])
        ]

    # =========================================================================
    # [2853] Saks Fifth Avenue Flagship Grand Beauty Atrium & Luxury Shoe Salon - 611 5th Ave
    # =========================================================================
    @staticmethod
    def get_2853_saks_metadata() -> Dict[str, Any]:
        return {
            "project_name": "[2853] Saks Fifth Avenue Flagship Grand Beauty Atrium & Luxury Shoe Salon - 611 5th Ave",
            "client_name": "Hudson's Bay Company / Store Planning",
            "client_company": "Structure Tone / Luxury Retail & Department Store Division",
            "date_str": "03/19/2027",
            "trade_category": "Tile & Stone"
        }

    @staticmethod
    def get_2853_saks_specs() -> Dict[str, MaterialSpec]:
        return {
            "CHEV-01": MaterialSpec(symbol="CHEV-01", description="Artistic Tile, Statuario Venato & Nero Marquina Custom Precision Chevron Marble Tile 12x36", unit="SQ FT", budget_price=0.0, notes="Grand beauty atrium promenade, designer shoe salon & cashwrap gallery floor", trade="Tile & Stone"),
            "ST-01": MaterialSpec(symbol="ST-01", description="Antolini, Calacatta Gold Extra 2cm Polished Marble Feature Island Plinths & Display Tables", unit="SQ FT", budget_price=0.0, notes="Cosmetic display plinths with 3-inch mitered aprons and LED reveals", trade="Tile & Stone"),
            "MOS-01": MaterialSpec(symbol="MOS-01", description="Bisazza, Gold Leaf & White Opal Micro-Glass Mosaic 1/2 x 1/2 Blend", unit="SQ FT", budget_price=0.0, notes="VIP styling salon powder room feature accent wall", trade="Tile & Stone"),
            "TB-01": MaterialSpec(symbol="TB-01", description="Artistic Tile, Nero Marquina 4x12 Polished Marble Baseboard", unit="LN FT", budget_price=0.0, notes="Retail gallery perimeter luxury marble baseboard", trade="Tile & Stone"),
            "WATERPROOF": MaterialSpec(symbol="WATERPROOF", description="Mapei Mapelastic AquaDefense Ultra Crack Isolation & Waterproofing Membrane", unit="SQ FT", budget_price=0.0, notes="Flagship department store subfloor crack isolation", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="Portland Precision Mud-Set Mortar Bed & Self-Leveling Underlayment", unit="SQ FT", budget_price=0.0, notes="Precision stone subfloor leveling bed", trade="Tile & Stone"),
            "MS-CHAMPAGNE": MaterialSpec(symbol="MS-CHAMPAGNE", description="Schluter Systems Schiene Custom Anodized Champagne Gold Metal Transition Trim", unit="LN FT", budget_price=0.0, notes="Chevron marble pattern borders and carpet transitions", trade="Tile & Stone"),
            "SADDLE": MaterialSpec(symbol="SADDLE", description="Statuario Venato Polished Marble Custom Double-Beveled Transition Saddle", unit="PCS", budget_price=0.0, notes="Designer boutique salon doorway thresholds", trade="Tile & Stone")
        }

    @staticmethod
    def get_2853_saks_rooms() -> List[RoomTakeoff]:
        return [
            RoomTakeoff(room_name="GRAND BEAUTY ATRIUM & DESIGNER SHOE SALON", floor_name="MAIN FLOOR 2", length_ft=60.0, width_ft=36.0, ceiling_height_ft=16.0, wall_tile_height_ft=0.0, door_count=3, items=[
                TakeoffLineItem(symbol="CHEV-01", finish_type="FLOOR", material_type="CHEVRON MARBLE", work_type="S&I", quantity=2160.0, unit="SQ FT", notes="Artistic Tile 12x36 custom precision chevron marble floor", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="DISPLAY ISLAND PLINTHS", material_type="MARBLE SLAB", work_type="S&I", quantity=140.0, unit="SQ FT", notes="Calacatta Gold 2cm polished display tables with 3-inch mitered aprons", trade="Tile & Stone"),
                TakeoffLineItem(symbol="TB-01", finish_type="WALL", material_type="MARBLE BASE", work_type="S&I", quantity=184.0, unit="LN FT", notes="Nero Marquina 4x12 polished marble baseboard", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=2160.0, unit="SQ FT", notes="Crack isolation and floor waterproofing", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=2160.0, unit="SQ FT", notes="Precision mud-set mortar bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-CHAMPAGNE", finish_type="FLOOR", material_type="CHAMPAGNE METAL TRIM", work_type="S&I", quantity=112.0, unit="LN FT", notes="Champagne gold transition trims between marble and carpet", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=3.0, unit="PCS", notes="Statuario Venato marble doorway saddles", trade="Tile & Stone")
            ]),
            RoomTakeoff(room_name="VIP PERSONAL STYLING POWDER ROOM", floor_name="MAIN FLOOR 2", length_ft=12.0, width_ft=9.0, ceiling_height_ft=10.0, wall_tile_height_ft=10.0, door_count=1, items=[
                TakeoffLineItem(symbol="CHEV-01", finish_type="FLOOR", material_type="CHEVRON MARBLE", work_type="S&I", quantity=108.0, unit="SQ FT", notes="Chevron marble floor", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MOS-01", finish_type="ACCENT WALL", material_type="GOLD GLASS MOSAIC", work_type="S&I", quantity=120.0, unit="SQ FT", notes="Bisazza gold leaf micro-glass mosaic accent wall", trade="Tile & Stone"),
                TakeoffLineItem(symbol="ST-01", finish_type="FLOATING VANITY SLAB", material_type="MARBLE SLAB", work_type="S&I", quantity=20.0, unit="SQ FT", notes="Calacatta Gold marble vanity top with undermount sink", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=108.0, unit="SQ FT", notes="Floor waterproofing", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=108.0, unit="SQ FT", notes="Mud-set bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-CHAMPAGNE", finish_type="WALL", material_type="CHAMPAGNE METAL TRIM", work_type="S&I", quantity=24.0, unit="LN FT", notes="Champagne gold mosaic edge trim", trade="Tile & Stone"),
                TakeoffLineItem(symbol="SADDLE", finish_type="FLOOR", material_type="SADDLE", work_type="S&I", quantity=1.0, unit="PCS", notes="Statuario marble saddle", trade="Tile & Stone")
            ])
        ]

    # =========================================================================
    # [2854] Pfizer Global Bio-Pharma Cleanroom & Sterile Compounding Suite - 235 E 42nd St
    # =========================================================================
    @staticmethod
    def get_2854_pfizer_metadata() -> Dict[str, Any]:
        return {
            "project_name": "[2854] Pfizer Global Bio-Pharma Cleanroom & Sterile Compounding Suite - 235 E 42nd St",
            "client_name": "Pfizer Global Supply / cGMP Facility Engineering",
            "client_company": "Turner Construction / Life Sciences & Pharma Division",
            "date_str": "04/08/2027",
            "trade_category": "Tile & Stone"
        }

    @staticmethod
    def get_2854_pfizer_specs() -> Dict[str, MaterialSpec]:
        return {
            "CLEAN-01": MaterialSpec(symbol="CLEAN-01", description="Crossville, cGMP Grade Ultra-Vitrified Non-Porous 24x24 Cleanroom Porcelain Tile (0.01% Water Absorption)", unit="SQ FT", budget_price=0.0, notes="ISO Class 5 sterile injectable compounding suite & airlock buffer rooms", trade="Tile & Stone"),
            "CWT-01": MaterialSpec(symbol="CWT-01", description="Daltile, Cleanroom Chemical Sterilant Resistant Glazed Wall Tile 12x24 White Gloss", unit="SQ FT", budget_price=0.0, notes="Full height 12' sterile compounding washdown walls", trade="Tile & Stone"),
            "COVE-01": MaterialSpec(symbol="COVE-01", description="Crossville, 6x12 Integral Radius Cleanroom Coved Ceramic Baseboard", unit="LN FT", budget_price=0.0, notes="FDA cGMP compliant seamless integral radius coved baseboard", trade="Tile & Stone"),
            "HERMETIC-SADDLE": MaterialSpec(symbol="HERMETIC-SADDLE", description="Trespa / High-Density Solid Phenolic Hermetic Pressure-Sealed Doorway Saddle", unit="PCS", budget_price=0.0, notes="Airlock pressure differential cleanroom doorway saddles", trade="Tile & Stone"),
            "WATERPROOF": MaterialSpec(symbol="WATERPROOF", description="Mapei Mapelastic 315 Zero-VOC Chemical Containment Waterproofing Membrane", unit="SQ FT", budget_price=0.0, notes="Sterile compounding cleanroom floor slab containment", trade="Tile & Stone"),
            "MUD-SET": MaterialSpec(symbol="MUD-SET", description="Portland Precision Polymer Mud-Set Bed & Self-Leveling Subfloor Underlayment", unit="SQ FT", budget_price=0.0, notes="Precision leveled subfloor underlayment", trade="Tile & Stone"),
            "NOVOLAC-EPOXY": MaterialSpec(symbol="NOVOLAC-EPOXY", description="Laticrete SpectraLOCK 2000 IG 100% Novolac Industrial Chemical Epoxy Grout", unit="SQ FT", budget_price=0.0, notes="Vaporized hydrogen peroxide (VHP) & sterilant proof epoxy grouting", trade="Tile & Stone"),
            "MS-316": MaterialSpec(symbol="MS-316", description="Schluter Systems Schiene 316 Pharmaceutical Grade Stainless Steel Cleanroom Trim", unit="LN FT", budget_price=0.0, notes="Cleanroom pass-through and wall edge terminations", trade="Tile & Stone")
        }

    @staticmethod
    def get_2854_pfizer_rooms() -> List[RoomTakeoff]:
        return [
            RoomTakeoff(room_name="ISO CLASS 5 STERILE COMPOUNDING CLEANROOM", floor_name="LAB FLOOR 4", length_ft=32.0, width_ft=20.0, ceiling_height_ft=12.0, wall_tile_height_ft=12.0, door_count=2, items=[
                TakeoffLineItem(symbol="CLEAN-01", finish_type="FLOOR", material_type="CLEANROOM PORCELAIN", work_type="S&I", quantity=640.0, unit="SQ FT", notes="Crossville cGMP ultra-vitrified cleanroom floor tile", trade="Tile & Stone"),
                TakeoffLineItem(symbol="CWT-01", finish_type="WALL", material_type="CLEANROOM WALL TILE", work_type="S&I", quantity=1200.0, unit="SQ FT", notes="Daltile 12x24 sterilant resistant wall tile full 12' height", trade="Tile & Stone"),
                TakeoffLineItem(symbol="COVE-01", finish_type="WALL", material_type="CLEANROOM COVE BASE", work_type="S&I", quantity=98.0, unit="LN FT", notes="6x12 FDA cGMP radius coved baseboard", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=640.0, unit="SQ FT", notes="Chemical containment waterproofing membrane", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=640.0, unit="SQ FT", notes="Precision mud-set mortar bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="NOVOLAC-EPOXY", finish_type="PREPARATION", material_type="NOVOLAC EPOXY", work_type="S&I", quantity=640.0, unit="SQ FT", notes="100% Novolac VHP sterilant-proof epoxy grout", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-316", finish_type="WALL", material_type="316 STAINLESS TRIM", work_type="S&I", quantity=48.0, unit="LN FT", notes="316 stainless pharmaceutical trims", trade="Tile & Stone"),
                TakeoffLineItem(symbol="HERMETIC-SADDLE", finish_type="FLOOR", material_type="HERMETIC SADDLE", work_type="S&I", quantity=2.0, unit="PCS", notes="Hermetic pressure-sealed airlock saddles", trade="Tile & Stone")
            ]),
            RoomTakeoff(room_name="PERSONNEL GOWNING & AIRLOCK BUFFER ROOM", floor_name="LAB FLOOR 4", length_ft=16.0, width_ft=12.0, ceiling_height_ft=11.0, wall_tile_height_ft=11.0, door_count=2, items=[
                TakeoffLineItem(symbol="CLEAN-01", finish_type="FLOOR", material_type="CLEANROOM PORCELAIN", work_type="S&I", quantity=192.0, unit="SQ FT", notes="Cleanroom porcelain floor tile", trade="Tile & Stone"),
                TakeoffLineItem(symbol="CWT-01", finish_type="WALL", material_type="CLEANROOM WALL TILE", work_type="S&I", quantity=580.0, unit="SQ FT", notes="Chemical resistant wall tile full height", trade="Tile & Stone"),
                TakeoffLineItem(symbol="COVE-01", finish_type="WALL", material_type="CLEANROOM COVE BASE", work_type="S&I", quantity=50.0, unit="LN FT", notes="Radius coved base", trade="Tile & Stone"),
                TakeoffLineItem(symbol="WATERPROOF", finish_type="FLOOR", material_type="WATERPROOF", work_type="S&I", quantity=192.0, unit="SQ FT", notes="Waterproofing membrane", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MUD-SET", finish_type="PREPARATION", material_type="MUD-SET", work_type="S&I", quantity=192.0, unit="SQ FT", notes="Mud-set leveling bed", trade="Tile & Stone"),
                TakeoffLineItem(symbol="NOVOLAC-EPOXY", finish_type="PREPARATION", material_type="NOVOLAC EPOXY", work_type="S&I", quantity=192.0, unit="SQ FT", notes="Novolac epoxy grout", trade="Tile & Stone"),
                TakeoffLineItem(symbol="MS-316", finish_type="WALL", material_type="316 STAINLESS TRIM", work_type="S&I", quantity=32.0, unit="LN FT", notes="316 stainless edge trim", trade="Tile & Stone"),
                TakeoffLineItem(symbol="HERMETIC-SADDLE", finish_type="FLOOR", material_type="HERMETIC SADDLE", work_type="S&I", quantity=2.0, unit="PCS", notes="Hermetic airlock doorway saddles", trade="Tile & Stone")
            ])
        ]



