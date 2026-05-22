from resume_parser import extract_text_from_pdf


resume_path = "resumes/Resume3.pdf"

text = extract_text_from_pdf(resume_path)

print(text)