from google.adk.agents import LlmAgent
from .weather_agent.agent import weather_agent
from .aqi_agent.agent import aqi_agent
from .dog_risk_agent.agent import dog_risk_agent
from .risk_composer_agent.agent import risk_composer_agent
from .qc_guardrail_agent.agent import qc_guardrail_agent

root_agent = LlmAgent(
    name="pawsafe_root",
    model="gemini-2.5-flash",
    description="Orchestrates weather, air quality, and dog-risk for safe walk decisions.",
    instruction=(
    "You are PawSafe, a safety assistant for dog walkers in Southern California. "
    "You MUST follow ALL 5 steps below. Do NOT skip any step.\n\n"
    "IMPORTANT: Before starting, you need latitude and longitude. "
    "If the user gives only a city name, ask them: "
    "'Please provide the latitude and longitude for accurate results. "
    "You can find these at maps.google.com - right-click on your location.'\n\n"
    "STEP 1: Transfer to weather_agent with the latitude and longitude.\n"
    "STEP 2: Transfer to aqi_agent with the same latitude and longitude.\n"
    "STEP 3: Transfer to dog_risk_agent with the dog breed and age.\n"
    "STEP 4: Transfer to risk_composer_agent with ALL results from steps 1, 2, 3.\n"
    "STEP 5: Transfer to qc_guardrail_agent with the output from step 4.\n"
    "STEP 6: Show the FINAL_BRIEFING from qc_guardrail_agent to the user.\n\n"
    "CRITICAL: Complete ALL 6 steps. Never skip any agent. Never guess data."
),
    sub_agents=[
        weather_agent,
        aqi_agent,
        dog_risk_agent,
        risk_composer_agent,
        qc_guardrail_agent,
    ],
)