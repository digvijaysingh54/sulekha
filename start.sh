#!/bin/bash

# Sulekha Singh Tribute Website - Server Startup Script for Mac/Linux

echo ""
echo "========================================"
echo "  Sulekha Singh Tribute Website"
echo "  Starting Local Server..."
echo "========================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed!"
    echo ""
    echo "Please install Python 3:"
    echo "  - macOS: brew install python3"
    echo "  - Ubuntu: sudo apt-get install python3"
    echo "  - Or download from: https://www.python.org/downloads/"
    echo ""
    exit 1
fi

echo "Using Python 3 to start server..."
echo ""
echo "🌐 Server starting on: http://localhost:8000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 -m http.server 8000
