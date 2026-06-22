# SmartHire AI – AI-Powered Resume Screening & Candidate Tracking System

## Overview

SmartHire AI is an AI-powered Resume Screening and Candidate Tracking System designed to automate the initial stages of recruitment using Natural Language Processing (NLP) and Machine Learning.


---

## Features

* Bulk Resume Upload
* Automated Resume Parsing
* Candidate Information Extraction
* Semantic AI Match Score Calculation
* Automatic Skill Extraction
* Candidate Ranking System
* Job Title-Based Candidate Tracking
* Search and Filter Candidates
* Recruitment Analytics Dashboard
* Email Notification System
* User Authentication System
* MySQL Database Integration
* Streamlit Multipage Interface

---

## How It Works

1. Recruiters enter a job title and job description.

2. One or multiple resumes are uploaded.

3. The system extracts:

   * Candidate Name
   * Email Address
   * Phone Number
   * Skills

4. Resume text and job descriptions are converted into semantic embeddings using Sentence Transformers.

5. Cosine similarity calculates an AI match score.

6. Candidates are ranked automatically based on their scores.

7. Recruiters can filter candidates by job role and visualize hiring metrics through interactive dashboards.

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Database

* MySQL
* MySQL Connector

### Machine Learning & NLP

* Sentence Transformers (`all-MiniLM-L6-v2`)
* Semantic Embeddings
* Cosine Similarity
* Scikit-learn
* spaCy (`en_core_web_sm`)

### Resume Processing

* PDFPlumber

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly

### Authentication & Security

* Bcrypt

### Email Service

* SMTP (`smtplib`)

### Development Tools

* Git
* GitHub

---

## Project Structure

```text
SmartHire-AI/
│
├── pages/
│   ├── upload_resume.py
│   ├── dashboard.py
│   └── analytics_dashboard.py
│
├── resumes/
│
├── app.py
├── auth.py
├── database.py
├── email_sender.py
├── ml_model.py
├── resume_parser.py
├── skill_extractor.py
├── candidate_extractor.py
├── requirements.txt
└── README.md
```

---

## AI Matching Pipeline

```text
Job Description
        │
        ▼
Sentence Transformer
(all-MiniLM-L6-v2)
        │
        ▼
Semantic Embeddings
        │
        ▼
Cosine Similarity
        │
        ▼
AI Match Score
        │
        ▼
Candidate Ranking
```

Unlike traditional keyword matching systems, SmartHire AI uses semantic embeddings to understand contextual similarities between resumes and job descriptions.

This allows the system to identify relevant candidates even when different terminology is used.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/himanshuvjj/SmartHire-AI.git
```

Navigate to the project directory:

```bash
cd SmartHire-AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure your MySQL credentials in `database.py`.

Create the required database tables.

Run the application:

```bash
streamlit run app.py
```

---

## Database Schema

### Users Table

| Column   | Type    |
| -------- | ------- |
| id       | INT     |
| username | VARCHAR |
| password | VARCHAR |
| role     | VARCHAR |

### Candidates Table

| Column           | Type    |
| ---------------- | ------- |
| id               | INT     |
| name             | VARCHAR |
| email            | VARCHAR |
| phone            | VARCHAR |
| skills           | TEXT    |
| extracted_skills | TEXT    |
| resume_path      | TEXT    |
| job_title        | VARCHAR |
| status           | VARCHAR |
| match_score      | FLOAT   |

---

## Key Benefits

* Reduces manual resume screening efforts
* Accelerates candidate shortlisting
* Improves recruiter productivity
* Provides consistent evaluation criteria
* Enables data-driven hiring decisions
* Supports multiple job openings simultaneously

---

## Future Enhancements

* Weighted Skill Matching
* Duplicate Resume Detection
* Candidate Status Workflow
* Recruiter Notes and Feedback
* Interview Scheduling
* Resume Summarization with LLMs
* Cloud Database Integration
* Production Deployment

---

## Author

**Himanshu Vijay**
