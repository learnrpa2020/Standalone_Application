import sqlite3

conn = sqlite3.connect("students_book_info.db")
cur = conn.cursor()

cur.execute('''CREATE TABLE student_book_info (
	b_id text PRIMARY KEY,
   	s_id text NOT NULL,
	borrow_date text NOT NULL,
	return_date text
)
	  ''')
conn.commit()
conn.close()
