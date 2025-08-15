from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from .auth import _users

router = APIRouter()

class ProgressReq(BaseModel):
    username: str
    checkpoint: Dict[str, Any] = {}

@router.patch('/save')
def save_progress(req: ProgressReq):
    user = _users.get(req.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user["progress"].update(req.checkpoint)
    return {"message": "Progress saved", "progress": user["progress"]}

@router.get('/{username}')
def get_progress(username: str):
    user = _users.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"progress": user["progress"]}
