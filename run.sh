#!/bin/bash

python3 -m venv env
echo "Virtual environment created."

echo "Activating virtual environment..."
source env/bin/activate

echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Starting FastAPI server..."
uvicorn main:app --reload
