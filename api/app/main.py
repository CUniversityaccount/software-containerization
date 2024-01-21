from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated

from .db import RedisDB
from .models import Item

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:7500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    yield RedisDB()

DBDep = Annotated[RedisDB, Depends(get_db)]


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items")
async def get_items(db : DBDep):
    items = await db.get_all()
    return {"items": items }

@app.post("/items")
async def post(db : DBDep, new_item: Item):
    ok = await db.post(new_item)
    return ok

#Open your browser at http://127.0.0.1:8000.