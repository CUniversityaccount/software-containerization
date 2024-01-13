import asyncio
import redis.asyncio as redis
from typing import List
from .config import Settings
from .models import Item
class RedisDB:
    def __init__(self) -> None:
        settings = Settings()
        self.redis = redis.Redis(
            host=settings.redis_host, 
            port=settings.redis_port,
            decode_responses=True)
        pass

    async def get_all(self):
        keys = await self.redis.keys()
        tasks = [asyncio.create_task(self.redis.get(key)) for key in keys]
        await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
        return [{ "key": key, "value": t.result() } for key, t in zip(keys, tasks)]

    async def post(self, item : Item):
        return await self.redis.set(item.key, item.value)

