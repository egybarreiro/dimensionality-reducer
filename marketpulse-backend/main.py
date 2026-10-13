from fastapi import FastAPI

from routers.model_router import router as model_router
from routers.ticker_router import router as ticker_router
from routers.data_router import router as data_router

app = FastAPI()

app.include_router(model_router, prefix="/model")
app.include_router(ticker_router, prefix="/ticker")
app.include_router(data_router, prefix="/data")
