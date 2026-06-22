import streamlit as st
import os

from database import get_connection
from resume_parser import extract_text_from_pdf
from ml_model import calculate_match_score
from skill_extractor import extract_skills
from candidate_extractor import extract_candidate_details

st.title("Upload Candidate Resume")

job_description = st.text_area(
    "Job Description"
)

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if st.button("Submit Candidate"):

    if uploaded_file is not None:

        os.makedirs("resumes", exist_ok=True)

        save_path = os.path.join(
            "resumes",
            uploaded_file.name
        )

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Extract resume text
        resume_text = extract_text_from_pdf(
            save_path
        )

        # Extract candidate details
        candidate = extract_candidate_details(
            resume_text
        )

        name = candidate["name"]
        email = candidate["email"]
        phone = candidate["phone"]

        # Extract skills
        extracted_skills = extract_skills(
            resume_text
        )

        skills_string = ", ".join(
            extracted_skills
        )

        # Calculate AI score
        match_score = float(
            calculate_match_score(
                job_description,
                resume_text
            )
        )

        # Show extracted information
        st.subheader("Extracted Details")

        st.write("Name:", name)
        st.write("Email:", email)
        st.write("Phone:", phone)
        st.write("Skills:", skills_string)

        # Save to database
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO candidates
        (
            name,
            email,
            phone,
            skills,
            resume_path,
            status,
            match_score,
            extracted_skills
        )
        VALUES (?,?,?,?,?,?,?,?)
        """

        values = (
            name,
            email,
            phone,
            skills_string,
            save_path,
            "Applied",
            match_score,
            skills_string
        )

        cursor.execute(query, values)

        conn.commit()
        conn.close()

        st.success(
            "Candidate Added Successfully"
        )

        st.write(
            "AI Match Score:",
            match_score,
            "%"
        )

    else:

        st.error(
            "Please upload a resume"
        )