from fastapi import FastAPI

from src.auth.router.auth import router as auth_router
from src.auth.router.users import router as users_router

app = FastAPI(
    title='FootSquad',
    description='Football squad builder.',
    version='0.0.1',
)

app.include_router(auth_router)
app.include_router(users_router)
