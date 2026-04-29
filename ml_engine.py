import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from jobs_data import JOBS, SKILL_ONTOLOGY


def vectorize(skills_dict):
    return np.array([
        float(skills_dict.get(skill, 0.0))
        for skill in SKILL_ONTOLOGY
    ]).reshape(1, -1)


def build_job_vector(job):
    return vectorize(job["required_skills"])


def predict_careers(user_skills, top_k=3):
    user_vec = vectorize(user_skills)

    results = []

    for job in JOBS:
        job_vec = build_job_vector(job)

        score = cosine_similarity(user_vec, job_vec)[0][0]

        missing = []
        for skill, weight in job["required_skills"].items():
            if user_skills.get(skill, 0) < weight:
                missing.append(skill)

        results.append({
            "job_title": job["title"],
            "match_score": round(score * 100, 2),
            "missing_skills": missing[:5]
        })

    results.sort(key=lambda x: x["match_score"], reverse=True)
    top_results = results[:top_k]

    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(top_results, f, indent=4, ensure_ascii=False)

    return top_results