import streamlit as st
import pandas as pd
import plotly.express as px

from database import get_connection


st.title("SmartHire AI Analytics Dashboard")
search_name = st.text_input("Search Candidate")

# Database Connection
conn = get_connection()


# Read Candidate Data
query = "SELECT * FROM candidates"

df = pd.read_sql(query, conn)

conn.close()


# =========================
# SUMMARY METRICS
# =========================

st.subheader("Recruitment Overview")


total_candidates = len(df)

selected_candidates = len(
    df[df["status"] == "Selected"]
)

rejected_candidates = len(
    df[df["status"] == "Rejected"]
)

average_score = round(
    df["match_score"].mean(),
    2
)


# Display Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Candidates",
    total_candidates
)

col2.metric(
    "Selected",
    selected_candidates
)

col3.metric(
    "Rejected",
    rejected_candidates
)

col4.metric(
    "Average Score",
    f"{average_score}%"
)


# =========================
# STATUS DISTRIBUTION
# =========================

st.subheader("Candidate Status Distribution")


status_chart = px.pie(
    df,
    names="status",
    title="Hiring Status Distribution"
)

st.plotly_chart(
    status_chart,
    use_container_width=True
)


# =========================
# MATCH SCORE CHART
# =========================

st.subheader("Candidate Match Scores")


score_chart = px.bar(
    df,
    x="name",
    y="match_score",
    title="AI Match Score by Candidate"
)

st.plotly_chart(
    score_chart,
    use_container_width=True
)


# =========================
# TOP CANDIDATE
# =========================

st.subheader("Top Candidate")


top_candidate = df.sort_values(
    by="match_score",
    ascending=False
).head(1)


st.dataframe(top_candidate)
# =========================
# CANDIDATE TABLE
# =========================

st.subheader("Candidate Records")
if search_name:

    filtered_df = df[
        df["name"].str.contains(
            search_name,
            case=False
        )
    ]

    st.dataframe(filtered_df)

else:

    st.dataframe(df)