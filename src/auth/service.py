from fastapi import Request

from fastapi_users import BaseUserManager, IntegerIDMixin

from src.auth.config import jwt_settings
from src.auth.models import User
from src.tasks.tasks import send_welcome_email


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = jwt_settings.secret
    verification_token_secret = jwt_settings.secret

    async def on_after_register(self, user: User, request: Request | None = None):
        send_welcome_email.delay(user.username, user.email)
