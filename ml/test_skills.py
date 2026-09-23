from nlp_engine import extract_skills


text = """
I have experience with Python, SQL, ML,
machine-learning, ReactJS, NodeJS,
and sklearn.
"""


skills = extract_skills(text)

print("Detected Skills:")
print(skills)