#!/bin/bash

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create the .env file if it doesn't exist
if [ ! -f .env ]; then
  echo "Creating .env file..."
  echo "API_KEY=y27vLBACEbsZIckn-8HPcIUwVyjDnqqAkJlYy_oZI3M" >> .env
fi

# Start the FastAPI server
uvicorn main:app --reload
