@echo off
title EasyTakeOffAI - Desktop Takeoff Suite
cd /d "%~dp0"
echo ========================================================
echo   EasyTakeOffAI - Intelligent Construction Takeoff
echo   Designed for Trade Takeoffs (Tile & Stone)
echo ========================================================
echo.
echo Starting local application server on http://127.0.0.1:8000 ...
start http://127.0.0.1:8000
python -m uvicorn backend.app:app --host 127.0.0.1 --port 8000 --reload
pause
