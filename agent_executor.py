import json

def generate_agent_prompt():
    # 1. Загружаем данные из вашего ML-анализа
    with open('results.json', 'r') as f:
        data = json.load(f)
    
    # Берем самый приоритетный навык (из первой вакансии)
    top_job = data[0]['job_title']
    missing_skill = data[0]['missing_skills'][0]
    
    # 2. Формируем "System Prompt Injection"
    prompt = f"""
    SYSTEM ROLE: Career Development Assistant.
    TASK: User needs to learn '{missing_skill}' to bridge the gap for a '{top_job}' role.
    
    INSTRUCTIONS:
    1. Execute a web search for the most current, high-quality learning resources for '{missing_skill}'.
    2. Look specifically for:
       - Trending GitHub repositories or open-source projects.
       - Upcoming hackathons or community events.
       - Official documentation or highly-rated interactive courses.
    3. Parse the results and summarize the top 3 actionable resources with direct links.
    """
    return prompt

if __name__ == "__main__":
    print("--- КОПИРУЙТЕ ЭТОТ ПРОМПТ В AGENT CHAT ---")
    print(generate_agent_prompt())