import re


# --------------------------------------------------
# Skills and their common variations
# --------------------------------------------------

SKILL_ALIASES = {
    "python": ["python"],
    "sql": ["sql", "mysql", "postgresql", "postgres"],
    "java": ["java"],
    "javascript": ["javascript", "js"],
    "typescript": ["typescript", "ts"],
    "html": ["html"],
    "css": ["css"],
    "react": ["react", "react.js"],
    "node.js": ["node.js", "nodejs", "node js"],
    "express": ["express", "express.js"],
    "fastapi": ["fastapi"],
    "flask": ["flask"],
    "spring boot": ["spring boot"],
    "docker": ["docker"],
    "kubernetes": ["kubernetes", "k8s"],
    "aws": ["aws", "amazon web services"],
    "azure": ["azure", "microsoft azure"],
    "git": ["git"],
    "github": ["github"],
    "rest api": ["rest api", "restful api", "rest apis"],
    "machine learning": ["machine learning", "ml"],
    "deep learning": ["deep learning", "dl"],
    "nlp": ["nlp", "natural language processing"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "scikit-learn": ["scikit-learn", "sklearn"],
    "tensorflow": ["tensorflow"],
    "pytorch": ["pytorch"],
    "selenium": ["selenium"],
    "pytest": ["pytest"],
    "jenkins": ["jenkins"],
    "power bi": ["power bi"],
    "excel": ["excel"],
    "mongodb": ["mongodb", "mongo db"],
    "c++": ["c++"],
    "c": ["c programming"],
    "oops": ["oops", "object oriented programming"],
}


# --------------------------------------------------
# Extract skills from text
# --------------------------------------------------

def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill, aliases in SKILL_ALIASES.items():

        for alias in aliases:

            # Escape special characters such as + and .
            pattern = r"(?<!\w)" + re.escape(alias.lower()) + r"(?!\w)"

            if re.search(pattern, text):
                found_skills.append(skill)
                break

    return found_skills


# --------------------------------------------------
# Analyze resume against job description
# --------------------------------------------------

def analyze_resume(resume, job_description):

    resume_skills = extract_skills(resume)

    job_skills = extract_skills(job_description)

    matched_skills = sorted(
        set(resume_skills) & set(job_skills)
    )

    missing_skills = sorted(
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