from fastapi import APIRouter
from typing import List, Dict
from .auth import _users

router = APIRouter()

@router.get('/')
def leaderboard():
    # Return top users by total_score (demo in-memory)
    users = list(_users.values())
    users_sorted = sorted(users, key=lambda u: u.get('total_score', 0), reverse=True)
    return [{"username": u['username'], "score": u.get('total_score', 0)} for u in users_sorted]
