import requests
from datetime import datetime


async def get_weather_data(lat: float, lon: float):
    # API externa: Open-Meteo
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&hourly=temperature_2m,weathercode"
        f"&daily=temperature_2m_max,temperature_2m_min,weathercode"
        f"&current_weather=true&timezone=auto"
    )
    response = requests.get(url)
    data = response.json()

    # Mapear condiciones
    def map_condition(code: int) -> str:
        conditions = {
            0: "despejado",
            1: "principalmente despejado",
            2: "parcialmente nublado",
            3: "nublado",
            45: "neblina",
            48: "niebla",
            51: "lluvia ligera",
            61: "lluvia moderada",
            80: "chubascos",
            95: "tormenta eléctrica"
        }
        return conditions.get(code, "desconocido")

    # Clima actual
    current = {
        "temperature": data["current_weather"]["temperature"],
        "condition": map_condition(data["current_weather"]["weathercode"]),
        "last_updated": datetime.utcnow().isoformat() + "Z",
    }

    # Pronóstico por horas (solo primeras 24h)
    hourly = []
    for t, temp, code in zip(
        data["hourly"]["time"], data["hourly"]["temperature_2m"], data["hourly"]["weathercode"]
    ):
        hourly.append({
            "time": t[-5:],  # HH:MM
            "temperature": temp,
            "condition": map_condition(code),
        })

    # Pronóstico diario
    daily = []
    for day, tmax, tmin, code in zip(
        data["daily"]["time"], data["daily"]["temperature_2m_max"],
        data["daily"]["temperature_2m_min"], data["daily"]["weathercode"]
    ):
        daily.append({
            "day": datetime.fromisoformat(day).strftime("%A"),
            "temp_max": tmax,
            "temp_min": tmin,
            "condition": map_condition(code),
        })

    return {
        "current": current,
        "forecast": {
            "hourly": hourly,
            "daily": daily,
        },
    }
