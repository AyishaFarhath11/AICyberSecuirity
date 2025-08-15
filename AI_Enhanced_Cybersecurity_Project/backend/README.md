# Backend - AI-Enhanced Cybersecurity Threat Detector

This backend is a starter FastAPI application with:
- Authentication (signup/login) using JWT (in-memory for demo)
- Endpoints for ingesting data, requesting analysis, saving progress, and leaderboard
- Simple in-memory "database" abstraction (replace with MongoDB in production)

Quick start:
```
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
