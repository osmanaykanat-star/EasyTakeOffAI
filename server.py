import sys, os
sys.path.insert(0, r"C:\Users\azran\.gemini\antigravity\scratch\EasyTakeOffAI")
import uvicorn
from backend.app import app

if __name__ == "__main__":
    print("Starting EasyTakeOffAI on http://127.0.0.1:8000 ...", flush=True)
    uvicorn.run("backend.app:app", host="127.0.0.1", port=8000, log_level="info")

