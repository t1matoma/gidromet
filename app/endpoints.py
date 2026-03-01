from fastapi import APIRouter, Query
from fastapi.responses import Response

from app.grib_service import load_grib_data
from app.plot_utils import plot_to_png
from app.settings import TEMPERATURE_FILE, PRESSURE_FILE


router = APIRouter()

@router.get("/temperature")
def get_temperature(time: str = Query(..., description="ISO формат времени, например 2026-01-30T00:00")):
    data, lats, lons = load_grib_data(TEMPERATURE_FILE, time)
    png_bytes = plot_to_png(data, lats, lons, f"Температура {time}")
    return Response(content=png_bytes, media_type="image/png")

@router.get("/pressure")
def get_pressure(time: str = Query(..., description="ISO формат времени, например 2026-01-30T00:00")):
    data, lats, lons = load_grib_data(PRESSURE_FILE, time)
    png_bytes = plot_to_png(data, lats, lons, f"Давление {time}")
    return Response(content=png_bytes, media_type="image/png")