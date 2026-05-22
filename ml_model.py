from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity


def calculate_match_score(
    job_description,
    resume_text
):

    documents = [
        job_description,
        resume_text
    ]


    # Convert text into vectors
    tfidf = TfidfVectorizer()

    tfidf_matrix = tfidf.fit_transform(documents)


    # Compare similarity
    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )


    # Convert into percentage
    score = similarity[0][0] * 100

    return round(score, 2)