from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.config import DATABASE

pg_url = f"postgresql+psycopg2://{DATABASE.user}:{DATABASE.password}@{DATABASE.host}:{DATABASE.port}/{DATABASE.db}"
pg_engine = create_engine(pg_url)
SessionPg = sessionmaker(autocommit=False, autoflush=False, bind=pg_engine)


def get_postgres():
    db_pg = SessionPg()
    try:
        yield db_pg
    finally:
        db_pg.close()
