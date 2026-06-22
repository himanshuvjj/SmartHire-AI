import streamlit as st
import pandas as pd
from email_sender import send_email

from database import get_connection


st.title("Candidate Dashboard")

minimum_score = st.slider(
    "Minimum Match Score",
    0,
    100,
    0
)


# Database Connection
conn = get_connection()


# Read Candidate Data
query = f"SELECT * FROM candidates WHERE match_score >= {minimum_score}"

df = pd.read_sql(query, conn)

job_titles = sorted(
    df["job_title"].dropna().unique()
)

selected_job = st.selectbox(
    "Filter by Job Title",
    ["All"] + list(job_titles)
)

if selected_job != "All":
    df = df[
        df["job_title"] == selected_job
    ]

df["match_score"] = pd.to_numeric(
    df["match_score"],
    errors="coerce"
)

df = df.dropna(subset=["match_score"])


# Display Table

# Filter Candidates
df = df[
    df["match_score"] >= minimum_score
]
# Sort Candidates by Match Score
ranked_df = df.sort_values(
    by="match_score",
    ascending=False
)


# Add Ranking Column
ranked_df.insert(
    0,
    "Rank",
    range(1, len(ranked_df) + 1)
)

# Top Candidate

if not ranked_df.empty:

    top_candidate = ranked_df.iloc[0]

    st.success(
        f"""

Top Candidate: {top_candidate['name']}

Match Score: {top_candidate['match_score']}%

"""
    )

else:

    st.warning(
        "No candidates found for selected score"
    )

# Status Color Function
def highlight_status(row):

    if row["status"] == "Selected":

        return ["background-color: lightgreen"] * len(row)

    elif row["status"] == "Rejected":

        return ["background-color: #ffcccc"] * len(row)

    else:

        return [""] * len(row)


# Apply Styling
styled_df = ranked_df.style.apply(
    highlight_status,
    axis=1
)


# Display Styled Dataframe
st.dataframe(styled_df)

st.subheader("Send Interview Email")


candidate_email = st.text_input(
    "Candidate Email"
)


if st.button("Send Interview Invitation"):

    subject = "Interview Invitation"

    message = """

Dear Candidate,

You have been shortlisted for interview.

Regards,
HR Team

"""

    send_email(
        candidate_email,
        subject,
        message
    )

    st.success(
        "Interview Email Sent Successfully"
    )

conn.close()