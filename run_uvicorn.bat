@echo on
:: run_server.bat
uvicorn main:app --reload
echo [UVICORN 실행 중...]