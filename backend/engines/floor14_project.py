import datetime
from typing import Dict, List
from ..trades.trade_base import ProjectTakeoff, RoomTakeoff, TakeoffLineItem, MaterialSpec

def get_floor14_project() -> ProjectTakeoff:
    """
    Returns the complete, professional tile & stone takeoff for Floor 14:
    - LEVEL 14 - CORE RESTROOM (ADA)
    - LEVEL 14 - MEN'S RESTROOM
    - LEVEL 14 - WOMEN'S RESTROOM
    - LEVEL 14 - PANTRY / BREAK ROOM
    - LEVEL 14 - JANITOR CLOSET
    - LEVEL 14 - ELEVATOR LOBBY & VESTIBULE
    With complete trade specifications (CTF-1, CTW-1, MS, TB-1, SSF-1, SADDLE, WATERPROOF, MUD-SET, EPOXY-GROUT, TRIM-01, PREP-01).
    """
    specs: Dict[str, MaterialSpec] = {
        "CTF-1": MaterialSpec(
            symbol="CTF-1",
            description="Ceramic / Porcelain Floor Tile, 12\"x24\" Rectified, Matte Finish, Slip-Resistant DCOF > 0.42, Thinset / Mudset Installation",
            manufacturer="Daltile / American Olean",
            collection="Commercial Porcelain",
            size="12\"x24\"",
            finish="Matte",
            color="Neutral Grey / Off-White",
            unit="SQ FT",
            budget_price=11.50,
            notes="Floor 14 Restrooms, Pantries & Vestibules.",
            trade="Tile & Stone"
        ),
        "CTW-1": MaterialSpec(
            symbol="CTW-1",
            description="Ceramic Wall Tile, 4\"x12\" / 3\"x6\" Glazed Commercial Wall Tile, Stackbond or Running Bond to 8'-6\" AFF",
            manufacturer="Nemo / Daltile",
            collection="Architectural Glazed",
            size="4\"x12\"",
            finish="Gloss / Satin",
            color="Bright White / Ivory",
            unit="SQ FT",
            budget_price=9.50,
            notes="Floor 14 Restroom walls throughout to ceiling height.",
            trade="Tile & Stone"
        ),
        "MS": MaterialSpec(
            symbol="MS",
            description="Mosaic Accent Tile, 2\"x2\" Sheet-Mounted Porcelain / Glass Mosaic at wet walls and feature bands",
            manufacturer="Stone Source / Crossville",
            collection="Designer Mosaics",
            size="2\"x2\" Mosaic Sheet",
            finish="Textured",
            color="Accent Charcoal / Grey",
            unit="SQ FT",
            budget_price=14.50,
            notes="Pantry backsplash & Restroom feature zones.",
            trade="Tile & Stone"
        ),
        "TB-1": MaterialSpec(
            symbol="TB-1",
            description="Ceramic / Porcelain Tile Base, 4\" High Cove Base with Finished Top Edge",
            manufacturer="Matching Tile Mfr",
            collection="Trim & Base",
            size="4\" High",
            finish="Matte",
            color="To Match CTF-1",
            unit="LN FT",
            budget_price=4.50,
            notes="Perimeter base at all tiled spaces.",
            trade="Tile & Stone"
        ),
        "SSF-1": MaterialSpec(
            symbol="SSF-1",
            description="Solid Surface / Engineered Quartz Lavatory Countertop, 2cm Thick Slab with Polished Edges & Undermount Sink Cutouts",
            manufacturer="Cambria / Caesarstone",
            collection="Commercial Quartz",
            size="2cm Slab",
            finish="Polished",
            color="Neutral White / Grey",
            unit="SQ FT",
            budget_price=42.00,
            notes="Custom vanity tops at core restrooms.",
            trade="Tile & Stone"
        ),
        "SADDLE": MaterialSpec(
            symbol="SADDLE",
            description="White Carrara / Black Granite Threshold Saddle, 2\"x36\" to 4\"x36\" x 3/4\" Beveled Edges, Polished Finish",
            manufacturer="Custom Stone Fabricator",
            collection="Threshold Saddles",
            size="2\"x36\"",
            finish="Polished",
            color="Carrara / Granite",
            unit="PCS",
            budget_price=45.00,
            notes="Entry doorways transition saddles.",
            trade="Tile & Stone"
        ),
        "WATERPROOF": MaterialSpec(
            symbol="WATERPROOF",
            description="Liquid-Applied Waterproofing & Anti-Fracture Membrane (Laticrete Hydro Ban / Custom RedGard), Continuous Membrane",
            manufacturer="Laticrete",
            collection="Hydro Ban",
            size="Continuous",
            finish="Liquid Membrane",
            color="Olive Green",
            unit="SQ FT",
            budget_price=2.50,
            notes="100% floor slab waterproofing at all restrooms & pantries.",
            trade="Tile & Stone"
        ),
        "MUD-SET": MaterialSpec(
            symbol="MUD-SET",
            description="Portland Cement Mortar Bed (Mud-Set Prep & Leveling Bed, Wire-Mesh Reinforced, 1.25\" - 1.5\" Nominal)",
            manufacturer="SpecChem / Laticrete",
            collection="Thick Bed Mortar",
            size="1.5\" Bed",
            finish="Troweled",
            color="Grey",
            unit="SQ FT",
            budget_price=3.50,
            notes="Under tile flooring for pitch & positive drainage.",
            trade="Tile & Stone"
        ),
        "EPOXY-GROUT": MaterialSpec(
            symbol="EPOXY-GROUT",
            description="100% Solids Chemical & Stain Resistant Epoxy Grout (ANSI A118.3)",
            manufacturer="Laticrete / Mapei",
            collection="SpectraLOCK / Kerapoxy",
            size="Standard Joints",
            finish="Smooth",
            color="Matching Tile",
            unit="SQ FT",
            budget_price=2.00,
            notes="Heavy duty commercial grout for floors & wet walls.",
            trade="Tile & Stone"
        ),
        "TRIM-01": MaterialSpec(
            symbol="TRIM-01",
            description="Schluter-QUADEC / JOLLY Aluminum Metal Edge & Outside Corner Tile Profile",
            manufacturer="Schluter Systems",
            collection="Quadec-10",
            size="3/8\" x 8'-2.5\"",
            finish="Satin Anodized Aluminum",
            color="Aluminum",
            unit="LN FT",
            budget_price=4.50,
            notes="All exposed outside vertical wall tile corners & wainscot cap.",
            trade="Tile & Stone"
        ),
        "PREP-01": MaterialSpec(
            symbol="PREP-01",
            description="Minor Floor Prep: Mechanical scraping, substrate cleaning, divot patching & polymer flash-patching (up to 1/8\")",
            manufacturer="Ardex / Mapei",
            collection="Feather Finish",
            size="Substrate Level",
            finish="Smooth",
            color="Grey",
            unit="SQ FT",
            budget_price=0.95,
            notes="Concrete slab preparation prior to tile installation.",
            trade="Tile & Stone"
        )
    }

    rooms = [
        RoomTakeoff(
            room_name="LEVEL 14 - CORE RESTROOM (ADA)",
            floor_name="LEVEL 14",
            length_ft=11.0,
            width_ft=11.0,
            ceiling_height_ft=9.0,
            wall_tile_height_ft=8.5,
            door_count=1,
            items=[
                TakeoffLineItem("PREP-01", "FLOOR PREP", "SUBSTRATE PREPARATION", "S&I", 121.0, "SQ FT", 0.95, 1.25, "Minor Floor Prep & Substrate Leveling"),
                TakeoffLineItem("WATERPROOF", "FLOOR PREP", "WATERPROOFING", "S&I", 121.0, "SQ FT", 2.50, 2.50, "Liquid-Applied Waterproofing Membrane (Hydro Ban)"),
                TakeoffLineItem("MUD-SET", "FLOOR PREP", "MUDSET BED", "S&I", 121.0, "SQ FT", 3.50, 5.50, "Portland Cement Thick Bed Mortar"),
                TakeoffLineItem("CTF-1", "FLOOR", "PORCELAIN TILE", "S&I", 121.0, "SQ FT", 11.50, 13.50, "12\"x24\" Rectified Floor Tile"),
                TakeoffLineItem("EPOXY-GROUT", "FLOOR PREP", "EPOXY GROUT", "S&I", 121.0, "SQ FT", 2.00, 3.00, "Commercial Epoxy Grout"),
                TakeoffLineItem("CTW-1", "WALL", "CERAMIC TILE", "S&I", 240.0, "SQ FT", 9.50, 15.50, "4\"x12\" Wall Tile to 8'-6\" AFF"),
                TakeoffLineItem("TB-1", "BASE", "TILE BASE", "S&I", 44.0, "LN FT", 4.50, 5.50, "4\" Ceramic Cove Base"),
                TakeoffLineItem("SSF-1", "COUNTERTOP", "QUARTZ", "S&I", 12.0, "SQ FT", 42.00, 50.00, "Quartz Lavatory Vanity Countertop"),
                TakeoffLineItem("SADDLE", "THRESHOLD", "MARBLE SADDLE", "S&I", 1.0, "PCS", 45.00, 55.00, "Doorway Marble / Granite Saddle (2\"x36\")"),
                TakeoffLineItem("TRIM-01", "TRIM", "METAL TRIM", "S&I", 26.0, "LN FT", 4.50, 6.50, "Schluter Quadec Outside Corner Metal Trim")
            ]
        ),
        RoomTakeoff(
            room_name="LEVEL 14 - MEN'S RESTROOM",
            floor_name="LEVEL 14",
            length_ft=22.0,
            width_ft=14.0,
            ceiling_height_ft=9.0,
            wall_tile_height_ft=8.5,
            door_count=1,
            items=[
                TakeoffLineItem("PREP-01", "FLOOR PREP", "SUBSTRATE PREPARATION", "S&I", 308.0, "SQ FT", 0.95, 1.25, "Minor Floor Prep & Substrate Leveling"),
                TakeoffLineItem("WATERPROOF", "FLOOR PREP", "WATERPROOFING", "S&I", 308.0, "SQ FT", 2.50, 2.50, "Liquid-Applied Waterproofing Membrane"),
                TakeoffLineItem("MUD-SET", "FLOOR PREP", "MUDSET BED", "S&I", 308.0, "SQ FT", 3.50, 5.50, "Portland Cement Thick Bed Mortar"),
                TakeoffLineItem("CTF-1", "FLOOR", "PORCELAIN TILE", "S&I", 308.0, "SQ FT", 11.50, 13.50, "12\"x24\" Rectified Floor Tile"),
                TakeoffLineItem("EPOXY-GROUT", "FLOOR PREP", "EPOXY GROUT", "S&I", 308.0, "SQ FT", 2.00, 3.00, "Commercial Epoxy Grout"),
                TakeoffLineItem("CTW-1", "WALL", "CERAMIC TILE", "S&I", 480.0, "SQ FT", 9.50, 15.50, "4\"x12\" Wall Tile to 8'-6\" AFF"),
                TakeoffLineItem("MS", "WALL", "MOSAIC ACCENT TILE", "S&I", 45.0, "SQ FT", 14.50, 16.50, "Vanity Wet Wall Accent Band Mosaic"),
                TakeoffLineItem("TB-1", "BASE", "TILE BASE", "S&I", 62.0, "LN FT", 4.50, 5.50, "4\" Ceramic Cove Base"),
                TakeoffLineItem("SSF-1", "COUNTERTOP", "QUARTZ", "S&I", 18.0, "SQ FT", 42.00, 50.00, "Quartz Lavatory Vanity Countertop"),
                TakeoffLineItem("SADDLE", "THRESHOLD", "MARBLE SADDLE", "S&I", 1.0, "PCS", 45.00, 55.00, "Doorway Marble / Granite Saddle (2\"x36\")"),
                TakeoffLineItem("TRIM-01", "TRIM", "METAL TRIM", "S&I", 34.0, "LN FT", 4.50, 6.50, "Schluter Quadec Outside Corner Metal Trim")
            ]
        ),
        RoomTakeoff(
            room_name="LEVEL 14 - WOMEN'S RESTROOM",
            floor_name="LEVEL 14",
            length_ft=20.0,
            width_ft=14.0,
            ceiling_height_ft=9.0,
            wall_tile_height_ft=8.5,
            door_count=1,
            items=[
                TakeoffLineItem("PREP-01", "FLOOR PREP", "SUBSTRATE PREPARATION", "S&I", 280.0, "SQ FT", 0.95, 1.25, "Minor Floor Prep & Substrate Leveling"),
                TakeoffLineItem("WATERPROOF", "FLOOR PREP", "WATERPROOFING", "S&I", 280.0, "SQ FT", 2.50, 2.50, "Liquid-Applied Waterproofing Membrane"),
                TakeoffLineItem("MUD-SET", "FLOOR PREP", "MUDSET BED", "S&I", 280.0, "SQ FT", 3.50, 5.50, "Portland Cement Thick Bed Mortar"),
                TakeoffLineItem("CTF-1", "FLOOR", "PORCELAIN TILE", "S&I", 280.0, "SQ FT", 11.50, 13.50, "12\"x24\" Rectified Floor Tile"),
                TakeoffLineItem("EPOXY-GROUT", "FLOOR PREP", "EPOXY GROUT", "S&I", 280.0, "SQ FT", 2.00, 3.00, "Commercial Epoxy Grout"),
                TakeoffLineItem("CTW-1", "WALL", "CERAMIC TILE", "S&I", 460.0, "SQ FT", 9.50, 15.50, "4\"x12\" Wall Tile to 8'-6\" AFF"),
                TakeoffLineItem("MS", "WALL", "MOSAIC ACCENT TILE", "S&I", 45.0, "SQ FT", 14.50, 16.50, "Vanity Wet Wall Accent Band Mosaic"),
                TakeoffLineItem("TB-1", "BASE", "TILE BASE", "S&I", 58.0, "LN FT", 4.50, 5.50, "4\" Ceramic Cove Base"),
                TakeoffLineItem("SSF-1", "COUNTERTOP", "QUARTZ", "S&I", 18.0, "SQ FT", 42.00, 50.00, "Quartz Lavatory Vanity Countertop"),
                TakeoffLineItem("SADDLE", "THRESHOLD", "MARBLE SADDLE", "S&I", 1.0, "PCS", 45.00, 55.00, "Doorway Marble / Granite Saddle (2\"x36\")"),
                TakeoffLineItem("TRIM-01", "TRIM", "METAL TRIM", "S&I", 34.0, "LN FT", 4.50, 6.50, "Schluter Quadec Outside Corner Metal Trim")
            ]
        ),
        RoomTakeoff(
            room_name="LEVEL 14 - PANTRY / BREAK ROOM",
            floor_name="LEVEL 14",
            length_ft=12.0,
            width_ft=10.0,
            ceiling_height_ft=9.0,
            wall_tile_height_ft=0.0,
            door_count=1,
            items=[
                TakeoffLineItem("PREP-01", "FLOOR PREP", "SUBSTRATE PREPARATION", "S&I", 120.0, "SQ FT", 0.95, 1.25, "Minor Floor Prep & Substrate Leveling"),
                TakeoffLineItem("WATERPROOF", "FLOOR PREP", "WATERPROOFING", "S&I", 120.0, "SQ FT", 2.50, 2.50, "Liquid-Applied Waterproofing Membrane"),
                TakeoffLineItem("CTF-1", "FLOOR", "PORCELAIN TILE", "S&I", 120.0, "SQ FT", 11.50, 13.50, "12\"x24\" Rectified Floor Tile"),
                TakeoffLineItem("EPOXY-GROUT", "FLOOR PREP", "EPOXY GROUT", "S&I", 120.0, "SQ FT", 2.00, 3.00, "Commercial Epoxy Grout"),
                TakeoffLineItem("CTW-1", "WALL", "CERAMIC TILE", "S&I", 40.0, "SQ FT", 9.50, 15.50, "Kitchenette Countertop Backsplash Full Height"),
                TakeoffLineItem("TB-1", "BASE", "TILE BASE", "S&I", 38.0, "LN FT", 4.50, 5.50, "4\" Ceramic Cove Base"),
                TakeoffLineItem("SSF-1", "COUNTERTOP", "QUARTZ", "S&I", 24.0, "SQ FT", 42.00, 50.00, "Kitchenette Quartz Countertop with Sink Cutout"),
                TakeoffLineItem("SADDLE", "THRESHOLD", "MARBLE SADDLE", "S&I", 1.0, "PCS", 45.00, 55.00, "Doorway Marble / Granite Saddle (2\"x36\")")
            ]
        ),
        RoomTakeoff(
            room_name="LEVEL 14 - JANITOR CLOSET",
            floor_name="LEVEL 14",
            length_ft=6.0,
            width_ft=6.0,
            ceiling_height_ft=9.0,
            wall_tile_height_ft=4.0,
            door_count=1,
            items=[
                TakeoffLineItem("PREP-01", "FLOOR PREP", "SUBSTRATE PREPARATION", "S&I", 36.0, "SQ FT", 0.95, 1.25, "Minor Floor Prep & Substrate Leveling"),
                TakeoffLineItem("WATERPROOF", "FLOOR PREP", "WATERPROOFING", "S&I", 36.0, "SQ FT", 2.50, 2.50, "Liquid-Applied Waterproofing Membrane"),
                TakeoffLineItem("CTF-1", "FLOOR", "PORCELAIN TILE", "S&I", 36.0, "SQ FT", 11.50, 13.50, "12\"x24\" Rectified Floor Tile"),
                TakeoffLineItem("CTW-1", "WALL", "CERAMIC TILE", "S&I", 48.0, "SQ FT", 9.50, 15.50, "Mop Basin Surround Wall Tile to 4'-0\" AFF"),
                TakeoffLineItem("TB-1", "BASE", "TILE BASE", "S&I", 20.0, "LN FT", 4.50, 5.50, "4\" Ceramic Cove Base"),
                TakeoffLineItem("SADDLE", "THRESHOLD", "MARBLE SADDLE", "S&I", 1.0, "PCS", 45.00, 55.00, "Doorway Marble / Granite Saddle (2\"x36\")")
            ]
        ),
        RoomTakeoff(
            room_name="LEVEL 14 - ELEVATOR LOBBY & VESTIBULE",
            floor_name="LEVEL 14",
            length_ft=28.0,
            width_ft=12.0,
            ceiling_height_ft=9.5,
            wall_tile_height_ft=0.0,
            door_count=2,
            items=[
                TakeoffLineItem("PREP-01", "FLOOR PREP", "SUBSTRATE PREPARATION", "S&I", 336.0, "SQ FT", 0.95, 1.25, "Minor Floor Prep & Scarifying under Mudset"),
                TakeoffLineItem("MUD-SET", "FLOOR PREP", "MUDSET BED", "S&I", 336.0, "SQ FT", 3.50, 5.50, "Portland Cement Thick Bed Mortar Bed"),
                TakeoffLineItem("CTF-1", "FLOOR", "PORCELAIN TILE", "S&I", 336.0, "SQ FT", 11.50, 13.50, "12\"x24\" / 24\"x24\" Porcelain Floor Tile"),
                TakeoffLineItem("EPOXY-GROUT", "FLOOR PREP", "EPOXY GROUT", "S&I", 336.0, "SQ FT", 2.00, 3.00, "Commercial Epoxy Grout"),
                TakeoffLineItem("TB-1", "BASE", "TILE BASE", "S&I", 80.0, "LN FT", 4.50, 5.50, "4\" Matching Porcelain Tile Base"),
                TakeoffLineItem("SADDLE", "THRESHOLD", "MARBLE SADDLE", "S&I", 2.0, "PCS", 45.00, 55.00, "Elevator Lobby Corridor Entrance Saddles (3'-0\" x 4\")")
            ]
        )
    ]

    exclusions = [
        "1) Demolition of existing partitions, fixtures and flooring (by Demolition Trade).",
        "2) Concrete slab structural alterations, floor infills or floor trenches.",
        "3) Moisture mitigation / epoxy vapor barrier unless specified.",
        "4) Premium / Overtime labor unless agreed in writing.",
        "5) Bathroom plumbing fixtures, faucets, flush valves and toilet accessories (by Division 22 & 10)."
    ]

    inclusions = [
        "1) Supply & Install of all specified Floor Tiles, Wall Tiles, Mosaics and Bases on Floor 14.",
        "2) 100% floor waterproofing membrane (Laticrete Hydro Ban) in all Restrooms & Pantry.",
        "3) Wire-mesh reinforced thick-bed mortar (Mudset) in Restrooms & Elevator Lobby.",
        "4) 100% solids chemical-resistant epoxy grout at tiled floors.",
        "5) Solid surface / Quartz countertops at Restroom vanities & Kitchenette.",
        "6) Schluter Quadec aluminum corner trims at all exposed outside wall tile corners.",
        "7) Marble / Granite door threshold saddles at all room entrances.",
        "8) Minor floor preparation: substrate scraping, cleaning, divot patching and flash-patching."
    ]

    notes = [
        "Project: Bidding Documents 09 22 26 - Floor 14 Dedicated Takeoff.",
        "Scope: Strictly Floor 14 (Level 14 Core ADA Restroom, Men's RR, Women's RR, Pantry, Janitor, Elevator Lobby).",
        "Waste Allowance: +10% standard tile, +12% mosaics included in gross quantities.",
        "Pricing: Prevailing commercial subcontractor labor & commercial grade materials."
    ]

    return ProjectTakeoff(
        project_name="Bidding Documents 09 22 26 - Floor 14 Takeoff",
        client_name="Commercial Client Directorate",
        client_company="General Contractor / Master Builder",
        estimator_name="Osman",
        estimator_title="Senior Commercial Estimator",
        bidder_company="EasyTakeOffAI Commercial Estimating",
        bidder_address="New York, NY",
        bidder_phone="(212) 555-0199",
        bidder_email="estimating@easytakeoffai.com",
        date_str=datetime.date.today().strftime("%m/%d/%Y"),
        trade_category="Tile & Stone",
        rooms=rooms,
        material_specs=specs,
        exclusions=exclusions,
        inclusions=inclusions,
        notes=notes
    )
