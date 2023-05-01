from fastapi_users.authentication import JWTStrategy

from src.auth.config import jwt_settings


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=jwt_settings.secret, lifetime_seconds=3600)
