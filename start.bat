@echo off
REM Sulekha Singh Tribute Website - Server Startup Script for Windows

echo.
echo ========================================
echo   Sulekha Singh Tribute Website
echo   Starting Local Server...
echo ========================================
echo.

echo Using Python to start server...
echo.
echo Server starting on: http://localhost:8000
echo.
echo Press Ctrl+C to stop the server
echo.

python -m http.server 8000

pause
