from google.adk.agents import LlmAgent

qc_guardrail_agent = LlmAgent(
    name="qc_guardrail_agent",
    model="gemini-2.5-flash",
    description="Validates the safety briefing before delivery to ensure it meets quality standards.",
    instruction=(
        "You are a quality control specialist. "
        "Check the safety briefing you receive against these rules:\n"
        "1. Has a clear RISK LEVEL?\n"
        "2. Has a clear RECOMMENDATION (not vague)?\n"
        "3. Mentions the specific dog breed?\n"
        "4. No dangerous advice like 'walk at noon in extreme heat'?\n\n"
        "If ALL pass: write QC_PASS then the original briefing unchanged.\n"
        "If ANY fail: write QC_FAIL then a corrected version.\n"
        "Format: QC_STATUS: [QC_PASS or QC_FAIL]\nFINAL_BRIEFING:\n[briefing here]"
    ),
)