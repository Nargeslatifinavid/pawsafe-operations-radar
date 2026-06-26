"""PawSafe root agent — Day 1 scaffold.

A single-agent that uses one stub tool () so we can verify
the ADK plumbing end-to-end before adding real APIs tomorrow.
"""

from google.adk.agents import LlmAgent


def get_weather(zip_code: str) -> dict:
    """Return today's weather forecast for a US zip code.

    This is a STUB implementation for Day 1. On Day 2 we will replace
    the body with a real Open-Meteo API call. The agent does not need
    to know the body changed — only the signature and docstring matter
    to Gemini for tool selection.

    Args:
        zip_code: 5-digit US zip code, e.g. "90092".

    Returns:
        A dict with keys: zip_code, temperature_f, condition, humidity.
    """
    # Day 1 stub data — replace on Day 2
    return {
        "zip_code": zip_code,
        "temperature_f": 78,
        "condition": "Sunny",
        "humidity": 0.42,
    }


root_agent = LlmAgent(
    name="pawsafe_root",
    model="gemini-2.5-flash",
    description="Helps pet-care businesses decide when it is safe to walk dogs.",
    instruction=(
        "You are PawSafe, an assistant for dog walkers and pet daycares in "
        "Southern California. When the user gives you a zip code, call the "
        "get_weather tool and use its result to give a short, friendly "
        "recommendation (2-3 sentences) about whether it is safe to walk "
        "dogs right now. If the temperature is above 85F, warn about hot "
        "pavement. Always be brief."
    ),
    tools=[get_weather],
)

