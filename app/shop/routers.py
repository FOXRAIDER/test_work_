from fastapi import APIRouter, Depends, HTTPException, status

from app.db.database import SessionPg, get_postgres
from app.shop.schema import BrandSchema, CarSchema, ModelsSchema

from app.shop.services import Items


router = APIRouter(
    tags=["shop"],
    prefix="/items",
    dependencies=[],
)


@router.get(
    "/add_start_data",
    summary="add start data",
)
async def add_start_data(
    db: SessionPg = Depends(get_postgres),
):
    if result := Items(db=db).start_data():
        print(result)
        return "Successfully added"
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Запись не найдена или не доступна",
    )


@router.get(
    "/brands",
    summary="get brands",
    response_model=list[BrandSchema],
)
async def get_brands(
    db: SessionPg = Depends(get_postgres),
):
    if result := Items(db=db).get_brands():
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Запись не найдена или не доступна",
    )


@router.get(
    "/models",
    summary="get models",
    response_model=list[ModelsSchema],
)
async def get_models(
    db: SessionPg = Depends(get_postgres),
):
    if result := Items(db=db).get_models():
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Запись не найдена или не доступна",
    )


@router.get(
    "/cars",
    summary="get cars",
    response_model=list[CarSchema],
)
async def get_cars(
    db: SessionPg = Depends(get_postgres),
):
    if result := Items(db=db).get_cars():
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Запись не найдена или не доступна",
    )


@router.get(
    "/cars_by_id",
    summary="get cars by id",
    response_model=list[CarSchema],
)
async def get_cars_by_id(
    id: int,
    db: SessionPg = Depends(get_postgres),
):
    if result := Items(db=db).get_car_by_id(id):
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Запись не найдена или не доступна",
    )


@router.put(
    "/cars_by_id",
    summary="update cars by id",
    response_model=CarSchema,
)
async def update_cars_by_id(
    id: int,
    car: CarSchema = Depends(),
    db: SessionPg = Depends(get_postgres),
):
    if result := Items(db=db).update_cars_by_id(id, car):
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Запись не найдена или не доступна",
    )


@router.post(
    "/add_car",
    summary="add car",
    response_model=CarSchema,
)
async def add_car(
    car: CarSchema = Depends(),
    db: SessionPg = Depends(get_postgres),
):
    if result := Items(db=db).add_cars(car):
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Запись не найдена или не доступна",
    )


@router.delete(
    "/delete_car",
    summary="delete car",
    # response_model=CarSchema,
)
async def delete_car(
    id: int,
    db: SessionPg = Depends(get_postgres),
):
    if result := Items(db=db).delete_cars_by_id(id):
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Запись не найдена или не доступна",
    )
