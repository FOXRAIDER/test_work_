from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from .logger import logger
from requests import ConnectTimeout


class LoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware которая логирует все запросы
    """

    async def dispatch(self, request, call_next: RequestResponseEndpoint):
        logger.info(f"Request: {request.method} {request.url}")
        try:
            response = await call_next(request)
            logger.info(f"Response: {response.status_code}")
            return response
        except ConnectTimeout:
            pass
        except Exception as e:
            logger.exception(e)
