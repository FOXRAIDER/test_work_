import os

from loguru import logger

# Установка пути к файлу логов
log_file = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "logs", "app-error.txt"
)
os.makedirs(os.path.dirname(log_file), exist_ok=True)

common_log = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "logs", "common-logs.txt"
)
os.makedirs(os.path.dirname(log_file), exist_ok=True)

logger.add(
    log_file,
    format="{time} {level} {level} {message}",
    level="ERROR",
    compression="zip",
    rotation="5 days",
    encoding="utf-8",
)

logger.add(
    common_log,
    format="{time} {level}  {message}",
    level="INFO",
    compression="zip",
    rotation="5 days",
    encoding="utf-8",
)
