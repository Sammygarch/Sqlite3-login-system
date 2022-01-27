import sqlite3
import pandas as pd

conn = sqlite3.connect('users')
c = conn.cursor()

c.execute('''
          SELECT *
          FROM users
          ''')

df = pd.DataFrame(c.fetchall(), columns=['user_id', 'usernames','passwords'])
print (df)
