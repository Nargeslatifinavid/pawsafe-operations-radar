# test_tools.py
import sys, asyncio
sys.path.insert(0, '.')

from pawsafe_root.weather_agent.agent import get_weather
from pawsafe_root.aqi_agent.agent import get_air_quality
from pawsafe_root.dog_risk_agent.agent import get_dog_risk_profile

async def test_all():
    print("=== Weather Tool Test ===")
    weather = get_weather(latitude=34.14, longitude=-118.14)
 
    print(weather)
    
    print("\n=== AQI Tool Test ===")
    aqi = get_air_quality(latitude=34.14, longitude=-118.14)      
    print(aqi)
    
    print("\n=== Dog Risk Tool Test ===")
    risk = get_dog_risk_profile("Bulldog",14)
    print(risk)

asyncio.run(test_all())