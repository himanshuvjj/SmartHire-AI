import bcrypt
from database import get_connection


# Hash password
def hash_password(password):

    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    return hashed.decode()


# Register user
def register_user(username, password, role):

    conn = get_connection()

    cursor = conn.cursor()

    hashed_password = hash_password(password)

    query = """
    INSERT INTO users (username, password, role)
    VALUES (%s, %s, %s)
    """

    values = (username, hashed_password, role)

    cursor.execute(query, values)

    conn.commit()

    conn.close()


# Login user
def login_user(username, password):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT password
    FROM users
    WHERE username = %s
    """

    cursor.execute(query, (username,))

    result = cursor.fetchone()

    conn.close()

    if result:

        stored_password = result[0]

        return bcrypt.checkpw(
            password.encode(),
            stored_password.encode()
        )

    return False