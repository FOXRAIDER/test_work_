
# Project Title

A brief description of what this project does and who it's for

Тестовое задание

## Usage/Examples
Поднять все контейнеры командой:
```docker
docker compose up --build -d
```


## API Reference

#### Add start data
Добавить стартовые данные

```http
  GET /items/add_start_data
```


#### Get brands
Получить все бренды

```http
  GET /items/brands
```
#### Get models
Получить все модели

```http
  GET /items/models
```

#### Get car
Получить все машины

```http
  GET /items/cars
```

#### Get car by id
Получить все машины по id 

```http
  GET /items/cars_by_id?id=4
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of item to fetch |


#### Update car by id
Обновить машину по id 

```http
  PUT /items/cars_by_id?id=4
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of item to fetch |
| `brand_name `      | `string` | **Required**. Brand name of item to fetch |
| `model_name `      | `string` | **Required**. Model name of item to fetch |
| `power `      | `string` | **Required**. Power of item to fetch |

#### Add car
Добавить машину, модель и бренд 

```http
  POST /items/add_car
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `brand_name `      | `string` | **Required**. Brand name of item to fetch |
| `model_name `      | `string` | **Required**. Model name of item to fetch |
| `power `      | `string` | **Required**. Power of item to fetch |

#### Delete car by id
Удалить все машины по id 

```http
  DELETE /items/cars_by_id?id=4
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of item to fetch |




