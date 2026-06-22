import streamlit as st
import os

from database import get_connection
from resume_parser import extract_text_from_pdf
from ml_model import calculate_match_score
from skill_extractor import extract_skills
from candidate_extractor import extract_candidate_details

st.title("Upload Candidate Resume")

job_title = st.text_input(
    "Job Title"
)

job_description = st.text_area(
    "Job Description"
)

uploaded_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Submit Candidate"):

    if uploaded_files:

        os.makedirs("resumes", exist_ok=True)

        conn = get_connection()
        st.write("Database opened")
        cursor = conn.cursor()

        progress_bar = st.progress(0)

        for index, uploaded_file in enumerate(uploaded_files):

         save_path = os.path.join(
        "resumes",
        uploaded_file.name
        )

        with open(save_path, "wb") as f:
         f.write(uploaded_file.getbuffer())

        resume_text = extract_text_from_pdf(
        save_path
        )

        candidate = extract_candidate_details(
        resume_text
        )

        name = candidate["name"]
        email = candidate["email"]
        phone = candidate["phone"]

        extracted_skills = extract_skills(
        resume_text
        )

        skills_string = ", ".join(
        extracted_skills
        )

        match_score = float(
        calculate_match_score(
            job_description,
            resume_text
        )
      )

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
        extracted_skills,
        job_title
         )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
        name,
        email,
        phone,
        skills_string,
        save_path,
        "Applied",
        match_score,
        skills_string,
        job_title
        )

        cursor.execute(query, values)

   

    st.success(
        f"Processed: {uploaded_file.name}"
    )

    

    st.write(
        f"Match Score: {round(match_score, 2)}%"
    )

    progress = (index + 1) / len(uploaded_files)

    progress_bar.progress(progress)

    conn.commit()
    st.write("Database closed")
    conn.close()

    

    st.success(
     f"{len(uploaded_files)} resumes processed successfully!"
)

else:

        st.error("Please upload at least one resume")