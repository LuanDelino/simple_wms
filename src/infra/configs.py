from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://wms:wms@localhost:5432/wms'
    DB_ECHO: bool = False

    class Config:
        case_sensitive = True


settings: Settings = Settings()
