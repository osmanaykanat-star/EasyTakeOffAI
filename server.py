import sys, os
sys.path.insert(0, r"C:\Users\azran\.gemini\antigravity\scratch\EasyTakeOffAI")
import uvicorn
from backend.app import app

if __name__ == "__main__":
    print("Starting EasyTakeOffAI on http://0.0.0.0:8000 (Local IP: http://192.168.86.44:8000) ...")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
