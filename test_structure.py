# test_structure.py
import sys
sys.path.insert(0, '.')

try:
    from pawsafe_root.agent import (
        root_agent, 
        weather_agent, 
        aqi_agent, 
        dog_risk_agent,
        risk_composer_agent,
        qc_guardrail_agent
    )
    print("✅ All agents imported successfully")
    print(f"✅ root_agent name: {root_agent.name}")
    print(f"✅ sub_agents count: {len(root_agent.sub_agents)}")
    for agent in root_agent.sub_agents:
        print(f"   - {agent.name}")
except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")