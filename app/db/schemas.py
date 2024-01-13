from pydantic import BaseModel


class DatabaseConfig(BaseModel):
    user: str
    password: str
    host: str
    db: str


class PostgresConfig(DatabaseConfig):
    port: int
