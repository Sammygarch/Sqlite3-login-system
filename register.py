import sqlite3
import getpass

username = input("Enter your username: ")
password = getpass.getpass("Enter you password: ")


conn = sqlite3.connect('users')
c = conn.cursor()



c.execute('''
          INSERT INTO users (username, passwords)
          VALUES (username, password)
          ''')
				
          
c.commit()
            
