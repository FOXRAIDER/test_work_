FROM python:3.11

WORKDIR /app

COPY ./ ./
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000