import sqlite3

conn = sqlite3.connect('users')
c = conn.cursor()
c.execute('''
          CREATE TABLE users
          ([user_id] NUMERIC PRIMARY KEY, [usernames] TEXT, [passwords] TEXT)
          ''')

conn.commit()
