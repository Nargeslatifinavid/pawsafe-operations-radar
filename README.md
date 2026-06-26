# PawSafe Operations Radar

A multi-agent AI system for dog-walking and pet-care businesses in Southern California.
Assesses outdoor safety by combining weather, air quality, and dog breed risk profiles.

**Built for:** Kaggle 5-Day AI Agents Intensive Capstone (June 2026)  
**Stack:** Google ADK · Gemini 2.5 Flash · Open-Meteo API · Cloud Run

## Architecture
Coordinator Agent → [Weather Agent + AQI Agent + Dog Risk Agent] → Risk Composer → Message Agent → QC Guardrail

## Status
- [x] Day 1: Single agent scaffold with stub weather tool
- [ ] Day 2: Real APIs + multi-agent
- [ ] Day 3: Risk composer + evaluation  
- [ ] Day 4: Deploy to Cloud Run
- [ ] Day 5: Submit

## Run locally
```bash
pip install google-adk python-dotenv
echo "GOOGLE_API_KEY=your_key" > .env
adk run pawsafe_root
```
