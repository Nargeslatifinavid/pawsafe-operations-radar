# 🐾 PawSafe Operations Radar

**A multi-agent AI system that generates daily outdoor safety briefings for dog-walking and pet-care businesses in Southern California.**

Combines real-time weather data, air quality index (AQI), and dog breed-specific risk profiles to produce actionable operational guidance — not just "what's the weather," but "what should staff do outdoors today?"

> Built for the [Kaggle 5-Day AI Agents Intensive Vibe Coding Course](https://www.kaggle.com/competitions/5-day-ai-agents-intensive-vibecoding-course-with-google) capstone project (June 2026).

---

## Problem

Pet-care businesses in Southern California face a recurring operational challenge: heat, poor air quality, and wildfire smoke create unsafe conditions for dogs, but there is no tool that translates raw weather data into **staff-ready operational decisions**. Existing consumer apps answer "is it okay to walk my dog now?" — but businesses need "what should my team do today, and how do we explain it to clients?"

## Solution

PawSafe Operations Radar uses a **multi-agent architecture** where specialized AI agents each handle one data domain, then a composer agent synthesizes everything into a unified safety briefing. A QC guardrail agent validates the output before delivery, blocking unsafe language like "guaranteed safe" or medical claims.

---

## Architecture

```
User Query (location + dog breed + age)
        │
        ▼
┌─────────────────────┐
│  Coordinator Agent   │   Receives query, delegates to specialists
│  (pawsafe_root)      │
└─────────┬───────────┘
          │
          ├──► Weather Agent ──────► get_weather() ──► Open-Meteo API
          │    (weather_agent)        temperature, humidity, wind, UV
          │
          ├──► AQI Agent ─────────► get_air_quality() ──► Open-Meteo AQI API
          │    (aqi_agent)            PM2.5, PM10, ozone, AQI index
          │
          └──► Dog Risk Agent ────► get_dog_risk_profile() ──► Python calculator
               (dog_risk_agent)      breed, age, brachycephalic flags
                    │
                    ▼
┌─────────────────────┐
│  Risk Composer Agent │   Synthesizes all data into unified risk assessment
│  (risk_composer_agent)│
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  QC Guardrail Agent  │   Validates output — blocks "safe/guaranteed",
│  (qc_guardrail_agent)│   medical claims, stale data
└─────────────────────┘
          │
          ▼
    Final Safety Briefing
```

> **Note on the demo:** Due to free-tier quota limits (5 requests/min), the live demo consolidates tools into the coordinator to show complete end-to-end output. The full 6-agent architecture above is the intended production design and is fully implemented in this repository.

---

## Key Features

- **Real-time weather data** via Open-Meteo API (no API key required)
- **Air quality monitoring** with PM2.5, PM10, and ozone levels
- **Breed-aware risk scoring** — brachycephalic, senior, and puppy dogs get higher risk ratings
- **Multi-agent coordination** — each agent is a specialist; the coordinator orchestrates them
- **QC guardrail** — blocks absolute safety claims and veterinary overreach
- **Structured safety briefings** — risk level, recommended walk windows, breed-specific cautions

---

## Example Output

**Input:**
```
Is it safe to walk a 3-year-old Labrador in Pasadena? latitude 34.14, longitude -118.14
```

**Output:**
```
RISK LEVEL: MODERATE
ASSESSMENT: The current temperature of 81.3°F and a Moderate Air Quality Index
(AQI 56) present environmental considerations for a walk. While a 3-year-old
Labrador typically has a low individual risk profile, the slightly elevated PM2.5
levels indicate that sensitive individuals, including some dogs, might experience
minor respiratory effects.
RECOMMENDATION: PROCEED WITH CAUTION
TIMING: Early morning or late evening hours when temperatures are lower and air
quality may be more favorable.
SPECIAL INSTRUCTIONS: For a Labrador, ensure consistent access to fresh water
and monitor closely for any signs of discomfort or heat stress.
Disclaimer: This is operational guidance, not veterinary advice.
```

---

## Tech Stack

| Component | Technology |
|---|---|
| Agent Framework | [Google ADK](https://google.github.io/adk-docs/) (Agent Development Kit) |
| LLM | Gemini 2.5 Flash via Google AI Studio |
| Weather API | [Open-Meteo](https://open-meteo.com/) (free, no key required) |
| AQI API | [Open-Meteo Air Quality](https://open-meteo.com/en/docs/air-quality-api) |
| Risk Calculator | Pure Python — no LLM call, saves quota |
| Language | Python 3.11+ |

---

## Project Structure

```
pawsafe-operations-radar/
│
├── pawsafe_root/                    # ADK agent package (entry point)
│   ├── agent.py                     # Root coordinator agent + orchestration logic
│   ├── __init__.py                  # Exports root_agent for ADK
│   │
│   ├── weather_agent/
│   │   ├── agent.py                 # weather_agent + get_weather() tool
│   │   └── __init__.py
│   │
│   ├── aqi_agent/
│   │   ├── agent.py                 # aqi_agent + get_air_quality() tool
│   │   └── __init__.py
│   │
│   ├── dog_risk_agent/
│   │   ├── agent.py                 # dog_risk_agent + get_dog_risk_profile() tool
│   │   └── __init__.py
│   │
│   ├── risk_composer_agent/
│   │   ├── agent.py                 # Synthesizes weather + AQI + dog risk
│   │   └── __init__.py
│   │
│   ├── qc_guardrail_agent/
│   │   ├── agent.py                 # Validates output, blocks unsafe language
│   │   └── __init__.py
│   │
│   └── .adk/
│       └── session.db               # Local session storage (auto-generated)
│
├── test_tools.py                    # Unit tests for individual tools
├── test_structure.py                # Tests for agent structure validation
├── test_quota.py                    # API connectivity and quota tests
├── .env                             # API key — not committed (see .gitignore)
├── .gitignore
└── README.md
```

---

## Prerequisites

- Python 3.11+
- A Google AI Studio API key ([get one free here](https://aistudio.google.com/apikey))
- Miniconda or pip

## Setup & Run

```bash
# 1. Clone the repository
git clone https://github.com/Nargeslatifinavid/pawsafe-operations-radar.git
cd pawsafe-operations-radar

# 2. Install dependencies
pip install google-adk python-dotenv httpx

# 3. Configure API key
echo "GOOGLE_API_KEY=your_key_here" > .env

# 4. Set environment variable (Windows PowerShell)
$env:GOOGLE_API_KEY="your_key_here"

# 5. Run the agent system
adk run pawsafe_root
```

**Example query:**
```
Is it safe to walk a 5-year-old French Bulldog in Pasadena? latitude 34.14, longitude -118.14
```

**Or run the web UI:**
```bash
adk web
# Open http://localhost:8000
```

---

## Course Concepts Applied

This project demonstrates the following concepts from the Kaggle 5-Day AI Agents Intensive Vibe Coding Course:

| Course Concept | How It's Used in PawSafe |
|---|---|
| **Multi-Agent Orchestration** (Day 1-2) | 5 specialized agents with coordinator pattern |
| **Tool / Function Calling** (Day 2) | 3 real tools: get_weather, get_air_quality, get_dog_risk_profile |
| **External API Integration** (Day 2) | Live data from Open-Meteo (weather + air quality, no key needed) |
| **Agent Transfer Pattern** (Day 2) | Coordinator delegates to specialist sub-agents |
| **Guardrails & Output Validation** (Day 4) | QC Agent blocks unsafe claims, medical language, stale data |
| **Google ADK Framework** (Day 1-5) | Entire project built on ADK with LlmAgent |
| **Gemini 2.5 Flash** (Day 1) | Powers all agent reasoning and synthesis |

---

## Development Timeline

| Day | Milestone | Status |
|---|---|---|
| Day 1 (Jun 26) | Single agent scaffold + stub weather tool | ✅ Complete |
| Day 2 (Jun 27) | Real APIs + 3 worker agents + coordinator | ✅ Complete |
| Day 3 (Jun 28) | Risk Composer + QC Guardrail | ✅ Complete |
| Day 4-5 (Jun 29 - Jul 6) | README + video demo + Kaggle Writeup + submission | ✅ Complete |

---

## Disclaimer

PawSafe Operations Radar provides informational, weather-based operational guidance for pet-care businesses. It does not provide veterinary advice and cannot guarantee safety. Risk varies by dog, surface, shade, exertion, hydration, health status, and local conditions. Always check pavement or ground conditions directly, monitor the dog, and use professional judgment.

---

## Author

**Narges Latifinavid**  
MSc Computer Science | AI Engineering  
[GitHub](https://github.com/Nargeslatifinavid) · [Kaggle](https://www.kaggle.com/nargeslatifinavid)

