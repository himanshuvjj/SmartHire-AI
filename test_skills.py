from resume_parser import extract_text_from_pdf

from skill_extractor import extract_skills


resume_path = "resumes/Resume3.pdf"


# Extract Resume Text
resume_text = extract_text_from_pdf(
    resume_path
)


# Extract Skills
skills = extract_skills(
    resume_text
)


print(skills)