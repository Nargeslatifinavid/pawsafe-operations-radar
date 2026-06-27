from google.adk.agents import LlmAgent
from .weather_agent.agent import weather_agent
from .aqi_agent.agent import aqi_agent
from .dog_risk_agent.agent import dog_risk_agent

root_agent = LlmAgent(
    name="pawsafe_root",
    model="gemini-2.0-flash-lite",
    description="Orchestrates weather, air quality, and dog-risk for safe walk decisions.",
    instruction=(
        "You are PawSafe, an assistant for dog walkers in Southern California. "
        "When asked about walk safety for a dog: "
        "1) Transfer to weather_agent to get current weather. "
        "2) Transfer to aqi_agent to get air quality. "
        "3) Transfer to dog_risk_agent to assess the dog breed and age. "
        "4) After receiving all results, combine them into a friendly 3-4 sentence safety recommendation. "
        "Never call tools directly. Always delegate to the appropriate sub-agent."
    ),
    sub_agents=[weather_agent, aqi_agent, dog_risk_agent],
)