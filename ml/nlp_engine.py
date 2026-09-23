SKILL_ALIASES = {

    "python": [
        "python",
        "python3"
    ],

    "sql": [
        "sql",
        "mysql",
        "postgresql",
        "postgres"
    ],

    "java": [
        "java"
    ],

    "javascript": [
        "javascript",
        "js"
    ],

    "html": [
        "html",
        "html5"
    ],

    "css": [
        "css",
        "css3"
    ],

    "react": [
        "react",
        "reactjs",
        "react.js"
    ],

    "node.js": [
        "node.js",
        "nodejs",
        "node js"
    ],

    "fastapi": [
        "fastapi",
        "fast api"
    ],

    "flask": [
        "flask"
    ],

    "docker": [
        "docker",
        "docker container",
        "docker containers"
    ],

    "aws": [
        "aws",
        "amazon web services"
    ],

    "machine learning": [
        "machine learning",
        "machine-learning",
        "machinelearning",
        "ml"
    ],

    "deep learning": [
        "deep learning",
        "deep-learning",
        "deeplearning",
        "dl"
    ],

    "nlp": [
        "nlp",
        "natural language processing"
    ],

    "scikit-learn": [
        "scikit-learn",
        "sklearn",
        "scikit learn"
    ]
}


def extract_skills(text):
    """
    Extract known skills from a piece of text.
    Different names/aliases are mapped to one standard skill.
    """

    text = text.lower()

    found_skills = []

    for skill, aliases in SKILL_ALIASES.items():

        for alias in aliases:

            if alias in text:
                found_skills.append(skill)
                break

    return found_skills


def analyze_resume(resume, job_description):
    """
    Compare resume skills with job description skills.
    """

    resume_skills = extract_skills(resume)

    job_skills = extract_skills(job_description)

    matched_skills = list(
        set(resume_skills) & set(job_skills)
    )

    missing_skills = list(
        set(job_skills) - set(resume_skills)
    )

    if len(job_skills) == 0:
        match_score = 0

    else:
        match_score = round(
            len(matched_skills) / len(job_skills) * 100
        )

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_score": match_score
    }