from similarity_engine import calculate_text_similarity


resume = """
I am a software developer with experience in Python,
SQL, machine learning and data analysis.
"""


job_description = """
We are looking for a software engineer with Python,
SQL, machine learning and Docker experience.
"""


score = calculate_text_similarity(
    resume,
    job_description
)

print("Similarity Score:", score)