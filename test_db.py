from database import get_connection

conn = get_connection()

if conn.is_connected():
  print("Database connection successfully")
else:  print("Database connection failed")