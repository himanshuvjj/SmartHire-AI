import streamlit as st


st.set_page_config(
    page_title="SmartHire AI",
    page_icon="🤖",
    layout="wide"
)


# Sidebar
st.sidebar.title("SmartHire AI")

st.sidebar.info("""

AI Powered Recruitment System

Modules:
- Dashboard
- Upload Resume
- Analytics

""")


# Main Page
st.title("SmartHire AI")

st.subheader(
    "AI Powered Resume Screening System"
)


st.write("""

Welcome to SmartHire AI.

Use the sidebar to navigate through the application.

Features:
- Resume Upload
- AI Resume Screening
- Analytics Dashboard
- Candidate Tracking

""")