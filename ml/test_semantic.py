from semantic_engine import calculate_semantic_similarity


resume = """
I developed machine learning models using Python and scikit-learn.
I worked on data preprocessing and predictive analytics.
"""


job_description = """
We are looking for a candidate with experience in
machine learning, Python and predictive modeling.
"""


score = calculate_semantic_similarity(
    resume,
    job_description
)


print("Semantic Similarity Score:", score)