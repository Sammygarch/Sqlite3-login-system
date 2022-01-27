import sqlite3

conn = sqlite3.connect('users')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS users
          ([user_id] INTEGER PRIMARY KEY, [username] TEXT, [passwords] TEXT)
          ''')

conn.commit()
