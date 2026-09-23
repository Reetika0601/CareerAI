resume = """
I am a computer science student.
I know Python, SQL, HTML, CSS and machine learning.
I have built a student performance prediction project.
"""

job_description = """
We are looking for a software engineer with Python,
SQL, machine learning and Docker experience.
"""

resume = resume.lower()
job_description = job_description.lower()

print("RESUME:")
print(resume)

print("JOB DESCRIPTION:")
print(job_description)

skills = [
    "python",
    "sql",
    "java",
    "javascript",
    "html",
    "css",
    "react",
    "node.js",
    "fastapi",
    "flask",
    "docker",
    "aws",
    "machine learning",
    "deep learning",
    "nlp"
] 
resume_skills = []

for skill in skills:
    if skill in resume:
        resume_skills.append(skill)
job_skills = []

for skill in skills:
    if skill in job_description:
        job_skills.append(skill)

print("\nRESUME SKILLS:")
print(resume_skills)

print("\nJOB SKILLS:")
print(job_skills)
