# fastAPI Part 1

This folder contains a simple FastAPI project for learning the basics.

## What is included

- `main.py`: the main FastAPI application.
- `venv/`: a Python virtual environment for project dependencies.

## What the code does

- Creates a FastAPI app instance.
- Defines two routes:
  - `/`: returns a greeting message.
  - `/about`: returns a simple informational message.

## How to run

1. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
2. Install dependencies if needed:
   - `pip install fastapi uvicorn`
3. Start the server:
   - `uvicorn main:app --reload`
4. Open in browser:
   - `http://127.0.0.1:8000/`
   - `http://127.0.0.1:8000/about`

## Notes

- This is a beginner-level project to demonstrate how to define routes and return JSON responses.
- FastAPI automatically creates API docs at `http://127.0.0.1:8000/docs`.
