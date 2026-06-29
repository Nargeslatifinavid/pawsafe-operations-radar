from google.adk.agents import LlmAgent

def get_dog_risk_profile(breed: str, age_years: float) -> dict:
    """Return risk profile for a dog breed and age."""
    high_risk_breeds = [
        "bulldog", "pug", "french bulldog", "boston terrier",
        "shih tzu", "boxer", "pekingese"
    ]
    breed_lower = breed.lower()
    is_brachycephalic = any(b in breed_lower for b in high_risk_breeds)
    is_senior = age_years >= 8
    is_puppy = age_years < 1

    risk_level = "Low"
    warnings = []
    if is_brachycephalic:
        risk_level = "High"
        warnings.append("Brachycephalic breed — very sensitive to heat and air quality.")
    if is_senior:
        risk_level = "High" if risk_level == "Low" else risk_level
        warnings.append("Senior dog — limit exercise, watch for fatigue.")
    if is_puppy:
        warnings.append("Puppy — paws sensitive to hot pavement.")

    return {
        "breed": breed,
        "age_years": age_years,
        "risk_level": risk_level,
        "is_brachycephalic": is_brachycephalic,
        "is_senior": is_senior,
        "warnings": warnings,
    }

dog_risk_agent = LlmAgent(
    name="dog_risk_agent",
    model="gemini-2.5-flash",
    description="Assesses walk safety risk based on dog breed and age.",
    instruction="Use get_dog_risk_profile to assess risk for the given dog breed and age.",
    tools=[get_dog_risk_profile],
)