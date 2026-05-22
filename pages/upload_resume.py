import streamlit as st
import os

from database import get_connection
from resume_parser import extract_text_from_pdf
from ml_model import calculate_match_score
from skill_extractor import extract_skills


st.title("Upload Candidate Resume")


# Candidate Details
name = st.text_input("Candidate Name")

email = st.text_input("Email")

phone = st.text_input("Phone")

skills = st.text_area("Skills")

job_description = st.text_area(
    "Job Description"
)


# Upload Resume
uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)


# Submit Button
if st.button("Submit Candidate"):

    if uploaded_file is not None:

        # Create file path
        save_path = os.path.join(
            "resumes",
            uploaded_file.name
        )

        # Save PDF file
        with open(save_path, "wb") as f:

            f.write(
                uploaded_file.getbuffer()
            )
        

        # Extract Resume Text
        resume_text = extract_text_from_pdf(
            save_path
        )
        # Extract Skills
        extracted_skills = extract_skills(
        resume_text
        )

        # Convert List to String
        skills_string = ", ".join(
             extracted_skills
              )

        # Calculate Match Score
        match_score = calculate_match_score(
            job_description,
            resume_text
        )

        # Database Connection
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
            skills,
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
        st.write(
    "Extracted Skills:",
    skills_string
)

    else:

        st.error("Please Upload Resume")