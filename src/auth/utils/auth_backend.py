from fastapi_users.authentication import AuthenticationBackend

from src.auth.utils.cookie import cookie_transport
from src.auth.utils.jwt import get_jwt_strategy


auth_backend = AuthenticationBackend(
    name='jwt',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
