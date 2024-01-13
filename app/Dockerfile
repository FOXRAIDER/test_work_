FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /app
COPY ./alembic /app/alembic
COPY ./alembic.ini /app

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY /app /app

CMD uvicorn main:app --host 0.0.0.0 --port 8000