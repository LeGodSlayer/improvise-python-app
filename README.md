# Improvise Python App

This project is a FastAPI-based application with endpoints to generate tokens and compute text checksums.

## Features
- **GET /token** → Returns a demo token
- **POST /generate** → Accepts JSON `{ "text": "..." }` and returns:
  - Welcome message
  - Original text
  - SHA-256 checksum
- **GET /health** → Healthcheck endpoint

## Requirements
- Python 3.10+
- pip

## Install
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

