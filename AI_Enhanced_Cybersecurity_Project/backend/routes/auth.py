from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Dict
from jose import JWTError, jwt
from passlib.context import CryptContext

router = APIRouter()

# NOTE: In production, move secret to env / secrets manager
SECRET_KEY = "dev-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# simple in-memory user store for demo; replace with real DB
_users: Dict[str, Dict] = {}

class SignupReq(BaseModel):
    username: str
    password: str

class TokenResp(BaseModel):
    access_token: str
    token_type: str

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post('/signup')
def signup(req: SignupReq):
    if req.username in _users:
        raise HTTPException(status_code=400, detail="User exists")
    _users[req.username] = {
        "username": req.username,
        "password_hash": get_password_hash(req.password),
        "created_at": datetime.utcnow().isoformat(),
        "total_score": 0,
        "progress": {}
    }
    token = create_access_token({"sub": req.username}, timedelta(hours=2))
    return {"access_token": token, "token_type": "bearer"}

class LoginReq(BaseModel):
    username: str
    password: str

@router.post('/login', response_model=TokenResp)
def login(req: LoginReq):
    user = _users.get(req.username)
    if not user or not verify_password(req.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": req.username}, timedelta(hours=2))
    return {"access_token": token, "token_type": "bearer"}

# simple dependency for demo
def get_current_user(token: str = None):
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None or username not in _users:
            raise HTTPException(status_code=401, detail="Invalid token")
        return _users[username]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
