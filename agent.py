import json

def generate_agent_task():
    with open("results.json", "r") as f:
        data = json.load(f)

    top_job = data[0]["job_title"]
    missing = data[0]["missing_skills"]

    return {
        "role": "career_ai_agent",
        "goal": f"Help user become {top_job}",
        "priority_skill": missing[0] if missing else None,
        "tasks": [
            f"Find top learning resources for {missing[0]}",
            f"Find GitHub projects related to {missing[0]}",
            f"Find 1 beginner roadmap"
        ]
    }