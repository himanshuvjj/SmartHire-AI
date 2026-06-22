from database import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS candidates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20),
    skills TEXT,
    resume_path TEXT,
    status VARCHAR(50),
    match_score FLOAT,
    extracted_skills TEXT,
    job_title VARCHAR(255)
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")