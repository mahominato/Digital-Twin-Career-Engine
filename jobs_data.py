# Полный список всех навыков, которые используются в системе
# Важно: здесь должны быть ВСЕ навыки, которые есть в JOBS и в skill_categories
SKILL_ONTOLOGY = [
    "figma", "sketch", "adobe_xd", "photoshop", "illustrator", "after_effects", # Design Tools
    "user_research", "wireframing", "prototyping", "usability_testing", "information_architecture", # UX Research
    "typography", "color_theory", "branding", "layout", # Visual Craft
    "product_strategy", "user_flows", "data_analysis", "ab_testing", "stakeholder_mgmt", # Product Thinking
    "ios_guidelines", "material_design", "responsive_design", "mobile_patterns", "html_css", # Mobile & Web
    "blender", "unity", "unreal_engine", "3d_modeling", "spatial_design", "vr_prototyping", # 3D / Spatial
    "communication", "teamwork", "presentation", "critical_thinking" # Soft Skills
]

# База данных вакансий
JOBS = [
    {
        "title": "UI/UX Designer",
        "required_skills": {
            "figma": 1.0,
            "wireframing": 1.0,
            "prototyping": 1.0,
            "user_research": 0.8,
            "photoshop": 0.7,
            "communication": 0.7,
            "responsive_design": 0.5
        }
    },
    {
        "title": "Product Designer",
        "required_skills": {
            "figma": 1.0,
            "product_strategy": 1.0,
            "user_research": 0.9,
            "prototyping": 0.8,
            "communication": 0.9,
            "data_analysis": 0.6
        }
    },
    {
        "title": "VR Designer",
        "required_skills": {
            "blender": 1.0,
            "unity": 1.0,
            "prototyping": 0.7,
            "communication": 0.6,
            "spatial_design": 0.8,
            "vr_prototyping": 0.9
        }
    }
]