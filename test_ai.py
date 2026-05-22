from resume_parser import extract_text_from_pdf

from ml_model import calculate_match_score


# Job Description
job_description = """

Python
SQL
Machine Learning
Streamlit
Data Analysis

"""


# Resume Path
resume_path = "resumes/Resume3.pdf"


# Extract Resume Text
resume_text = extract_text_from_pdf(
    resume_path
)


# Calculate Score
score = calculate_match_score(
    job_description,
    resume_text
)


print("Match Score:", score, "%")