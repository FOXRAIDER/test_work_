from fastapi import FastAPI
import uvicorn
from app.utils.middleware import LoggingMiddleware
from app.shop.routers import router as shop_router


app = FastAPI(title="Test Work", description="API for test work", version="0.0.1")
app.add_middleware(LoggingMiddleware)
app.include_router(shop_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1111)
