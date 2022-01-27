import sqlite3

conn = sqlite3.connect('users')
c = conn.cursor()

c.execute("DELETE FROM users")

conn.commit()
