import datetime
from typing import Dict, List
from ..trades.trade_base import ProjectTakeoff, RoomTakeoff, TakeoffLineItem, MaterialSpec

def get_penn1_project() -> ProjectTakeoff:
    """
    Returns the complete takeoff for PENN 1 (One Penn Plaza, NY):
    - 6th Floor Restrooms & Corridors
    - 32nd Floor Restrooms & Corridors
    - 33rd Floor Restrooms & Corridors
    Incorporating Scope Clarifications:
    1) Minor floor prep included across all trades and areas.
    2) Stone wall panels (ST-2) full height to underside of beams at elevator lobbies (10'-0" AFF).
    3) All typical drinking fountain alcoves receive ST-1 floor & SB-1 base (except single fountain outside 6th fl unisex RR).
    """
    specs: Dict[str, MaterialSpec] = {
        "ST-01": MaterialSpec(
            symbol="ST-01",
            description="TileBar Rift, Color: Graffito, 32\"x32\"x11mm Stone Tile Flooring, Monolithic, Grout: Laticrete Dusty Grey #60 (1/8\" spacer)",
            manufacturer="TileBar",
            collection="Rift",
            size="32\"x32\"",
            finish="Matte",
            color="Graffito",
            unit="SQ FT",
            budget_price=13.50,
            notes="Restroom floor tile. Mfr Contact: Rhys Rogers (212) 246-4149 ext 032",
            trade="Tile & Stone"
        ),
        "TL-01": MaterialSpec(
            symbol="TL-01",
            description="Nemo Towne, Color: Ivory Craquele TOW12.510, 2.5\"x10\"x3/8\" Ceramic Wall Tile, Vertical Stackbond, Grout: Laticrete Sauterne (1/16\" spacer)",
            manufacturer="Nemo Tile",
            collection="Towne",
            size="2.5\"x10\"",
            finish="Craquele Gloss",
            color="Ivory Craquele",
            unit="SQ FT",
            budget_price=11.09,
            notes="Restroom walls throughout to 8'-6\" AFF. Mfr Contact: Akilah Hoyte (212) 505-0009 ext 328",
            trade="Tile & Stone"
        ),
        "TL-02": MaterialSpec(
            symbol="TL-02",
            description="Stone Source Wig Wag Tile 4100321, Color: Black, 3\"x6\"x11mm Ceramic Tile, Stackbond Random, Grout: Laticrete Midnight Black (1/16\" spacer)",
            manufacturer="Stone Source",
            collection="Wig Wag",
            size="3\"x6\"",
            finish="Textured Gloss",
            color="Black",
            unit="SQ FT",
            budget_price=13.40,
            notes="Restroom vanity accent wall full height. Mfr Contact: Brant Abrams (212) 979-6400",
            trade="Tile & Stone"
        ),
        "ST-02": MaterialSpec(
            symbol="ST-02",
            description="ST-1: Porcelanosa Bottega Caliza 100323039, 32\"x32\"x5/16\" Stone Tile Flooring, Mudset Installation, Grout: Laticrete 90 Light Pewter",
            manufacturer="Porcelanosa",
            collection="Bottega Caliza",
            size="32\"x32\"",
            finish="Honed",
            color="Caliza",
            unit="SQ FT",
            budget_price=15.50,
            notes="Elevator lobby stone floor & typical drinking fountain alcoves (ST-1). Mfr: Natalie Severo (646) 751-1180",
            trade="Tile & Stone"
        ),
        "SB-01": MaterialSpec(
            symbol="SB-01",
            description="SB-1: Porcelanosa Bottega Caliza 100323039, 4\" High Stone Tile Base cut from 32\"x32\" tile in field, Thinset Installation, Grout: Laticrete 90 Light Pewter",
            manufacturer="Porcelanosa",
            collection="Bottega Caliza",
            size="4\" High",
            finish="Honed",
            color="Caliza",
            unit="LNFT",
            budget_price=8.50,
            notes="Stone tile base at typical drinking fountain alcoves (SB-1).",
            trade="Tile & Stone"
        ),
        "ST-03": MaterialSpec(
            symbol="ST-03",
            description="ST-2: Florim Metal 759809, Color: Metal Burnished, 63\"x126\"x6mm (1/4\") Stone Wall Cladding Panels, Thinset, Grout: Laticrete 45 Raven",
            manufacturer="Florim",
            collection="Metal",
            size="63\"x126\"",
            finish="Burnished",
            color="Metal Burnished",
            unit="SQ FT",
            budget_price=24.00,
            notes="Elevator lobby core walls ST-2 panels full height to underside of beams (10'-0\" AFF). Mfr: Marco Mastrandrea (931) 401-6774",
            trade="Tile & Stone"
        ),
        "CPT-01": MaterialSpec(
            symbol="CPT-01",
            description="Bentley Ritual 8RR26, Color: Folkways 800223, Broadloom Carpet, Glue-Down HP High Performance (Alt #3: 18x36 Carpet Tile Ashlar)",
            manufacturer="Bentley",
            collection="Ritual",
            size="Broadloom / 18\"x36\"",
            finish="Tufted Textured Loop",
            color="Folkways 800223",
            unit="SQ FT",
            budget_price=4.50,
            notes="Public circulation corridors & freight lobby. Mfr Contact: Wendy Jorgensen (201) 310-7069",
            trade="Flooring & Wood"
        ),
        "SS-01": MaterialSpec(
            symbol="SS-01",
            description="Cambria Quartz Countertop, Color: Blackpool Matte, 2cm Custom Cut Slab with Undermount Sink Cutouts & Finished Edges",
            manufacturer="Cambria",
            collection="Quartz",
            size="2cm Slab",
            finish="Matte",
            color="Blackpool Matte",
            unit="SQ FT",
            budget_price=43.45,
            notes="Restroom custom lavatory vanity counters.",
            trade="Tile & Stone"
        ),
        "SDL-01": MaterialSpec(
            symbol="SDL-01",
            description="Black Granite Marble Saddle / Threshold, 3'-0\" x 6\" x 3/4\" Beveled Edges, Polished Finish",
            manufacturer="Custom / Fabricator",
            collection="Granite Thresholds",
            size="3'-0\" x 6\"",
            finish="Polished",
            color="Black Granite",
            unit="PCS",
            budget_price=45.00,
            notes="Restroom entrance doorways transition saddle.",
            trade="Tile & Stone"
        ),
        "TRIM-01": MaterialSpec(
            symbol="TRIM-01",
            description="Schluter-QUADEC-10-Q100EB, Aluminum / Sand Pebble (SP), Full-Height Outside Corner Metal Tile Profile",
            manufacturer="Schluter",
            collection="Quadec-10",
            size="3/8\" x 8'-2.5\"",
            finish="Sand Pebble",
            color="SP",
            unit="LNFT",
            budget_price=4.50,
            notes="Vertical outside corners of restroom wet walls and stall returns.",
            trade="Tile & Stone"
        ),
        "TRIM-02": MaterialSpec(
            symbol="TRIM-02",
            description="Schluter Schiene AE160 5/8\" Metal Angle Transition Strip Secured to Slab",
            manufacturer="Schluter",
            collection="Schiene",
            size="5/8\"",
            finish="Anodized Aluminum",
            color="Aluminum",
            unit="LNFT",
            budget_price=5.50,
            notes="Transition detail between Elevator Lobby Stone Tile and Corridor Carpet.",
            trade="Tile & Stone"
        ),
        "TRIM-03": MaterialSpec(
            symbol="TRIM-03",
            description="Schluter Reno-U-AEU150 Metal Angle Transition Strip Secured to Slab",
            manufacturer="Schluter",
            collection="Reno-U",
            size="1/2\"",
            finish="Anodized Aluminum",
            color="Aluminum",
            unit="LNFT",
            budget_price=5.50,
            notes="Transition detail between Polished Concrete and Corridor Carpet.",
            trade="Flooring & Wood"
        ),
        "VB-01": MaterialSpec(
            symbol="VB-01",
            description="Tarkett 4\" Millwork Wallbase Reveal, Color: 40 Black (Freight: 24 Gray Haze)",
            manufacturer="Tarkett",
            collection="Millwork Wallbase",
            size="4\" High",
            finish="Matte",
            color="40 Black",
            unit="LNFT",
            budget_price=2.20,
            notes="Perimeter base at all carpeted corridors and lobbies.",
            trade="Flooring & Wood"
        ),
        "WP-01": MaterialSpec(
            symbol="WP-01",
            description="Laticrete Hydro Ban Waterproofing and Anti-Fracture Membrane (Liquid Applied)",
            manufacturer="Laticrete",
            collection="Hydro Ban",
            size="Continuous",
            finish="Liquid Applied",
            color="Olive Green",
            unit="SQ FT",
            budget_price=2.50,
            notes="Restroom slab waterproofing under stone tile flooring.",
            trade="Tile & Stone"
        ),
        "MUD-01": MaterialSpec(
            symbol="MUD-01",
            description="Thick-Bed Portland Cement Sand Mudset Bed (1-1/4\" to 1-1/2\" wire mesh reinforced)",
            manufacturer="Laticrete / SpecChem",
            collection="Mortar Bed",
            size="1.5\" Bed",
            finish="Troweled",
            color="Grey",
            unit="SQ FT",
            budget_price=3.50,
            notes="Required under 32\"x32\" stone tile in restrooms & elevator lobbies.",
            trade="Tile & Stone"
        ),
        "PREP-01": MaterialSpec(
            symbol="PREP-01",
            description="Minor Floor Prep: Mechanical scraping, substrate cleaning, divot patching & polymer-modified flash-patching (up to 1/8\")",
            manufacturer="Ardex / Mapei",
            collection="Feather Finish / Planiprep",
            size="Substrate Level",
            finish="Smooth Troweled",
            color="Grey",
            unit="SQ FT",
            budget_price=0.95,
            notes="Minor floor prep per industry standards ANSI A108 / ASTM F710 before flooring installation.",
            trade="Tile & Stone"
        )
    }

    def build_restroom_items(floor_str: str, is_mens: bool) -> List[TakeoffLineItem]:
        fl_sf = 373.3 if is_mens else 357.7
        vanity_w = 7.58 if is_mens else 7.75
        vanity_sf = round(vanity_w * 8.5, 1)
        wall_sf = 570.0 if is_mens else 548.0
        counter_sf = 15.2 if is_mens else 15.5
        
        items = [
            TakeoffLineItem(
                symbol="PREP-01",
                finish_type="FLOOR PREP",
                material_type="SUBSTRATE PREPARATION",
                work_type="S&I",
                quantity=fl_sf,
                unit="SQ FT",
                material_price=0.95,
                labor_price=1.25,
                notes=f"{floor_str} Minor Floor Prep: Concrete substrate cleaning, grinding & flash-patching",
                trade="Tile & Stone"
            ),
            TakeoffLineItem(
                symbol="WP-01",
                finish_type="FLOOR PREP",
                material_type="WATERPROOFING",
                work_type="S&I",
                quantity=fl_sf,
                unit="SQ FT",
                material_price=2.50,
                labor_price=2.50,
                notes="Liquid Applied Waterproofing & Crack Isolation (Laticrete Hydro Ban)",
                trade="Tile & Stone"
            ),
            TakeoffLineItem(
                symbol="MUD-01",
                finish_type="FLOOR PREP",
                material_type="MUDSET BED",
                work_type="S&I",
                quantity=fl_sf,
                unit="SQ FT",
                material_price=3.50,
                labor_price=5.50,
                notes="Thick Bed Portland Sand Mortar Bed with Welded Wire Mesh",
                trade="Tile & Stone"
            ),
            TakeoffLineItem(
                symbol="ST-01",
                finish_type="FLOOR",
                material_type="STONE TILE",
                work_type="S&I",
                quantity=fl_sf,
                unit="SQ FT",
                material_price=13.50,
                labor_price=14.50,
                notes=f"{floor_str} Restroom Floor Stone Tile (TileBar Rift 32\"x32\")",
                trade="Tile & Stone"
            ),
            TakeoffLineItem(
                symbol="TL-01",
                finish_type="WALL",
                material_type="CERAMIC TILE",
                work_type="S&I",
                quantity=wall_sf,
                unit="SQ FT",
                material_price=11.09,
                labor_price=16.00,
                notes="General Restroom Wall Tile to 8'-6\" AFF (Nemo Towne 2.5\"x10\")",
                trade="Tile & Stone"
            ),
            TakeoffLineItem(
                symbol="TL-02",
                finish_type="WALL",
                material_type="CERAMIC ACCENT TILE",
                work_type="S&I",
                quantity=vanity_sf,
                unit="SQ FT",
                material_price=13.40,
                labor_price=18.50,
                notes="Vanity Accent Wall Tile Full Height (Stone Source Wig Wag 3\"x6\")",
                trade="Tile & Stone"
            ),
            TakeoffLineItem(
                symbol="SS-01",
                finish_type="COUNTERTOP",
                material_type="QUARTZ",
                work_type="S&I",
                quantity=counter_sf,
                unit="SQ FT",
                material_price=43.45,
                labor_price=55.00,
                notes="Cambria Blackpool Matte 2cm Quartz Lavatory Countertop",
                trade="Tile & Stone"
            ),
            TakeoffLineItem(
                symbol="SDL-01",
                finish_type="THRESHOLD",
                material_type="MARBLE SADDLE",
                work_type="S&I",
                quantity=1.0,
                unit="PCS",
                material_price=45.00,
                labor_price=55.00,
                notes="Black Granite Marble Saddle at Entryway (3'-0\" x 6\")",
                trade="Tile & Stone"
            ),
            TakeoffLineItem(
                symbol="TRIM-01",
                finish_type="TRIM",
                material_type="METAL TRIM",
                work_type="S&I",
                quantity=51.0,
                unit="LNFT",
                material_price=4.50,
                labor_price=6.50,
                notes="Schluter Quadec-10 Outside Corner Aluminum Sand Pebble Trim",
                trade="Tile & Stone"
            )
        ]
        return items

    def build_corridor_items(floor_str: str, is_floor_6: bool) -> List[TakeoffLineItem]:
        carpet_sf = 2153.0 if is_floor_6 else 1258.0
        base_lf = 480.0 if is_floor_6 else 310.0
        
        items = [
            TakeoffLineItem(
                symbol="PREP-01",
                finish_type="FLOOR PREP",
                material_type="SUBSTRATE PREPARATION",
                work_type="S&I",
                quantity=carpet_sf,
                unit="SQ FT",
                material_price=0.75,
                labor_price=0.95,
                notes=f"{floor_str} Minor Floor Prep: Scrape, sweep, flash-patch substrate for carpet",
                trade="Flooring & Wood"
            ),
            TakeoffLineItem(
                symbol="CPT-01",
                finish_type="FLOOR",
                material_type="CARPET",
                work_type="S&I",
                quantity=carpet_sf,
                unit="SQ FT",
                material_price=4.50,
                labor_price=3.50,
                notes=f"{floor_str} Public Corridors Bentley Ritual Broadloom / Tile Carpet",
                trade="Flooring & Wood"
            ),
            TakeoffLineItem(
                symbol="VB-01",
                finish_type="BASE",
                material_type="VINYL BASE",
                work_type="S&I",
                quantity=base_lf,
                unit="LNFT",
                material_price=2.20,
                labor_price=2.30,
                notes="Tarkett 4\" Millwork Wallbase Reveal (Black / Gray Haze)",
                trade="Flooring & Wood"
            ),
            TakeoffLineItem(
                symbol="TRIM-03",
                finish_type="TRANSITION",
                material_type="METAL TRIM",
                work_type="S&I",
                quantity=18.0,
                unit="LNFT",
                material_price=5.50,
                labor_price=6.50,
                notes="Schluter Reno-U-AEU150 Metal Angle Transition (Concrete to Carpet)",
                trade="Flooring & Wood"
            )
        ]
        return items

    def build_elevator_lobby_items(floor_str: str) -> List[TakeoffLineItem]:
        # Stone wall panels full height to underside of beams (10'-0" AFF)
        # Gross perimeter: 85 LF x 10.0' = 850 SF gross - 196 SF door openings = 654.0 SF Net
        lobby_floor_sf = 448.0
        lobby_wall_sf = 654.0
        
        items = [
            TakeoffLineItem(
                symbol="PREP-01",
                finish_type="FLOOR PREP",
                material_type="SUBSTRATE PREPARATION",
                work_type="S&I",
                quantity=lobby_floor_sf,
                unit="SQ FT",
                material_price=0.95,
                labor_price=1.25,
                notes=f"{floor_str} Elevator Lobby Minor Floor Prep & Scarifying under Mudset Bed",
                trade="Tile & Stone"
            ),
            TakeoffLineItem(
                symbol="MUD-01",
                finish_type="FLOOR PREP",
                material_type="MUDSET BED",
                work_type="S&I",
                quantity=lobby_floor_sf,
                unit="SQ FT",
                material_price=3.50,
                labor_price=5.50,
                notes="Thick Bed Mudset Mortar Bed at Elevator Lobby",
                trade="Tile & Stone"
            ),
            TakeoffLineItem(
                symbol="ST-02",
                finish_type="FLOOR",
                material_type="STONE TILE",
                work_type="S&I",
                quantity=lobby_floor_sf,
                unit="SQ FT",
                material_price=15.50,
                labor_price=17.50,
                notes=f"{floor_str} Elevator Lobby Porcelanosa Bottega Caliza 32\"x32\" Stone Floor",
                trade="Tile & Stone"
            ),
            TakeoffLineItem(
                symbol="ST-03",
                finish_type="WALL",
                material_type="STONE WALL CLADDING",
                work_type="S&I",
                quantity=lobby_wall_sf,
                unit="SQ FT",
                material_price=24.00,
                labor_price=26.00,
                notes=f"{floor_str} Elevator Lobby Florim 63\"x126\" Stone Panels ST-2 (Full Height to Underside of Beams @ 10'-0\" AFF)",
                trade="Tile & Stone"
            ),
            TakeoffLineItem(
                symbol="TRIM-02",
                finish_type="TRANSITION",
                material_type="METAL TRIM",
                work_type="S&I",
                quantity=16.0,
                unit="LNFT",
                material_price=5.50,
                labor_price=6.50,
                notes="Schluter Schiene AE160 Metal Transition Angle (Stone to Carpet)",
                trade="Tile & Stone"
            )
        ]
        return items

    def build_drinking_fountain_items(floor_str: str) -> List[TakeoffLineItem]:
        # Typical drinking fountain alcove: ST-1 floor (20 SF) and SB-1 base (14 LF)
        items = [
            TakeoffLineItem(
                symbol="PREP-01",
                finish_type="FLOOR PREP",
                material_type="SUBSTRATE PREPARATION",
                work_type="S&I",
                quantity=20.0,
                unit="SQ FT",
                material_price=0.95,
                labor_price=1.25,
                notes=f"{floor_str} Drinking Fountain Alcove Minor Floor Prep",
                trade="Tile & Stone"
            ),
            TakeoffLineItem(
                symbol="ST-02",
                finish_type="FLOOR",
                material_type="STONE TILE",
                work_type="S&I",
                quantity=20.0,
                unit="SQ FT",
                material_price=15.50,
                labor_price=17.50,
                notes=f"{floor_str} Drinking Fountain Alcove Stone Floor (ST-1: Porcelanosa Bottega Caliza 32\"x32\")",
                trade="Tile & Stone"
            ),
            TakeoffLineItem(
                symbol="SB-01",
                finish_type="BASE",
                material_type="STONE BASE",
                work_type="S&I",
                quantity=14.0,
                unit="LNFT",
                material_price=8.50,
                labor_price=9.50,
                notes=f"{floor_str} Drinking Fountain Alcove 4\" Stone Base (SB-1: Porcelanosa Bottega Caliza)",
                trade="Tile & Stone"
            ),
            TakeoffLineItem(
                symbol="TRIM-02",
                finish_type="TRANSITION",
                material_type="METAL TRIM",
                work_type="S&I",
                quantity=6.0,
                unit="LNFT",
                material_price=5.50,
                labor_price=6.50,
                notes="Schluter Schiene AE160 Transition at Fountain Alcove Edge",
                trade="Tile & Stone"
            )
        ]
        return items

    rooms: List[RoomTakeoff] = [
        # 6th Floor Restrooms
        RoomTakeoff(
            room_name="MEN'S RESTROOM 6.01",
            floor_name="6TH FLOOR",
            length_ft=25.17,
            width_ft=14.83,
            ceiling_height_ft=8.5,
            wall_tile_height_ft=8.5,
            door_count=1,
            door_width_ft=3.0,
            door_height_ft=7.0,
            items=build_restroom_items("6th Floor", is_mens=True)
        ),
        RoomTakeoff(
            room_name="WOMEN'S RESTROOM 6.07",
            floor_name="6TH FLOOR",
            length_ft=22.83,
            width_ft=15.67,
            ceiling_height_ft=8.5,
            wall_tile_height_ft=8.5,
            door_count=1,
            door_width_ft=3.0,
            door_height_ft=7.0,
            items=build_restroom_items("6th Floor", is_mens=False)
        ),
        # 6th Floor Elevator Lobby & Corridors
        RoomTakeoff(
            room_name="ELEVATOR LOBBY 6.00",
            floor_name="6TH FLOOR",
            length_ft=34.8,
            width_ft=12.3,
            ceiling_height_ft=10.0,
            wall_tile_height_ft=10.0,
            door_count=2,
            door_width_ft=6.0,
            door_height_ft=7.0,
            items=build_elevator_lobby_items("6th Floor")
        ),
        RoomTakeoff(
            room_name="DRINKING FOUNTAIN ALCOVE (TYP.) 6.00",
            floor_name="6TH FLOOR",
            length_ft=6.0,
            width_ft=3.33,
            ceiling_height_ft=8.5,
            wall_tile_height_ft=0.0,
            door_count=0,
            items=build_drinking_fountain_items("6th Floor")
        ),
        RoomTakeoff(
            room_name="CIRCULATION CORRIDORS (6.01, 6.02, 6.05, 6.06 & FREIGHT 6.03)",
            floor_name="6TH FLOOR",
            length_ft=120.0,
            width_ft=18.0,
            ceiling_height_ft=9.0,
            wall_tile_height_ft=0.0,
            door_count=8,
            items=build_corridor_items("6th Floor", is_floor_6=True)
        ),

        # 32nd Floor Restrooms
        RoomTakeoff(
            room_name="MEN'S RESTROOM 32.01",
            floor_name="32ND FLOOR",
            length_ft=25.17,
            width_ft=14.83,
            ceiling_height_ft=8.5,
            wall_tile_height_ft=8.5,
            door_count=1,
            door_width_ft=3.0,
            door_height_ft=7.0,
            items=build_restroom_items("32nd Floor", is_mens=True)
        ),
        RoomTakeoff(
            room_name="WOMEN'S RESTROOM 32.02",
            floor_name="32ND FLOOR",
            length_ft=22.83,
            width_ft=15.67,
            ceiling_height_ft=8.5,
            wall_tile_height_ft=8.5,
            door_count=1,
            door_width_ft=3.0,
            door_height_ft=7.0,
            items=build_restroom_items("32nd Floor", is_mens=False)
        ),
        # 32nd Floor Elevator Lobby, Alcove & Corridors
        RoomTakeoff(
            room_name="ELEVATOR LOBBY 32.00",
            floor_name="32ND FLOOR",
            length_ft=34.8,
            width_ft=12.3,
            ceiling_height_ft=10.0,
            wall_tile_height_ft=10.0,
            door_count=2,
            door_width_ft=6.0,
            door_height_ft=7.0,
            items=build_elevator_lobby_items("32nd Floor")
        ),
        RoomTakeoff(
            room_name="DRINKING FOUNTAIN ALCOVE (TYP.) 32.00",
            floor_name="32ND FLOOR",
            length_ft=6.0,
            width_ft=3.33,
            ceiling_height_ft=8.5,
            wall_tile_height_ft=0.0,
            door_count=0,
            items=build_drinking_fountain_items("32nd Floor")
        ),
        RoomTakeoff(
            room_name="CIRCULATION CORRIDORS (32.01, 32.02 & FREIGHT 32.03)",
            floor_name="32ND FLOOR",
            length_ft=70.0,
            width_ft=18.0,
            ceiling_height_ft=9.0,
            wall_tile_height_ft=0.0,
            door_count=6,
            items=build_corridor_items("32nd Floor", is_floor_6=False)
        ),

        # 33rd Floor Restrooms
        RoomTakeoff(
            room_name="MEN'S RESTROOM 33.01",
            floor_name="33RD FLOOR",
            length_ft=25.17,
            width_ft=14.83,
            ceiling_height_ft=8.5,
            wall_tile_height_ft=8.5,
            door_count=1,
            door_width_ft=3.0,
            door_height_ft=7.0,
            items=build_restroom_items("33rd Floor", is_mens=True)
        ),
        RoomTakeoff(
            room_name="WOMEN'S RESTROOM 33.02",
            floor_name="33RD FLOOR",
            length_ft=22.83,
            width_ft=15.67,
            ceiling_height_ft=8.5,
            wall_tile_height_ft=8.5,
            door_count=1,
            door_width_ft=3.0,
            door_height_ft=7.0,
            items=build_restroom_items("33rd Floor", is_mens=False)
        ),
        # 33rd Floor Elevator Lobby, Alcove & Corridors
        RoomTakeoff(
            room_name="ELEVATOR LOBBY 33.00",
            floor_name="33RD FLOOR",
            length_ft=34.8,
            width_ft=12.3,
            ceiling_height_ft=10.0,
            wall_tile_height_ft=10.0,
            door_count=2,
            door_width_ft=6.0,
            door_height_ft=7.0,
            items=build_elevator_lobby_items("33rd Floor")
        ),
        RoomTakeoff(
            room_name="DRINKING FOUNTAIN ALCOVE (TYP.) 33.00",
            floor_name="33RD FLOOR",
            length_ft=6.0,
            width_ft=3.33,
            ceiling_height_ft=8.5,
            wall_tile_height_ft=0.0,
            door_count=0,
            items=build_drinking_fountain_items("33rd Floor")
        ),
        RoomTakeoff(
            room_name="CIRCULATION CORRIDORS (33.01, 33.02 & FREIGHT 33.03)",
            floor_name="33RD FLOOR",
            length_ft=70.0,
            width_ft=18.0,
            ceiling_height_ft=9.0,
            wall_tile_height_ft=0.0,
            door_count=6,
            items=build_corridor_items("33rd Floor", is_floor_6=False)
        )
    ]

    exclusions = [
        "1) Demolition of existing floors and core partitions (by Demolition Subcontractor).",
        "2) Subfloor structural framing and concrete slab structural infills by others.",
        "3) Moisture mitigation / calcium chloride testing unless specifically contracted.",
        "4) Premium / Overtime labor unless authorized in writing.",
        "5) Architectural access doors and MEP cleanouts relocation by MEP trades.",
        "6) Furnishing and installation of bathroom plumbing fixtures, toilets, urinals, mirrors and toilet partitions by Division 10 / Division 22.",
        "7) Single drinking fountain outside of new Unisex Restroom on 6th Floor excluded from ST-1 & SB-1 stone finishes (per scope clarification)."
    ]

    inclusions = [
        "1) Supply and Installation of all specified Stone, Ceramic, Cladding and Carpet materials.",
        "2) MINOR FLOOR PREP: Concrete slab scraping, surface prep, divot patching & flash-patching (up to 1/8\") across all tile & carpet areas.",
        "3) STONE WALL PANELS (ST-2) FULL HEIGHT: Extended full height to underside of beams at elevator lobbies (10'-0\" AFF).",
        "4) DRINKING FOUNTAIN ALCOVES: ST-1 stone floor (Porcelanosa 32x32) & SB-1 4\" stone base included at all typical corridor alcoves.",
        "5) 100% floor waterproofing membrane (Laticrete Hydro Ban) in all core restrooms.",
        "6) Mudset mortar bed installation for 32\"x32\" stone tile in restrooms & elevator lobbies.",
        "7) Schluter Quadec aluminum corner trims at all exposed outside wall tile corners.",
        "8) Black granite polished door thresholds / saddles at all restroom entrances.",
        "9) Schluter Schiene & Reno-U transition strips between dissimilar flooring materials.",
        "10) Tarkett 4\" millwork wallbase reveal around all carpeted corridors.",
        "11) Complete cleanup and daily debris removal to building dumpster."
    ]

    notes = [
        "Project: PENN 1 (One Penn Plaza, New York, NY) - 6th, 32nd & 33rd Floors Renovation.",
        "Architectural Drawings: Spin Design, Inc., Set IFB 8-18-26 ARCH (Sheets A-100, A-300, A-400, A-401, A-402).",
        "Clarification 1: Minor floor prep fully included across all rooms and floor areas.",
        "Clarification 2: Elevator lobby stone wall panels (ST-2 Florim 63x126) extended full height to underside of beams (10'-0\" AFF).",
        "Clarification 3: Typical drinking fountain alcoves receive ST-1 stone floor & SB-1 4\" stone base; 6th Fl Unisex RR exterior single fountain excluded.",
        "Waste allowance: +10% standard tile/carpet, +12% vanity accent tile included in gross quantities.",
        "Pricing based on standard NYC commercial prevailing trade union / established commercial subcontractor benchmark rates."
    ]

    return ProjectTakeoff(
        project_name="PENN 1 - Floors 6, 32 & 33 (Restrooms & Corridors)",
        client_name="Gaetan Toussaint / Spin Design, Inc.",
        client_company="Vornado Realty Trust",
        estimator_name="Osman",
        estimator_title="Senior Commercial Estimator",
        bidder_company="EasyTakeOffAI Commercial Estimating",
        bidder_address="One Penn Plaza, New York, NY",
        bidder_phone="(212) 629-6901",
        bidder_email="estimating@easytakeoffai.com",
        date_str=datetime.date.today().strftime("%m/%d/%Y"),
        trade_category="Tile, Stone & Flooring",
        rooms=rooms,
        material_specs=specs,
        exclusions=exclusions,
        inclusions=inclusions,
        notes=notes
    )
