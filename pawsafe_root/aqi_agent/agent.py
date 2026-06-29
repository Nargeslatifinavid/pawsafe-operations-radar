import httpx
from google.adk.agents import LlmAgent

def get_air_quality(latitude: float, longitude: float) -> dict:
    """Fetch air quality data from Open-Meteo AQI API."""
    url = (
        f"https://air-quality-api.open-meteo.com/v1/air-quality"
        f"?latitude={latitude}&longitude={longitude}"
        f"&current=us_aqi,pm2_5,pm10"
    )
    try:
        r = httpx.get(url, timeout=10)
        r.raise_for_status()
        c = r.json().get("current", {})
        aqi = c.get("us_aqi", 0)
        if aqi <= 50: category = "Good"
        elif aqi <= 100: category = "Moderate"
        elif aqi <= 150: category = "Unhealthy for Sensitive Groups"
        elif aqi <= 200: category = "Unhealthy"
        elif aqi <= 300: category = "Very Unhealthy"
        else: category = "Hazardous"
        return {
            "aqi_value": aqi,
            "pm25": c.get("pm2_5"),
            "pm10": c.get("pm10"),
            "aqi_category": category,
        }
    except Exception as e:
        return {"error": str(e)}

aqi_agent = LlmAgent(
    name="aqi_agent",
    model="gemini-2.5-flash",
    description="Provides current air quality index for a latitude/longitude location.",
    instruction="Use get_air_quality to fetch AQI, PM2.5, PM10, and air quality category.",
    tools=[get_air_quality],
)