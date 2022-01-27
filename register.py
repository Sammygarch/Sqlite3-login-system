import sqlite3
import getpass
import random

username = input('Enter your username: ')
password = getpass.getpass("Enter you password: ")
id = '%032x' % random.randrange(16**32)

conn = sqlite3.connect('users')
c = conn.cursor()
c.execute("INSERT INTO users VALUES ('%s', '%s', '%s')" % (id,username,password))


conn.commit()
