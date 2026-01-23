#!/usr/bin/env bash
set -e
echo "Installing Stamp for Python..."
if ! command -v python3 >/dev/null 2>&1; then # if that then python not found
    echo "python3 not found. Please install Python 3.10+."
    exit 1
fi
read -n 1 -p "Do you want to updgrade pip? [y/n]: " response
if [[ "$response" =~ ^[Yy]$ ]]; then
    python3 -m pip install --upgrade pip
    python3 -m pip install .
else;
    python3 -m pip install .
echo "Installation complete."