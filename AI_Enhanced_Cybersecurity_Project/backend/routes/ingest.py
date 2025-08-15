from fastapi import APIRouter, UploadFile, File, Depends
from pydantic import BaseModel
from typing import Dict
from .auth import get_current_user

router = APIRouter()

class IngestResp(BaseModel):
    message: str

@router.post('/', response_model=IngestResp)
async def ingest(file: UploadFile = File(...), token: str = None):
    # For demo, we just read bytes and return success.
    # In production: parse PCAP / logs, normalize, store to DB or vector store
    contents = await file.read()
    size = len(contents)
    return {"message": f"Received {file.filename} ({size} bytes)"}
