@echo off
echo [UVICORN 종료 중...]
taskkill /IM uvicorn.exe /F
echo [완료됨! 창을 닫거나 계속 진행하세요.]
pause