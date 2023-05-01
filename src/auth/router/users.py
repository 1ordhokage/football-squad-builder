from fastapi import APIRouter

from fastapi_users import FastAPIUsers

from src.auth.models import User
from src.auth.schemas import UserRead, UserUpdate
from src.auth.utils.auth_backend import auth_backend
from src.auth.utils.users import get_user_manager


router = APIRouter()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix='/users',
    tags=['users'],
)
