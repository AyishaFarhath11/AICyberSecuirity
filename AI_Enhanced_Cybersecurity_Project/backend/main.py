from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import auth, ingest, analyze, progress, leaderboard

app = FastAPI(title="AI-Enhanced Cybersecurity Threat Detector - Backend")

# Allow local dev from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(ingest.router, prefix="/ingest", tags=["ingest"])
app.include_router(analyze.router, prefix="/analyze", tags=["analyze"])
app.include_router(progress.router, prefix="/progress", tags=["progress"])
app.include_router(leaderboard.router, prefix="/leaderboard", tags=["leaderboard"])

@app.get('/health')
def health():
    return {'status': 'ok'}
