#from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings():
    #DB_HOST: str
    #DB_PORT: int
    #DB_USER: str
    #DB_PASS: str
    #DB_NAME: str

    @property
    def DATABASE_URL_asyncpg(self):
        # postgresql+asyncpg://postgres:postgres@localhost:5432/sa
        return f"mysql+aiomysql://shadrin:Pa$$w0rd@KP11MYSQL-S1.OUIIT.LOCAL:3306/shadrin_db"

    @property
    def DATABASE_URL_psycopg(self):
        # DSN
        # postgresql+psycopg://postgres:postgres@localhost:5432/sa
        return f"mysql+pymysql://shadrin:Pa$$w0rd@KP11MYSQL-S1.OUIIT.LOCAL/shadrin_db"

    #model_config = SettingsConfigDict(env_file=".env")


settings = Settings()