from pydantic import BaseSettings


class DBSettings(BaseSettings):
    connection_string: str

    class Config:
        env_file = '.env'
        env_prefix = 'DB_'


db_settings = DBSettings()
