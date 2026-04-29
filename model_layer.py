import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from jobs_data import JOBS, SKILL_ONTOLOGY


# -----------------------------
# Vectorization Helper
# -----------------------------
def vectorize(skill_dict):
    """
    Convert user/job skills into fixed-order numpy vector
    based on SKILL_ONTOLOGY.
    """
    return np.array([
        float(skill_dict.get(skill, 0))
        for skill in SKILL_ONTOLOGY
    ]).reshape(1, -1)


# -----------------------------
# Main Career Prediction Engine
# -----------------------------
def predict_careers(user_skills, top_k=3):
    """
    Predict best matching careers for user skills.
    Returns top_k jobs sorted by cosine similarity.
    Also saves results to results.json
    """
    user_vec = vectorize(user_skills)

    results = []

    for job in JOBS:
        job_vec = vectorize(job["required_skills"])

        score = float(cosine_similarity(user_vec, job_vec)[0][0])

        missing_skills = []

        for skill, weight in job["required_skills"].items():
            user_level = float(user_skills.get(skill, 0))

            # Missing only important skills
            if user_level < 0.4 and weight >= 0.7:
                missing_skills.append(skill)

        results.append({
            "job_title": job["title"],
            "match_score": round(score * 100, 1),
            "missing_skills": missing_skills[:5]
        })

    results.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )

    top_results = results[:top_k]

    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(
            top_results,
            f,
            indent=4,
            ensure_ascii=False
        )

    return top_results


# -----------------------------
# Radar Chart Skill Categories
# -----------------------------
def skill_categories(user_skills):
    """
    Aggregate user skills into radar-chart categories.
    """
    categories = {
        "Design Tools": [
            "figma",
            "sketch",
            "adobe_xd",
            "photoshop",
            "illustrator",
            "after_effects"
        ],

        "UX Research": [
            "user_research",
            "wireframing",
            "prototyping",
            "usability_testing",
            "information_architecture"
        ],

        "Visual Craft": [
            "typography",
            "color_theory",
            "branding",
            "illustration",
            "layout"
        ],

        "Product Thinking": [
            "product_strategy",
            "user_flows",
            "data_analysis",
            "ab_testing",
            "stakeholder_mgmt"
        ],

        "Mobile & Web": [
            "ios_guidelines",
            "material_design",
            "responsive_design",
            "mobile_patterns",
            "html_css"
        ],

        "3D / Spatial": [
            "blender",
            "unity",
            "unreal_engine",
            "3d_modeling",
            "spatial_design",
            "vr_prototyping"
        ],

        "Soft Skills": [
            "communication",
            "teamwork",
            "presentation",
            "critical_thinking"
        ]
    }

    output = []

    for category, skills in categories.items():
        values = [
            float(user_skills.get(skill, 0))
            for skill in skills
        ]

        avg = (sum(values) / len(values)) * 100 if values else 0

        output.append({
            "category": category,
            "value": round(avg, 1)
        })

    return output