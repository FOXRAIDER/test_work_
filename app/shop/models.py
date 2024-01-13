from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    # DateTime,
    # ForeignKey,
    # Boolean,
    # Table,
)

from app.mixins.time import Timestamp

Base = declarative_base()


class Models(Base):
    id = Column(Integer, nullable=False, primary_key=True)
    id_brand = relationship("Brand", back_populates="cars")
    name = Column(String, nullable=False)


class Brand(Base):
    id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)


class Car(Base, Timestamp):
    """Table with cars."""

    __tablename__ = "cars"
    id = Column(Integer, primary_key=True)
    brand = relationship("Brand", back_populates="cars")
    model = relationship("Models", back_populates="cars")
    power = Column(Float, nullable=False)
