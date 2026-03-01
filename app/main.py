from fastapi import FastAPI
from app.endpoints import router as weather_router

app = FastAPI(title="Weather GRIB API")

app.include_router(weather_router)