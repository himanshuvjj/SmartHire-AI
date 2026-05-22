from database import get_connection

conn = get_connection()

cursor = conn.cursor()

query = """ 
Insert into users (username,password,role)
VALUES (%s,%s,%s)
"""

values = ("himanshu","2004","admin")

cursor.execute(query,values)

conn.commit()

print("User inserted successfully")

conn.close()