from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from database import db
from models import Settings, User
from contextlib import asynccontextmanager
import uvicorn
from datetime import datetime, timedelta
import bcrypt
import jwt
from pydantic import BaseModel
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "you really need to change this!")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)

class Token(BaseModel):
    access_token: str
    token_type: str

@asynccontextmanager
async def lifespan(app: FastAPI):
    db.connect()
    db.create_tables([Settings, User], safe=True)
    yield
    db.close()

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  #TODO: Adjust this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(datetime.UTC) + expires_delta
    else:
        expire = datetime.now(datetime.UTC) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.post("/register")
async def register(form_data: OAuth2PasswordRequestForm = Depends()):
    hashed_password = bcrypt.hashpw(form_data.password.encode('utf-8'), bcrypt.gensalt())
    try:
        user = User.create(
            username=form_data.username,
            password=hashed_password.decode('utf-8'),
            created_at=datetime.now()
        )
    except Exception:
        raise HTTPException(status_code=400, detail="Email already registered")
    return {"message": "User created successfully"}

@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = User.get_or_none(User.username == form_data.username)
    if not user or not bcrypt.checkpw(form_data.password.encode('utf-8'), user.password.encode('utf-8')):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/ping")
def read_root():
    return {"message": "Pong!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
