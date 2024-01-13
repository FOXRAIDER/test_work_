from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    # DateTime,
    ForeignKey,
    # Boolean,
    # Table,
)

from app.mixins.time import Timestamp

Base = declarative_base()


class Brand(Base):
    __tablename__ = "brands"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    models = relationship("Model", back_populates="brand")


class Model(Base):
    __tablename__ = "models"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    brand_id = Column(Integer, ForeignKey("brands.id"))
    brand = relationship("Brand", back_populates="models")
    cars = relationship("Car", back_populates="model")


class Car(Base, Timestamp):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True)
    brand_id = Column(Integer, ForeignKey("brands.id"))
    model_id = Column(Integer, ForeignKey("models.id"))
    brand = relationship("Brand")
    model = relationship("Model", back_populates="cars")
    power = Column(Float, nullable=True)
