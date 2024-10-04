from fastapi import FastAPI
from database import db
from models import Settings
from contextlib import asynccontextmanager
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    db.connect()
    db.create_tables([Settings], safe=True)
    yield
    db.close()

app = FastAPI(lifespan=lifespan)

@app.get("/ping")
def read_root():
    return {"message": "Pong!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
