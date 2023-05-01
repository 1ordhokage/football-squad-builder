from pydantic import BaseSettings


class JWTSettings(BaseSettings):
    secret: str

    class Config:
        env_file = '.env'
        env_prefix = 'JWT_'


jwt_settings = JWTSettings()
