def extract_skills(resume_text):

    # Predefined Skills
    skills_list = [

        "Python",
        "Java",
        "C++",
        "SQL",
        "MySQL",
        "Machine Learning",
        "Deep Learning",
        "Data Analysis",
        "Pandas",
        "NumPy",
        "Streamlit",
        "Flask",
        "Django",
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js",
        "Git",
        "GitHub"

    ]


    extracted_skills = []


    # Convert Resume Text to Lowercase
    resume_text = resume_text.lower()


    # Match Skills
    for skill in skills_list:

        if skill.lower() in resume_text:

            extracted_skills.append(skill)


    return extracted_skills