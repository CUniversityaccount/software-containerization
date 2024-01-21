import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from typing import List
from .config import Settings
from .models import Item

class MongoDB:
    def __init__(self) -> None:
        settings = Settings()
        self.client = AsyncIOMotorClient(settings.mongo_url).services
        pass

    async def get_all(self):
        print(self.client)
        return [Item(**item) for item in await self.client["values"].find().to_list(length=1000) ]

    async def post(self, item : Item):
        # TODO: Add index when the db is created
        await self.client["values"].create_index("key", unique=True)
        await self.client["values"].insert_one(item.model_dump())

