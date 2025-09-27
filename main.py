from fastapi import FastAPI, HTTPException
from services.weather_service import get_weather_data

app = FastAPI(title="Weather API", version="1.1.0")

# Catálogo de lugares predefinidos
LOCATIONS = {
    "suchiapa": {"lat": 16.6264, "lon": -93.1000},
    "tuxtla": {"lat": 16.7597, "lon": -93.1131},
    "ocozocoautla": {"lat": 16.7640, "lon": -93.3719},
    "apicpac": {"lat": 16.6125, "lon": -93.2833}  # Embarcadero Apicpac
}


@app.get("/weather/{location}")
async def weather(location: str):
    """
    Devuelve el clima actual, pronóstico por horas y por días de una localidad.
    Parámetro:
    - location: Nombre corto del lugar (suchiapa, tuxtla, ocozocoautla, apicpac).
    """
    loc = LOCATIONS.get(location.lower())
    if not loc:
        raise HTTPException(status_code=404, detail="Localidad no soportada")

    return await get_weather_data(loc["lat"], loc["lon"])
