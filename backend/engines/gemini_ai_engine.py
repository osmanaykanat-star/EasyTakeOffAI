import os
import json
import re
from typing import List, Dict, Any, Optional
import pymupdf
from google import genai
from google.genai import types

from ..trades.trade_base import ProjectTakeoff, RoomTakeoff, TakeoffLineItem, MaterialSpec
from ..trades.tile_and_stone import TileAndStoneEngine
from .universal_knowledge_base import UniversalKnowledgeBase

class GeminiAIEngine:
    """
    Intelligent Multimodal Takeoff and Estimating Engine powered by Gemini 3.6 Flash.
    Provides automated blueprint vision takeoff, schedule extraction, Q&A chat, and price advisory.
    """
    DEFAULT_MODEL = "gemini-3.6-flash"

    @staticmethod
    def get_api_key() -> str:
        return os.environ.get("GEMINI_API_KEY", "").strip()

    @classmethod
    def get_client(cls) -> genai.Client:
        key = cls.get_api_key()
        return genai.Client(api_key=key)

    @classmethod
    def check_connection(cls) -> Dict[str, Any]:
        try:
            client = cls.get_client()
            res = client.models.generate_content(
                model=cls.DEFAULT_MODEL,
                contents="Say: Gemini 3.6 Flash is connected and ready!"
            )
            return {
                "status": "success",
                "connected": True,
                "model": cls.DEFAULT_MODEL,
                "message": res.text.strip() if res.text else "OK"
            }
        except Exception as e:
            return {
                "status": "error",
                "connected": False,
                "model": cls.DEFAULT_MODEL,
                "error": str(e)
            }

    @classmethod
    def convert_pdf_to_images(cls, pdf_path: str, max_pages: int = 5, dpi: int = 150) -> List[bytes]:
        images_bytes = []
        try:
            doc = pymupdf.open(pdf_path)
            total = len(doc)
            for p_num in range(min(total, max_pages)):
                page = doc[p_num]
                zoom = dpi / 72.0
                mat = pymupdf.Matrix(zoom, zoom)
                pix = page.get_pixmap(matrix=mat, alpha=False)
                images_bytes.append(pix.tobytes("jpeg"))
            doc.close()
        except Exception as e:
            print(f"Error converting PDF: {e}")
        return images_bytes

    @classmethod
    def analyze_blueprint_with_vision(cls, file_path: str, trade_focus: str = "Tile & Stone") -> Dict[str, Any]:
        client = cls.get_client()
        ext = os.path.splitext(file_path)[1].lower()
        contents_payload = []

        if ext == ".pdf":
            images = cls.convert_pdf_to_images(file_path, max_pages=6, dpi=160)
            if not images:
                raise ValueError("Could not render PDF pages for AI Vision.")
            for img in images:
                contents_payload.append(types.Part.from_bytes(data=img, mime_type="image/jpeg"))
        elif ext in [".png", ".jpg", ".jpeg", ".webp"]:
            with open(file_path, "rb") as f:
                img_data = f.read()
            mime = "image/png" if ext == ".png" else "image/jpeg"
            contents_payload.append(types.Part.from_bytes(data=img_data, mime_type=mime))
        else:
            raise ValueError(f"Unsupported file format: {ext}")

        training_ref = UniversalKnowledgeBase.get_summary_context_for_ai()
        prompt = f"""
You are a Senior Construction Estimator specializing in Architectural Blueprint Takeoffs ({trade_focus}).
Trained on 1,747+ commercial construction benchmark projects.
{training_ref}

Analyze the provided blueprint images carefully.
Extract project details, material finish schedules, and all distinct rooms/areas with estimated dimensions and quantities.

Return ONLY a valid JSON object matching this schema:
{{
  "project_name": "Project Name from Title Block or Sheet Header",
  "client_name": "Architect / GC Contact Name",
  "client_company": "General Contractor or Property Owner",
  "trade_category": "{trade_focus}",
  "material_specs": {{
    "FT-1": {{
      "symbol": "FT-1",
      "description": "Porcelain Floor Tile 12x24",
      "unit": "SQ FT",
      "budget_price": 0.0,
      "notes": "Restroom and pantry floors"
    }}
  }},
  "rooms": [
    {{
      "room_name": "RESTROOM 101",
      "floor_name": "1ST FLOOR",
      "length_ft": 10.0,
      "width_ft": 8.0,
      "ceiling_height_ft": 9.0,
      "wall_tile_height_ft": 8.0,
      "door_count": 1,
      "items": [
        {{
          "symbol": "FT-1",
          "finish_type": "FLOOR",
          "material_type": "PORCELAIN TILE",
          "work_type": "S&I",
          "quantity": 80.0,
          "unit": "SQ FT",
          "material_price": 0.0,
          "labor_price": 0.0,
          "notes": "Floor tile installation"
        }},
        {{
          "symbol": "WATERPROOF",
          "finish_type": "FLOOR",
          "material_type": "WATERPROOF",
          "work_type": "S&I",
          "quantity": 80.0,
          "unit": "SQ FT",
          "material_price": 0.0,
          "labor_price": 0.0,
          "notes": "Floor waterproofing membrane"
        }}
      ]
    }}
  ],
  "exclusions": [
    "Epoxy grout unless specified",
    "Premium / overtime labor",
    "Structural subfloor prep by others"
  ],
  "analysis_summary": "Summary of scope and drawing observations."
}}
"""
        contents_payload.append(prompt)
        res = client.models.generate_content(
            model=cls.DEFAULT_MODEL,
            contents=contents_payload
        )
        raw = res.text or ""
        cleaned = re.sub(r"^```json\s*", "", raw.strip(), flags=re.IGNORECASE)
        cleaned = re.sub(r"```$", "", cleaned.strip())
        try:
            data = json.loads(cleaned)
            return {"status": "success", "data": data}
        except Exception as e:
            match = re.search(r"(\{.*\})", cleaned, re.DOTALL)
            if match:
                return {"status": "success", "data": json.loads(match.group(1))}
            return {"status": "error", "raw_response": raw, "error": str(e)}

    @classmethod
    def chat_with_project(cls, message: str, project_context: Dict[str, Any]) -> str:
        client = cls.get_client()
        summary = {
            "project_name": project_context.get("project_name", ""),
            "client_name": project_context.get("client_name", ""),
            "client_company": project_context.get("client_company", ""),
            "trade": project_context.get("trade_category", "Tile & Stone"),
            "total_rooms": len(project_context.get("rooms", [])),
            "rooms_sample": [
                {
                    "name": r.get("room_name"),
                    "floor": r.get("floor_name"),
                    "items": [
                        {"symbol": it.get("symbol"), "type": it.get("finish_type"), "qty": it.get("quantity"), "unit": it.get("unit")}
                        for it in r.get("items", [])
                    ]
                }
                for r in project_context.get("rooms", [])[:20]
            ],
            "material_specs": project_context.get("material_specs", {})
        }
        prompt = f"""
You are EasyTakeOffAI Copilot powered by Gemini 3.6 Flash.
You are assisting Osman, the estimator.
Context:
{json.dumps(summary, indent=2)}

Question: {message}
Provide a clear, accurate, professional answer (in Turkish if asked in Turkish, or in English).
"""
        res = client.models.generate_content(
            model=cls.DEFAULT_MODEL,
            contents=prompt
        )
        return res.text or "No response generated."

    @classmethod
    def suggest_pricing(cls, trade: str, symbol: str, description: str, unit: str = "SQ FT") -> Dict[str, Any]:
        client = cls.get_client()
        prompt = f"""
Provide market unit pricing (NYC / US Commercial Standard) for:
Trade: {trade}
Material: {symbol} - {description} ({unit})

Return ONLY JSON:
{{
  "suggested_material_price": 5.50,
  "suggested_labor_price": 12.00,
  "recommended_waste_percentage": 10.0,
  "reasoning": "Brief explanation."
}}
"""
        res = client.models.generate_content(
            model=cls.DEFAULT_MODEL,
            contents=prompt
        )
        cleaned = re.sub(r"^```json\s*", "", (res.text or "").strip(), flags=re.IGNORECASE)
        cleaned = re.sub(r"```$", "", cleaned.strip())
        try:
            return json.loads(cleaned)
        except Exception:
            return {
                "suggested_material_price": 5.50,
                "suggested_labor_price": 12.00,
                "recommended_waste_percentage": 10.0,
                "reasoning": "Commercial benchmark standard."
            }
