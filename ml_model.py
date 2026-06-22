from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_match_score(
    job_description,
    resume_text
):

    # Convert text into embeddings
    job_embedding = model.encode(job_description)

    resume_embedding = model.encode(resume_text)

    # Compare similarity
    similarity = cosine_similarity(
        [job_embedding],
        [resume_embedding]
    )

    # Convert to percentage
    score = similarity[0][0] * 100

    return round(score, 2)