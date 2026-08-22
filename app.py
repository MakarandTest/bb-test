print("Hello from my Snyk test application")
import sqlite3

def get_user(user_id):
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE id = " + user_id
    return conn.execute(query).fetchall()
