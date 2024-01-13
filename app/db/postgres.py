""" Репозиторий работы с PostgreSQL. """
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import select
from .database import ISQLRepository
from app.db.config import DATABASE


class Postgtes(ISQLRepository):
    """
    Репозиторий работы с PostgreSQL.
    """

    def __init__(self, *args, **kwargs):
        self.engine = create_async_engine(
            f"postgresql+asyncpg://{DATABASE.user}:"
            + f"{DATABASE.password}@{DATABASE.host}:"
            + f"{DATABASE.port}/{DATABASE.db}",
        )
        self.async_session = async_sessionmaker(self.engine, expire_on_commit=False)
        self.model = None

    @property
    def model(self):
        return self.model

    @model.setter
    def model(self, model):
        self.model = model

    async def get_all(self, *args, **kwargs):
        """Метод возвращает все записи по фильтру из БД."""
        async with self.async_session() as session:
            query = select(self.model).where(*args, **kwargs)
            data_table = await session.execute(query)
            return data_table.scalars().all()

    async def get(self, *args, **kwargs):
        """Метод возвращает первую запись по фильтру из БД."""
        async with self.async_session() as session:
            query = select(self.model).where(*args, **kwargs)
            data_table = await session.execute(query)
            return data_table.scalars().first()

    async def create(self, *args, **kwargs):
        """Метод добавляет новую запись в БД."""
        async with self.async_session() as session:
            new_object = self.model(**kwargs)
            session.add(new_object)
            await session.commit()
            return new_object

    async def update(self, *args, **kwargs):
        """Метод обновляет запись в БД."""
        async with self.async_session() as session:
            new_object = self.model(**kwargs)
            session.add(new_object)
            await session.commit()
            return new_object

    async def delete(self, *args, **kwargs):
        """Метод удаляет запись из БД."""
        async with self.async_session() as session:
            new_object = self.model(**kwargs)
            session.delete(new_object)
            await session.commit()
            return new_object
