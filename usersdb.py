import sqlite3

conn = sqlite3.connect("users.db")
cur = conn.cursor()
cur.execute('''INSERT INTO users (
   	oid,username,password) VALUES (1,"Monica","test1234")
	  ''')
conn.commit()
conn.close()
