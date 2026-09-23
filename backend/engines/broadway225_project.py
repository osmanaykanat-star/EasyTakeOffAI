import datetime
from typing import Dict, List
from ..trades.trade_base import ProjectTakeoff, RoomTakeoff, TakeoffLineItem, MaterialSpec

def get_broadway225_project() -> ProjectTakeoff:
    """
    Official Commercial Tile & Stone Proposal:
    Project: DDF: Downtown Dance Factory - 225 Broadway, 14th Floor, New York, NY 10007
    Owner: William Macklowe Company (126 East 56th St, NY)
    Architect: Daniel Goldner Architects (152 West 25th St, NY)
    Interior Design: Pink Green Interiors - Katie Hartell (917-912-2504)
    Drawing Set: 90% CD & Bid Set Rev. 1 (09/03/2026)
    
    Tile & Stone Base Bid Scope (Clear Unshaded Areas):
    1) Room 1424 - GIRL'S WC (16'-0" x 18'-2"): Black & White Strip Porcelain Tile, 84" Ceramic Wall Tile, E24 Accent Wall, 116-5/8" Solid Surface Top w/ 4 Undermount Sinks.
    2) Room 1422 - BOY'S WC (11'-9" x 8'-6"): Black & White Triangle Geometric Tile, 84" Ceramic Wall Tile, E33 Sink & E35 Urinal Accent Walls (Wall-hung sink per E33).
    3) Room 1425 - JANITOR'S CLOSET (11'-3" x 5'-6"): Black & White Diamond Tile, 48" Ceramic Wall Tile Surround at Mop Basin.

    Excluded from Base Bid per Drawing Scope Rules:
    - Dark Gray Shaded Areas (Corridors 1400/1401/1413/1429/1431, Elevator Shafts, Stair B, and Room 1417 ADA WC) are strictly EXCLUDED (Existing to Remain / NIC / By Others).
    - Elevator Lobby (Rooms 1430 & 1412, ~496.7 SF): Existing Terrazzo per Sheet A-011.00 ('WHERE EXISTING TERRAZZO TILE ENDS') & Painted Walls (Available as Add-Alternate: +$21,279.84).
    - ADA WC (Room 1417) & Broom Closet: Shaded dark gray on A-100 / A-011 core zone (Available as Add-Alternate: +$12,788.80 & +$587.95).
    - Countertop Apron: 5" Fixed P-Lam Apron is by Millwork contractor per Detail 01/A-500. Horizontal Solid Surface slab top & 4" backsplash included per Detail 10/A-500.
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
            notes="Girl's Bathroom Floor (Room 1424) (+1/2\" finish).",
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
            notes="Boy's Bathroom Floor (Room 1422) (+1/2\" finish).",
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
            notes="Janitor's Closet Floor (Room 1425).",
            trade="Tile & Stone"
        ),
        "WT-01": MaterialSpec(
            symbol="WT-01",
            description="Glazed Ceramic Wall Tile, 84\" (7'-0\" AFF) Wainscot & Mop Basin Wet Wall Tile (NEMO Ceramic Metro 2x8 / Daltile)",
            manufacturer="NEMO Tile / Daltile",
            collection="Commercial Glazed Wall",
            size="2\"x8\" Metro / 3\"x6\"",
            finish="Gloss / Satin",
            color="Crisp White",
            unit="SQ FT",
            budget_price=9.50,
            notes="Full 84\" AFF wall tile at Girl's & Boy's Restrooms, 48\" AFF at Janitor's Closet.",
            trade="Tile & Stone"
        ),
        "WT-ACCENT": MaterialSpec(
            symbol="WT-ACCENT",
            description="Ceramic Sink & Urinal Feature Wall Tile, Full 84\" Height Accent (E24 Girl's Sink Wall, E33 Boy's Sink Wall & E35 Urinal)",
            manufacturer="Custom Ceramic / Designer Spec",
            collection="Accent Feature Series",
            size="Accent Module",
            finish="Satin",
            color="Feature Contrast Pattern",
            unit="SQ FT",
            budget_price=12.50,
            notes="Sink and urinal wet feature walls to 84\" AFF.",
            trade="Tile & Stone"
        ),
        "TB-1": MaterialSpec(
            symbol="TB-1",
            description="4\" Ceramic / Porcelain Sanitary Cove Base with Finished Rounded Top Edge",
            manufacturer="Matching Tile Mfr",
            collection="Cove Base",
            size="4\" High",
            finish="Matte",
            color="To Match Floor Pattern",
            unit="LN FT",
            budget_price=5.00,
            notes="Perimeter cove base at all tiled restrooms & janitor's closet.",
            trade="Tile & Stone"
        ),
        "SSF-1": MaterialSpec(
            symbol="SSF-1",
            description="Engineered Quartz / Solid Surface Custom Vanity Countertop (34\" AFF, 1-1/2\" Square Edge & 4\" Backsplash per Detail 10/A-500)",
            manufacturer="Caesarstone / Corian",
            collection="Commercial Solid Surface",
            size="2cm / 1-1/2\" Built-up Square Edge",
            finish="Polished / Matte Satin",
            color="Solid White / Neutral",
            unit="SQ FT",
            budget_price=45.00,
            notes="Custom 116-5/8\" top in Girl's WC with 4 undermount lavatory cutouts and 4\" backsplash.",
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
            notes="Entrance threshold transitions at restroom and closet doors.",
            trade="Tile & Stone"
        ),
        "WATERPROOF": MaterialSpec(
            symbol="WATERPROOF",
            description="Liquid-Applied Waterproofing Membrane (Laticrete Hydro Ban / RedGard ANSI A118.10), 100% Floor Slab Coverage & 8\" Up Walls",
            manufacturer="Laticrete",
            collection="Hydro Ban",
            size="Continuous Membrane",
            finish="Liquid Membrane",
            color="Green",
            unit="SQ FT",
            budget_price=2.50,
            notes="Full floor slab waterproofing under all wet restrooms & mop closet.",
            trade="Tile & Stone"
        ),
        "MUD-SET": MaterialSpec(
            symbol="MUD-SET",
            description="Portland Cement Mortar Bed (Mud-Set Wire-Mesh Reinforced Leveling & Pitch Bed, 1.25\" - 2.0\" Variable)",
            manufacturer="SpecChem / Laticrete",
            collection="Thick Bed Mortar",
            size="Variable Bed (+1/2\" finish)",
            finish="Troweled",
            color="Grey",
            unit="SQ FT",
            budget_price=3.75,
            notes="Mudset mortar leveling bed for +1/2\" floor elevations.",
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
            room_name="14TH FL - GIRL'S WC (ROOM 1424)",
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
                TakeoffLineItem("SSF-1", "COUNTERTOP", "QUARTZ", "S&I", 19.5, "SQ FT", 45.00, 50.00, "116-5/8\" Solid Surface Vanity Top (4 Cutouts & 4\" Backsplash per DTL 10/A-500)"),
                TakeoffLineItem("SADDLE", "THRESHOLD", "MARBLE SADDLE", "S&I", 1.0, "PCS", 50.00, 55.00, "Doorway Marble / Granite Transition Saddle"),
                TakeoffLineItem("TRIM-01", "TRIM", "METAL TRIM", "S&I", 35.0, "LN FT", 4.50, 6.50, "Schluter Wainscot Cap & Corner Profiles")
            ]
        ),
        RoomTakeoff(
            room_name="14TH FL - BOY'S WC (ROOM 1422)",
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
                TakeoffLineItem("SADDLE", "THRESHOLD", "MARBLE SADDLE", "S&I", 1.0, "PCS", 50.00, 55.00, "Doorway Marble / Granite Transition Saddle"),
                TakeoffLineItem("TRIM-01", "TRIM", "METAL TRIM", "S&I", 28.0, "LN FT", 4.50, 6.50, "Schluter Wainscot Cap & Corner Profiles")
            ]
        ),
        RoomTakeoff(
            room_name="14TH FL - JANITOR'S CLOSET (ROOM 1425)",
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
        )
    ]

    exclusions = [
        "1) Dance studio specialized flooring (Marley dance floors, sprung wood dance floors by Division 096400).",
        "2) Concrete slab structural trenching, slab infill or core drilling beyond minor floor prep.",
        "3) Dance studio wall mirrors, barre brackets, and collapsible partitions (by Specialties Division 10).",
        "4) Bathroom plumbing fixtures, faucets, grab bars, flush valves and soap dispensers (by MEP / Division 22).",
        "5) Premium / Overtime labor unless authorized in writing.",
        "6) Moisture mitigation / epoxy vapor barrier unless specified.",
        "7) DARK GRAY SHADED AREAS RULE: All rooms and areas shaded dark gray on architectural plans (Corridors 1400/1401/1413/1429/1431, Elevator Vestibules 1430 & 1412, Stair B, elevator shafts, and Room 1417 ADA WC) are strictly EXCLUDED (Existing to Remain / NIC / By Landlord / By Others).",
        "8) ELEVATOR LOBBY TERRAZZO: Elevator Lobby (Rooms 1430 & 1412, ~496.7 SF) is existing terrazzo floor to remain per Sheet A-011.00 note ('WHERE EXISTING TERRAZZO TILE ENDS') and walls are paint finish. Excluded from Base Bid (Available as Add-Alternate: +$21,279.84).",
        "9) ADA WC (ROOM 1417) & BROOM CLOSET: Shaded dark gray on sheet A-100 & A-011 (building core). Excluded from Base Bid (Available as Add-Alternate: +$12,788.80 for ADA WC and +$587.95 for Broom Closet).",
        "10) COUNTERTOP SUB-FRAMING & APRON: Countertop pricing includes 116-5/8\" horizontal Solid Surface slab top with square edge and 4\" backsplash per Detail 10/A-500. Countertop sub-framing, wood blocking, and 5\" Fixed P-Lam Apron are by Millwork contractor per Detail 01/A-500. Vertical Solid Surface drop apron / mitered face is strictly EXCLUDED unless requested by written change order.",
        "11) BOY'S WC (ROOM 1422): Features a wall-mounted lavatory fixture per Detail E33/ID-11 without countertop."
    ]

    inclusions = [
        "1) Supply & Install of specified Floor Tiles (Strip, Triangle & Diamond patterns) on 14th Floor (Rooms 1424, 1422, 1425).",
        "2) Supply & Install of full 84\" (7'-0\" AFF) glazed ceramic wall tile and sink/urinal accent feature walls.",
        "3) 100% floor slab liquid-applied waterproofing membrane (Laticrete Hydro Ban) in all restrooms & mop closet.",
        "4) Wire-mesh reinforced thick-bed mortar (Mudset) for +1/2\" floor elevations.",
        "5) Commercial 100% solids stain-resistant epoxy grout at all tiled floors & wet walls.",
        "6) Custom 116-5/8\" Solid Surface / Quartz vanity countertop in Girl's WC (Room 1424) with 4 undermount sink cutouts and 4\" backsplash.",
        "7) Polished marble / granite threshold saddles at all doorway transitions.",
        "8) Schluter aluminum metal trims at all outside wall tile corners and 84\" AFF wainscot top caps.",
        "9) Minor floor prep: mechanical scraping, substrate cleaning, divot patching and polymer flash-patching."
    ]

    notes = [
        "Project: DDF: Downtown Dance Factory - 225 Broadway, 14th Floor, New York, NY 10007.",
        "Drawing Reference: 90% CD & Bid Set Rev. 1 (Architect: Daniel Goldner Architects / Interior Design: Pink Green Interiors - Katie Hartell).",
        "Key Sheets: A-100.00 (Partition Plan), A-011.00 (Existing Plan), A-500.00 (Details 01 & 10), ID-1, ID-9 (Girl's WC), ID-11 (Boy's WC), ID-12 (Janitor's Closet), 1-Default-Section Rev. 2 (Finish Schedule).",
        "Official Room Numbers: Room 1424 (Girl's WC), Room 1422 (Boy's WC), Room 1425 (Janitor's Closet).",
        "Dark Gray Scope Rule: Rooms 1417 (ADA WC), 1430 & 1412 (Elevator Vestibules), Corridors 1400/1401/1413/1429/1431 and Broom Area are shaded dark gray on A-100 / A-011 and are excluded from Base Bid.",
        "Countertop / Apron Specification: Apron is 5\" Fixed P-Lam by Millwork per Detail 01/A-500. Tile & Stone scope includes horizontal Solid Surface slab & 4\" backsplash per Detail 10/A-500.",
        "Add-Alternates Available Upon Request: ADA Bathroom 1417 (+$12,788.80), Broom Closet (+$587.95), Elevator Lobby Terrazzo (+$21,279.84)."
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
