import sys, os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import uvicorn
from backend.app import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0"
    print(f"Starting EasyTakeOffAI on http://{host}:{port} ...", flush=True)
    uvicorn.run("backend.app:app", host=host, port=port, log_level="info")


