from fastapi import Request

from fastapi_users import BaseUserManager, IntegerIDMixin

from src.auth.config import jwt_settings
from src.auth.models import User


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = jwt_settings.secret
    verification_token_secret = jwt_settings.secret

    async def on_after_register(self, user: User, request: Request | None = None):
        print(f'User {user.id} has registered.')
