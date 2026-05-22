from database import get_connection


conn = get_connection()

cursor = conn.cursor()


cursor.execute("""

CREATE TABLE IF NOT EXISTS candidates (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT,

    email TEXT,

    phone TEXT,

    skills TEXT,

    resume_path TEXT,

    status TEXT,

    match_score REAL,

    extracted_skills TEXT

)

""")


conn.commit()

conn.close()


print("Database Created Successfully")