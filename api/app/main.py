from fastapi import FastAPI, Depends, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated

from .db import MongoDB
from .models import Item

app = FastAPI()
router = APIRouter(prefix="/api")

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
    yield MongoDB()

DBDep = Annotated[MongoDB, Depends(get_db)]


@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/items")
async def get_items(db : DBDep):
    items = await db.get_all()
    return {"items": items }

@router.post("/items")
async def post(db : DBDep, new_item: Item):
    ok = await db.post(new_item)
    return ok

app.include_router(router) 
#Open your browser at http://127.0.0.1:8000. 