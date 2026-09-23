import datetime
from typing import Dict, List
from ..trades.trade_base import ProjectTakeoff, RoomTakeoff, TakeoffLineItem, MaterialSpec

def get_broadway225_project() -> ProjectTakeoff:
    """
    Official Takeoff for:
    DDF: Downtown Dance Factory - 225 Broadway, 14th Floor, New York, NY 10007
    Owner: William Macklowe Company
    Architect: Daniel Goldner Architects (152 West 25th St, NY)
    Interior Design: Pink Green Interiors - Katie Hartell (917-912-2504)
    Drawing Set: 90% CD & Bid Set Rev. 1 (09/03/2026)
    
    Tile & Stone Scope:
    1) Girl's Bathroom (16'-0" x 18'-2"): Black & White Strip Tile, Wall Tile to 84" AFF, Quartz Vanity Top
    2) Boy's Bathroom (11'-9" x 8'-6"): Black & White Triangle Tile, Wall Tile to 84" AFF, Urinal & Sink Walls
    3) ADA Bathroom (12'-0" x 7'-10"): Black & White Diamond Tile, Wall Tile to 84" AFF, ADA Vanity Top
    4) Janitor's Closet (11'-3" x 5'-6"): Black & White Diamond Tile, Mop Sink Surround Wall Tile
    5) Broom Closet (3'-1" x 2'-9"): Black & White Diamond Tile
    Note: Dark gray shaded areas on architectural plans (Building common corridors, elevator vestibules, existing terrazzo) are strictly EXCLUDED (Existing to Remain / NIC / By Others).
    """
    specs: Dict[str, MaterialSpec] = {
        "FT-STRIP": MaterialSpec(
            symbol="FT-STRIP",
            description="Black and White Strip Porcelain Floor Tile, Matte Finish, Slip Resistant DCOF > 0.42, Thinset/Mudset Installation",
            manufacturer="Pink Green Interiors Spec / Custom Ceramic",
            collection="Graphic Black & White",
            size="Custom Pattern Strip",
            finish="Matte",
            color="Black & White",
            unit="SQ FT",
            budget_price=13.50,
            notes="Girl's Bathroom Floor (+1/2\" finish).",
            trade="Tile & Stone"
        ),
        "FT-TRIANGLE": MaterialSpec(
            symbol="FT-TRIANGLE",
            description="Black and White Triangle Geometric Porcelain Floor Tile, Matte Finish",
            manufacturer="Pink Green Interiors Spec / Custom Ceramic",
            collection="Geometric Collection",
            size="Triangle Mosaic / Modular",
            finish="Matte",
            color="Black & White",
            unit="SQ FT",
            budget_price=14.00,
            notes="Boy's Bathroom Floor (+1/2\" finish).",
            trade="Tile & Stone"
        ),
        "FT-DIAMOND": MaterialSpec(
            symbol="FT-DIAMOND",
            description="Black and White Diamond Porcelain Floor Tile, Matte Finish",
            manufacturer="Pink Green Interiors Spec / Custom Ceramic",
            collection="Harlequin Diamond",
            size="Diamond Pattern",
            finish="Matte",
            color="Black & White",
            unit="SQ FT",
            budget_price=13.00,
            notes="ADA Bathroom, Janitor's Closet & Broom Closet floors.",
            trade="Tile & Stone"
        ),
        "WT-01": MaterialSpec(
            symbol="WT-01",
            description="Glazed Ceramic Wall Tile, 84\" (7'-0\" AFF) Full Height Wainscot & Wet Wall Tile",
            manufacturer="Daltile / American Olean",
            collection="Commercial Glazed Wall",
            size="3\"x6\" / 4\"x12\"",
            finish="Gloss / Satin",
            color="Crisp White / Accent Black Band",
            unit="SQ FT",
            budget_price=9.50,
            notes="Full 84\" AFF wall tile at Girl's, Boy's and ADA Restrooms.",
            trade="Tile & Stone"
        ),
        "WT-ACCENT": MaterialSpec(
            symbol="WT-ACCENT",
            description="Ceramic Sink Accent Wall Tile, Full 84\" Height Feature Wall (E24 Sink Wall & E33 Boy's Sink Wall)",
            manufacturer="Custom Ceramic / Designer Spec",
            collection="Accent Feature Series",
            size="Accent Module",
            finish="Satin",
            color="Feature Contrast Pattern",
            unit="SQ FT",
            budget_price=12.50,
            notes="Behind vanity sinks to 84\" AFF.",
            trade="Tile & Stone"
        ),
        "TB-1": MaterialSpec(
            symbol="TB-1",
            description="4\" Ceramic / Porcelain Cove Base with Finished Rounded Top Edge",
            manufacturer="Matching Tile Mfr",
            collection="Cove Base",
            size="4\" High",
            finish="Matte",
            color="To Match Floor Pattern",
            unit="LN FT",
            budget_price=5.00,
            notes="Perimeter base at all tiled restrooms & closets.",
            trade="Tile & Stone"
        ),
        "SSF-1": MaterialSpec(
            symbol="SSF-1",
            description="Engineered Quartz / Solid Surface Custom Vanity Countertop (34\" AFF, Multi-Sink Cutouts & Finished Edges)",
            manufacturer="Caesarstone / Corian",
            collection="Commercial Tops",
            size="2cm Thick Slab",
            finish="Polished",
            color="Solid White / Neutral",
            unit="SQ FT",
            budget_price=45.00,
            notes="Custom countertops: 116-5/8\" in Girl's WC, 75\" in Boy's WC, 56\" in ADA WC.",
            trade="Tile & Stone"
        ),
        "SADDLE": MaterialSpec(
            symbol="SADDLE",
            description="White Carrara / Black Granite Doorway Transition Saddle, 2\"x36\" to 4\"x42\" x 3/4\" Beveled Edges",
            manufacturer="Custom Stone Fabricator",
            collection="Door Saddles",
            size="Beveled Saddle",
            finish="Honed / Polished",
            color="Carrara / Absolute Black",
            unit="PCS",
            budget_price=50.00,
            notes="Entrance threshold transitions at all restroom and closet doors.",
            trade="Tile & Stone"
        ),
        "TERRAZZO": MaterialSpec(
            symbol="TERRAZZO",
            description="Epoxy / Cementitious Terrazzo Floor Finish & Base (+1/2\" finish)",
            manufacturer="Fritztile / Terrazzo USA",
            collection="Classic Architectural Terrazzo",
            size="Seamless / Tile",
            finish="Polished Satin",
            color="Architectural Gray Blend",
            unit="SQ FT",
            budget_price=18.00,
            notes="Hallway & Elevator Lobby Floor (10'-0\" x 49'-8\").",
            trade="Tile & Stone"
        ),
        "WATERPROOF": MaterialSpec(
            symbol="WATERPROOF",
            description="Liquid-Applied Waterproofing Membrane (Laticrete Hydro Ban / RedGard ANSI A118.10), 100% Floor Slab Coverage",
            manufacturer="Laticrete",
            collection="Hydro Ban",
            size="Continuous Membrane",
            finish="Liquid Membrane",
            color="Green",
            unit="SQ FT",
            budget_price=2.50,
            notes="Full floor slab waterproofing under all wet restrooms & mop closets.",
            trade="Tile & Stone"
        ),
        "MUD-SET": MaterialSpec(
            symbol="MUD-SET",
            description="Portland Cement Mortar Bed (Mud-Set Wire-Mesh Reinforced Leveling & Pitch Bed, 1.25\" - 3.5\" Variable)",
            manufacturer="SpecChem / Laticrete",
            collection="Thick Bed Mortar",
            size="Variable Bed (+1/2\" to +3.5\")",
            finish="Troweled",
            color="Grey",
            unit="SQ FT",
            budget_price=3.75,
            notes="Mudset mortar leveling bed for ADA (+3.5\") and standard (+1/2\") floor elevations.",
            trade="Tile & Stone"
        ),
        "EPOXY-GROUT": MaterialSpec(
            symbol="EPOXY-GROUT",
            description="100% Solids Stain & Chemical Resistant Commercial Epoxy Grout (ANSI A118.3)",
            manufacturer="Laticrete SpectraLOCK / Mapei Kerapoxy",
            collection="Commercial Epoxy",
            size="Standard Joints",
            finish="Smooth",
            color="To Match Tile",
            unit="SQ FT",
            budget_price=2.25,
            notes="All wet floor tile and wainscot tile joints.",
            trade="Tile & Stone"
        ),
        "TRIM-01": MaterialSpec(
            symbol="TRIM-01",
            description="Schluter-QUADEC / JOLLY Aluminum Metal Edge & Wainscot Cap Profile (84\" AFF Cap)",
            manufacturer="Schluter Systems",
            collection="Quadec Satin Aluminum",
            size="3/8\" x 8'-2.5\"",
            finish="Satin Anodized Aluminum",
            color="Black / Aluminum",
            unit="LN FT",
            budget_price=4.50,
            notes="All exposed outside vertical wall corners and 84\" AFF wainscot top cap.",
            trade="Tile & Stone"
        ),
        "PREP-01": MaterialSpec(
            symbol="PREP-01",
            description="Minor Floor Prep: Mechanical scraping, concrete substrate cleaning, divot patching and flash-patching (up to 1/8\")",
            manufacturer="Ardex / Mapei",
            collection="Feather Finish",
            size="Substrate Level",
            finish="Smooth",
            color="Grey",
            unit="SQ FT",
            budget_price=0.95,
            notes="Concrete slab preparation prior to tile & mudset installation.",
            trade="Tile & Stone"
        )
    }

    rooms = [
        RoomTakeoff(
            room_name="14TH FL - GIRL'S BATHROOM",
            floor_name="LEVEL 14",
            length_ft=18.17,
            width_ft=16.0,
            ceiling_height_ft=10.33,
            wall_tile_height_ft=7.0,
            door_count=1,
            items=[
                TakeoffLineItem("PREP-01", "FLOOR PREP", "SUBSTRATE PREPARATION", "S&I", 290.7, "SQ FT", 0.95, 1.25, "Minor Floor Prep & Substrate Leveling"),
                TakeoffLineItem("WATERPROOF", "FLOOR PREP", "WATERPROOFING", "S&I", 290.7, "SQ FT", 2.50, 2.50, "Liquid-Applied Hydro Ban Membrane"),
                TakeoffLineItem("MUD-SET", "FLOOR PREP", "MUDSET BED", "S&I", 290.7, "SQ FT", 3.75, 5.50, "Portland Cement Thick Bed Mortar (+1/2\" finish)"),
                TakeoffLineItem("FT-STRIP", "FLOOR", "PORCELAIN TILE", "S&I", 290.7, "SQ FT", 13.50, 14.50, "Black & White Strip Porcelain Floor Tile"),
                TakeoffLineItem("EPOXY-GROUT", "FLOOR PREP", "EPOXY GROUT", "S&I", 290.7, "SQ FT", 2.25, 3.00, "Commercial Epoxy Grout Floor & Walls"),
                TakeoffLineItem("WT-01", "WALL", "CERAMIC TILE", "S&I", 380.0, "SQ FT", 9.50, 15.50, "Glazed Ceramic Wall Tile to 84\" (7'-0\" AFF)"),
                TakeoffLineItem("WT-ACCENT", "WALL", "CERAMIC ACCENT TILE", "S&I", 77.0, "SQ FT", 12.50, 16.50, "E24 Sink Accent Wall Tile to 84\" AFF"),
                TakeoffLineItem("TB-1", "BASE", "TILE BASE", "S&I", 65.0, "LN FT", 5.00, 5.50, "4\" Cove Ceramic Tile Base"),
                TakeoffLineItem("SSF-1", "COUNTERTOP", "QUARTZ", "S&I", 19.5, "SQ FT", 45.00, 50.00, "116-5/8\" Quartz Vanity Countertop with Sink Cutouts"),
                TakeoffLineItem("SADDLE", "THRESHOLD", "MARBLE SADDLE", "S&I", 1.0, "PCS", 50.00, 55.00, "Doorway Marble / Granite Transition Saddle"),
                TakeoffLineItem("TRIM-01", "TRIM", "METAL TRIM", "S&I", 35.0, "LN FT", 4.50, 6.50, "Schluter Wainscot Cap & Corner Profiles")
            ]
        ),
        RoomTakeoff(
            room_name="14TH FL - BOY'S BATHROOM",
            floor_name="LEVEL 14",
            length_ft=11.75,
            width_ft=8.5,
            ceiling_height_ft=10.33,
            wall_tile_height_ft=7.0,
            door_count=1,
            items=[
                TakeoffLineItem("PREP-01", "FLOOR PREP", "SUBSTRATE PREPARATION", "S&I", 99.9, "SQ FT", 0.95, 1.25, "Minor Floor Prep & Substrate Leveling"),
                TakeoffLineItem("WATERPROOF", "FLOOR PREP", "WATERPROOFING", "S&I", 99.9, "SQ FT", 2.50, 2.50, "Liquid-Applied Hydro Ban Membrane"),
                TakeoffLineItem("MUD-SET", "FLOOR PREP", "MUDSET BED", "S&I", 99.9, "SQ FT", 3.75, 5.50, "Portland Cement Thick Bed Mortar (+1/2\" finish)"),
                TakeoffLineItem("FT-TRIANGLE", "FLOOR", "PORCELAIN TILE", "S&I", 99.9, "SQ FT", 14.00, 15.00, "Black & White Triangle Geometric Floor Tile"),
                TakeoffLineItem("EPOXY-GROUT", "FLOOR PREP", "EPOXY GROUT", "S&I", 99.9, "SQ FT", 2.25, 3.00, "Commercial Epoxy Grout Floor & Walls"),
                TakeoffLineItem("WT-01", "WALL", "CERAMIC TILE", "S&I", 215.0, "SQ FT", 9.50, 15.50, "Glazed Ceramic Wall Tile to 84\" AFF"),
                TakeoffLineItem("WT-ACCENT", "WALL", "CERAMIC ACCENT TILE", "S&I", 51.0, "SQ FT", 12.50, 16.50, "E33 Sink & E35 Urinal Accent Wall Tile"),
                TakeoffLineItem("TB-1", "BASE", "TILE BASE", "S&I", 38.0, "LN FT", 5.00, 5.50, "4\" Cove Ceramic Tile Base"),
                TakeoffLineItem("SSF-1", "COUNTERTOP", "QUARTZ", "S&I", 12.5, "SQ FT", 45.00, 50.00, "75\" Quartz Vanity Countertop with Sink Cutouts"),
                TakeoffLineItem("SADDLE", "THRESHOLD", "MARBLE SADDLE", "S&I", 1.0, "PCS", 50.00, 55.00, "Doorway Marble / Granite Transition Saddle"),
                TakeoffLineItem("TRIM-01", "TRIM", "METAL TRIM", "S&I", 28.0, "LN FT", 4.50, 6.50, "Schluter Wainscot Cap & Corner Profiles")
            ]
        ),
        RoomTakeoff(
            room_name="14TH FL - ADA BATHROOM",
            floor_name="LEVEL 14",
            length_ft=12.0,
            width_ft=7.83,
            ceiling_height_ft=10.04,
            wall_tile_height_ft=7.0,
            door_count=1,
            items=[
                TakeoffLineItem("PREP-01", "FLOOR PREP", "SUBSTRATE PREPARATION", "S&I", 94.0, "SQ FT", 0.95, 1.25, "Minor Floor Prep & Substrate Leveling"),
                TakeoffLineItem("WATERPROOF", "FLOOR PREP", "WATERPROOFING", "S&I", 94.0, "SQ FT", 2.50, 2.50, "Liquid-Applied Hydro Ban Membrane"),
                TakeoffLineItem("MUD-SET", "FLOOR PREP", "MUDSET BED", "S&I", 94.0, "SQ FT", 4.50, 6.50, "Thick Bed Mudset for +3.5\" Raised Floor Transition"),
                TakeoffLineItem("FT-DIAMOND", "FLOOR", "PORCELAIN TILE", "S&I", 94.0, "SQ FT", 13.00, 14.50, "Black & White Diamond Porcelain Floor Tile"),
                TakeoffLineItem("EPOXY-GROUT", "FLOOR PREP", "EPOXY GROUT", "S&I", 94.0, "SQ FT", 2.25, 3.00, "Commercial Epoxy Grout Floor & Walls"),
                TakeoffLineItem("WT-01", "WALL", "CERAMIC TILE", "S&I", 253.0, "SQ FT", 9.50, 15.50, "Glazed Ceramic Wall Tile to 84\" (7'-0\" AFF)"),
                TakeoffLineItem("TB-1", "BASE", "TILE BASE", "S&I", 36.0, "LN FT", 5.00, 5.50, "4\" Cove Ceramic Tile Base"),
                TakeoffLineItem("SSF-1", "COUNTERTOP", "QUARTZ", "S&I", 9.3, "SQ FT", 45.00, 50.00, "56\" ADA Quartz Lavatory Countertop with Sink Cutout"),
                TakeoffLineItem("SADDLE", "THRESHOLD", "MARBLE SADDLE", "S&I", 1.0, "PCS", 50.00, 55.00, "42\" Beveled Marble / Granite Doorway Saddle"),
                TakeoffLineItem("TRIM-01", "TRIM", "METAL TRIM", "S&I", 28.0, "LN FT", 4.50, 6.50, "Schluter Wainscot Cap & Corner Profiles")
            ]
        ),
        RoomTakeoff(
            room_name="14TH FL - JANITOR'S CLOSET",
            floor_name="LEVEL 14",
            length_ft=11.25,
            width_ft=5.5,
            ceiling_height_ft=9.5,
            wall_tile_height_ft=4.0,
            door_count=1,
            items=[
                TakeoffLineItem("PREP-01", "FLOOR PREP", "SUBSTRATE PREPARATION", "S&I", 61.9, "SQ FT", 0.95, 1.25, "Minor Floor Prep & Substrate Leveling"),
                TakeoffLineItem("WATERPROOF", "FLOOR PREP", "WATERPROOFING", "S&I", 61.9, "SQ FT", 2.50, 2.50, "Liquid-Applied Hydro Ban Membrane"),
                TakeoffLineItem("MUD-SET", "FLOOR PREP", "MUDSET BED", "S&I", 61.9, "SQ FT", 3.75, 5.50, "Portland Cement Thick Bed Mortar"),
                TakeoffLineItem("FT-DIAMOND", "FLOOR", "PORCELAIN TILE", "S&I", 61.9, "SQ FT", 13.00, 14.50, "Black & White Diamond Porcelain Floor Tile"),
                TakeoffLineItem("WT-01", "WALL", "CERAMIC TILE", "S&I", 48.0, "SQ FT", 9.50, 15.50, "Mop Service Basin Ceramic Tile Surround to 48\" AFF"),
                TakeoffLineItem("TB-1", "BASE", "TILE BASE", "S&I", 31.0, "LN FT", 5.00, 5.50, "4\" Cove Ceramic Tile Base"),
                TakeoffLineItem("SADDLE", "THRESHOLD", "MARBLE SADDLE", "S&I", 1.0, "PCS", 50.00, 55.00, "Doorway Marble / Granite Transition Saddle")
            ]
        ),
        RoomTakeoff(
            room_name="14TH FL - BROOM CLOSET",
            floor_name="LEVEL 14",
            length_ft=3.08,
            width_ft=2.75,
            ceiling_height_ft=9.5,
            wall_tile_height_ft=0.0,
            door_count=1,
            items=[
                TakeoffLineItem("PREP-01", "FLOOR PREP", "SUBSTRATE PREPARATION", "S&I", 8.5, "SQ FT", 0.95, 1.25, "Minor Floor Prep & Substrate Leveling"),
                TakeoffLineItem("WATERPROOF", "FLOOR PREP", "WATERPROOFING", "S&I", 8.5, "SQ FT", 2.50, 2.50, "Liquid-Applied Hydro Ban Membrane"),
                TakeoffLineItem("MUD-SET", "FLOOR PREP", "MUDSET BED", "S&I", 8.5, "SQ FT", 4.50, 6.50, "Thick Bed Mudset for +3.5\" Raised Floor"),
                TakeoffLineItem("FT-DIAMOND", "FLOOR", "PORCELAIN TILE", "S&I", 8.5, "SQ FT", 13.00, 14.50, "Black & White Diamond Porcelain Floor Tile"),
                TakeoffLineItem("TB-1", "BASE", "TILE BASE", "S&I", 9.0, "LN FT", 5.00, 5.50, "4\" Cove Ceramic Tile Base"),
                TakeoffLineItem("SADDLE", "THRESHOLD", "MARBLE SADDLE", "S&I", 1.0, "PCS", 50.00, 55.00, "Doorway Marble / Granite Transition Saddle")
            ]
        )
    ]

    exclusions = [
        "1) Dance studio specialized flooring (Marley dance floors, sprung wood dance floors by Division 096400).",
        "2) Concrete slab structural trenching, slab infill or core drilling beyond minor floor prep.",
        "3) Dance studio wall mirrors, barre brackets, and collapsible partitions (by Specialties Division 10).",
        "4) Bathroom plumbing fixtures, faucets, grab bars, flush valves and soap dispensers (by MEP / Division 22).",
        "5) Premium / Overtime labor unless authorized in writing.",
        "6) Moisture mitigation / epoxy vapor barrier unless specified.",
        "7) Dark gray shaded areas on architectural drawings (Building common corridors, elevator vestibules, existing terrazzo flooring, elevator shafts, stairs and electrical closets) are strictly EXCLUDED per client / GC scope rules (Existing to Remain / NIC / By Others)."
    ]

    inclusions = [
        "1) Supply & Install of all specified Floor Tiles (Strip, Triangle & Diamond patterns) on 14th Floor.",
        "2) Supply & Install of full 84\" (7'-0\" AFF) ceramic wall tile and sink accent feature walls.",
        "3) 100% floor slab liquid-applied waterproofing membrane (Laticrete Hydro Ban) in all restrooms & closets.",
        "4) Wire-mesh reinforced thick-bed mortar (Mudset) for +1/2\" and +3.5\" raised floor transitions.",
        "5) Commercial 100% solids stain-resistant epoxy grout at all tiled floors & wet walls.",
        "6) Custom engineered quartz vanity countertops (Girl's 116-5/8\", Boy's 75\", ADA 56\") with undermount sink cutouts.",
        "7) Polished marble / granite threshold saddles at all doorway transitions.",
        "8) Schluter aluminum trims at all exposed outside wall tile corners and 84\" AFF wainscot top caps.",
        "9) Minor floor prep: mechanical scraping, substrate cleaning, divot patching and polymer flash-patching."
    ]

    notes = [
        "Project: DDF: Downtown Dance Factory - 225 Broadway, 14th Floor, New York, NY 10007.",
        "Drawing Reference: 90% CD & Bid Set Rev. 1 (Architect: Daniel Goldner Architects / Interior Design: Pink Green Interiors).",
        "Key Sheets: ID-1 (Studio Floor Plan), ID-9 (Girl's WC), ID-10 (ADA WC), ID-11 (Boy's WC & Broom), ID-12 (Janitor's Closet), A-002/A-003 (Specs).",
        "Wall Tile Heights: 84\" (7'-0\" AFF) in Girl's Bathroom, Boy's Bathroom and ADA Bathroom.",
        "Floor Transitions: Mudset leveling provided for +1/2\" and +3.5\" floor height differential.",
        "Waste Allowance: +10% standard tile & terrazzo, +12% geometric pattern tiles included in net quantities."
    ]

    return ProjectTakeoff(
        project_name="[BID] DDF: Downtown Dance Factory - 225 Broadway, 14th Floor",
        client_name="Katie Hartell (Pink Green Interiors)",
        client_company="DDFNYC / William Macklowe Company",
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
