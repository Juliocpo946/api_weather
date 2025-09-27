# Weather API - FastAPI

API de clima para **lugares específicos en Chiapas, México**:  
- Suchiapa  
- Tuxtla Gutiérrez  
- Ocozocoautla  
- Embarcadero Apicpac  

Los datos se obtienen de [Open-Meteo](https://open-meteo.com/).  
La API devuelve el **clima actual**, **pronóstico por horas** y **pronóstico por días** en un JSON simple.

---

## Endpoints

### Clima por localidad
```

GET /weather/{location}

```

### Ejemplos
```

/weather/suchiapa
/weather/tuxtla
/weather/ocozocoautla
/weather/apicpac

````

---

### Ejemplo de respuesta
```json
{
  "current": {
    "temperature": 28,
    "condition": "despejado",
    "last_updated": "2025-09-26T22:55:00Z"
  },
  "forecast": {
    "hourly": [
      {
        "time": "23:00",
        "temperature": 26,
        "condition": "despejado"
      }
    ],
    "daily": [
      {
        "day": "Sábado",
        "temp_max": 30,
        "temp_min": 22,
        "condition": "despejado"
      }
    ]
  }
}
````

---

## Despliegue en Render

Despliégalo fácilmente con un solo clic:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/tu-usuario/weather-api)

### Configuración en Render

* **Runtime:** Python
* **Build Command:**

  ```bash
  pip install -r requirements.txt
  ```
* **Start Command:**

  ```bash
  uvicorn main:app --host 0.0.0.0 --port $PORT
  ```

---

## Tech Stack

* [FastAPI](https://fastapi.tiangolo.com/)
* [Requests](https://docs.python-requests.org/)
* [Open-Meteo API](https://open-meteo.com/)

---

## Uso en tu App

Solo necesitas hacer un request al endpoint con el nombre del lugar:

```bash
curl https://tu-api.onrender.com/weather/tuxtla
```

Y obtendrás el JSON con:

* `current` → Clima actual
* `forecast.hourly` → Pronóstico por horas
* `forecast.daily` → Pronóstico por días

---

## Notas

* Los nombres de los lugares son **insensibles a mayúsculas/minúsculas**.
* Actualmente soporta únicamente las localidades predefinidas.
* El JSON sigue un formato **fijo**, ideal para apps móviles o web que consumen la API.


