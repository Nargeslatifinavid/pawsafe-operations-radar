import httpx
from google.adk.agents import LlmAgent

def get_weather(latitude: float, longitude: float) -> dict:
    """Fetch real weather data from Open-Meteo API."""
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m,uv_index"
        f"&temperature_unit=fahrenheit"
    )
    try:
        r = httpx.get(url, timeout=10)
        r.raise_for_status()
        c = r.json().get("current", {})
        wind_kmh = c.get("wind_speed_10m")
        return {
            "temperature_f": c.get("temperature_2m"),
            "humidity_percent": c.get("relative_humidity_2m"),
            "wind_speed_mph": round(wind_kmh * 0.621371, 2) if wind_kmh else None,
            "uv_index": c.get("uv_index"),
        }
    except Exception as e:
        return {"error": str(e)}

weather_agent = LlmAgent(
    name="weather_agent",
    model="gemini-2.5-flash",
    description="Provides current weather for a latitude/longitude location.",
    instruction="Use get_weather to fetch temperature, humidity, wind speed, and UV index.",
    tools=[get_weather],
)