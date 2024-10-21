#!/bin/bash

set -e
cd "$(dirname "$0")/../.." || exit 1

error() {
    echo "ERROR: $1" >&2
    exit 1
}

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv || error "Failed to create virtual environment. Is Python installed?"
fi

echo "Activating virtual environment..."
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
elif [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
else
    error "virtual environment activation script not found"
fi

echo "upgrading pip..."
python -m pip install --upgrade pip || error "Failed to upgrade pip."

echo "installing dependencies..."
echo "current directory: $(pwd)"
if [ -f "$(pwd)/scribeparse/requirements.txt" ]; then
    echo "found requirements.txt in: $(pwd)/scribeparse/requirements.txt"
    pip install -r "$(pwd)/scribeparse/requirements.txt" || error "failed to install dependencies."
else
    error "requirements.txt not found in $(pwd)/scribeparse/requirements.txt"
fi

echo "setup has completed" 

