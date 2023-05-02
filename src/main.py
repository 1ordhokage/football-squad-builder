from fastapi import FastAPI

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

from src.auth.router.auth import router as auth_router
from src.auth.router.users import router as users_router
from src.players.router import router as players_router
from src.squads.router import router as squads_router


app = FastAPI(
    title='FootSquad',
    description='Football squad builder.',
    version='0.0.1',
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(players_router)
app.include_router(squads_router)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
