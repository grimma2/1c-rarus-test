from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = 'sqlite+aiosqlite:///test.db'
    echo_sql: bool = True
    test: bool = False
    debug_logs: bool = False
    project_name: str = "ToDo"


settings = Settings()
