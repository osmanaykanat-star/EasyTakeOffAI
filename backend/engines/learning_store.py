import os
import json
from typing import Dict, Any, Optional

SETTINGS_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "trade_settings.json")
PROFILE_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "user_profile.json")

DEFAULT_SETTINGS = {
    "company": {
        "name": "",
        "address": "",
        "phone": "",
        "email": "",
        "license_no": "",
        "logo_url": ""
    },
    "trade_rules": {
        "standard_tile_waste_pct": 10.0,
        "large_format_waste_pct": 15.0,
        "mosaic_waste_pct": 12.0,
        "slab_waste_pct": 20.0,
        "include_floor_waterproofing": True,
        "waterproof_base_height_inches": 6.0,
        "waterproof_shower_wall_full_height": True,
        "include_mudset_bed": True,
        "standard_mudset_thickness_inches": 1.5,
        "saddle_per_single_door": 1,
        "saddle_per_double_door": 2,
        "default_ceiling_height_ft": 9.0
    },
    "labor_rates": {
        "floor_tile_install_sqft": 14.50,
        "wall_tile_install_sqft": 18.00,
        "tile_base_install_lnft": 8.50,
        "waterproofing_install_sqft": 3.25,
        "mudset_bed_install_sqft": 5.50,
        "countertop_slab_sqft": 45.00,
        "saddle_install_pcs": 45.00,
        "metal_trim_install_lnft": 6.00,
        "epoxy_grout_adder_sqft": 2.50
    },
    "standard_terms": [
        "Proposal is valid for 60 calendar days from bid date.",
        "All work to be performed during standard business hours (7:00 AM - 3:30 PM).",
        "Substrates must be clean, structurally sound, and within 1/8\" in 10'-0\" tolerance prior to install.",
        "Epoxy grout, premium/overtime labor, and air freight are excluded unless specifically noted."
    ]
}

DEFAULT_PROFILE = {
    "company_name": "",
    "estimator_name": "",
    "estimator_title": "Senior Estimator",
    "address": "",
    "phone": "",
    "email": "",
    "website": "",
    "trade_specialty": "Tile & Stone",
    "license_no": "",
    "is_registered": False
}

class LearningStore:
    """
    Active Learning & Trade Configuration Persistence Store:
    - Saves user-edited rates, company branding, and trade rules
    - Saves user/company registration profile
    - Loads settings on app startup
    """

    @staticmethod
    def get_settings() -> Dict[str, Any]:
        if os.path.exists(SETTINGS_FILE):
            try:
                with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                    saved = json.load(f)
                    merged = DEFAULT_SETTINGS.copy()
                    for k, v in saved.items():
                        if isinstance(v, dict) and k in merged:
                            merged[k].update(v)
                        else:
                            merged[k] = v
                    return merged
            except Exception:
                pass
        return DEFAULT_SETTINGS.copy()

    @staticmethod
    def save_settings(new_settings: Dict[str, Any]) -> Dict[str, Any]:
        os.makedirs(os.path.dirname(SETTINGS_FILE), exist_ok=True)
        current = LearningStore.get_settings()
        for k, v in new_settings.items():
            if isinstance(v, dict) and k in current:
                current[k].update(v)
            else:
                current[k] = v
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(current, f, indent=2)
        return current

    @staticmethod
    def get_user_profile() -> Dict[str, Any]:
        if os.path.exists(PROFILE_FILE):
            try:
                with open(PROFILE_FILE, "r", encoding="utf-8") as f:
                    saved = json.load(f)
                    res = DEFAULT_PROFILE.copy()
                    res.update(saved)
                    return res
            except Exception:
                pass
        return DEFAULT_PROFILE.copy()

    @staticmethod
    def save_user_profile(profile_data: Dict[str, Any]) -> Dict[str, Any]:
        os.makedirs(os.path.dirname(PROFILE_FILE), exist_ok=True)
        current = LearningStore.get_user_profile()
        current.update(profile_data)
        current["is_registered"] = True
        with open(PROFILE_FILE, "w", encoding="utf-8") as f:
            json.dump(current, f, indent=2)
        return current
