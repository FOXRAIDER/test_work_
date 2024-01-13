from pydantic import BaseModel


class ModelsSchema(BaseModel):
    name: str


class BrandSchema(BaseModel):
    name: str


class CarSchema(BaseModel):
    brand_name: str
    model_name: str
    power: float
