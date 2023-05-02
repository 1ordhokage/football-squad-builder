from pydantic import BaseSettings


class SMTPSettings(BaseSettings):
    user: str
    password: str
    host: str
    port: int

    class Config:
        env_file = ['../.env', '.env']
        env_prefix = 'SMTP_'


smtp_settings = SMTPSettings()
