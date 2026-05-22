from database import get_connection

conn = get_connection()

cursor = conn.cursor()

query = "Select * from users "

cursor.execute(query)

users = cursor.fetchall()

for user in users:
  print(user)

conn.close()