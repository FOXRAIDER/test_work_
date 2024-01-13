import os
from app.db.schemas import PostgresConfig
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))
file_env_path = os.path.join(current_dir, ".env")
load_dotenv(file_env_path)


DATABASE = PostgresConfig(
    user=os.environ.get("POSTGRES_USER"),
    password=os.environ.get("POSTGRES_PASSWORD"),
    host=os.environ.get("POSTGRES_HOST"),
    db=os.environ.get("POSTGRES_DB"),
    port=os.environ.get("POSTGRES_PORT"),
)
