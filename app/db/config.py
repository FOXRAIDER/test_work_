import os
from app.db.schemas import PostgresConfig
from dotenv import load_dotenv


load_dotenv()


DATABASE = PostgresConfig(
    user=os.environ.get("POSTGRES_USER"),
    password=os.environ.get("POSTGRES_PASSWORD"),
    host=os.environ.get("POSTGRES_HOST"),
    db=os.environ.get("POSTGRES_DB"),
    port=os.environ.get("POSTGRES_PORT"),
)
