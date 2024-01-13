from fastapi import HTTPException, status
from app.shop.models import Brand, Car, Model
from app.shop.schema import BrandSchema, CarSchema, ModelsSchema


class Items:
    def __init__(self, db):
        self.db = db

    def start_data(self):
        brand1 = Brand(name="Toyota")
        brand2 = Brand(name="Ford")
        brand3 = Brand(name="Volkswagen")
        self.db.add_all([brand1, brand2, brand3])
        self.db.commit()

        # Добавляем модели
        model1 = Model(name="Camry", brand=brand1)
        model2 = Model(name="Corolla", brand=brand1)
        model3 = Model(name="Focus", brand=brand2)
        model4 = Model(name="Mustang", brand=brand2)
        model5 = Model(name="Golf", brand=brand3)
        model6 = Model(name="Passat", brand=brand3)
        model7 = Model(name="Polo", brand=brand3)
        model8 = Model(name="Tiguan", brand=brand3)
        model9 = Model(name="Touareg", brand=brand3)
        model10 = Model(name="Jetta", brand=brand3)
        self.db.add_all(
            [
                model1,
                model2,
                model3,
                model4,
                model5,
                model6,
                model7,
                model8,
                model9,
                model10,
            ]
        )
        self.db.commit()

        # Добавляем автомобили
        car1 = Car(brand=brand1, model=model1, power=115.0)
        car2 = Car(brand=brand1, model=model2, power=120.0)
        car3 = Car(brand=brand2, model=model3, power=250.0)
        car4 = Car(brand=brand2, model=model4, power=300.0)
        car5 = Car(brand=brand3, model=model5, power=180.0)
        car6 = Car(brand=brand3, model=model6, power=200.0)
        car7 = Car(brand=brand3, model=model7, power=150.0)
        car8 = Car(brand=brand3, model=model8, power=250.0)
        car9 = Car(brand=brand3, model=model9, power=250.0)
        car10 = Car(brand=brand3, model=model10, power=250.0)
        self.db.add_all([car1, car2, car3, car4, car5, car6, car7, car8, car9, car10])
        self.db.commit()

        return

    def get_brands(self):
        return [BrandSchema(name=x.name) for x in self.db.query(Brand).all()]

    def get_models(self):
        return [ModelsSchema(name=x.name) for x in self.db.query(Model).all()]

    def get_cars(self):
        cars = (
            self.db.query(Car.power, Brand.name, Model.name)
            .select_from(Car)
            .join(Brand, Brand.id == Car.brand_id)
            .join(Model, Model.id == Car.model_id)
            .group_by(Car.id, Brand.name, Model.name)
            .all()
        )
        return [
            CarSchema(
                power=power,
                brand_name=brand_name,
                model_name=model_name,
            )
            for power, brand_name, model_name in cars
        ]

    def get_car_by_id(self, id):
        cars = (
            self.db.query(Car.power, Brand.name, Model.name)
            .select_from(Car)
            .join(Brand, Brand.id == Car.brand_id)
            .join(Model, Model.id == Car.model_id)
            .group_by(Car.id, Brand.name, Model.name)
            .filter(Car.id == id)
            .all()
        )
        return [
            CarSchema(
                power=power,
                brand_name=brand_name,
                model_name=model_name,
            )
            for power, brand_name, model_name in cars
        ]

    def update_cars_by_id(self, id, car_upd: CarSchema):
        # TODO: добавить проверку на существование Бренда или Модели
        car = self.db.query(Car).filter(Car.id == id).first()
        car.brand = Brand(name=car_upd.brand_name)
        car.model = Model(name=car_upd.model_name)
        car.power = car_upd.power
        self.db.add(car)
        self.db.commit()
        return CarSchema(
            brand_name=car.brand.name,
            model_name=car.model.name,
            power=car.power,
        )

    def delete_cars_by_id(self, id):
        car = self.db.query(Car).filter(Car.id == id).first()
        if car:
            self.db.delete(car)
            self.db.commit()
            return True
        return False

    def add_cars(self, car: CarSchema):
        if (
            self.db.query(Car)
            .filter(
                Car.brand.has(name=car.brand_name),
                Car.model.has(name=car.model_name),
                Car.power == car.power,
            )
            .first()
        ):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Автомобиль с такими характеристиками уже существует",
            )
        if not self.db.query(Brand).filter(Brand.name == car.brand_name).first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Бренд не найден",
            )
        if not self.db.query(Model).filter(Model.name == car.model_name).first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Модель не найдена",
            )
        brand = self.db.query(Brand).filter(Brand.name == car.brand_name).first()
        model = self.db.query(Model).filter(Model.name == car.model_name).first()
        car = Car(brand=brand, model=model, power=car.power)
        self.db.add(car)
        self.db.commit()
        return CarSchema(
            brand_name=car.brand.name, model_name=car.model.name, power=car.power
        )
