import sqlite3

def create_db():
	con= sqlite3.connect(database ="RTO.db")

	cur=con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS Employee(fname text, lname text, contact text, email text primary key, question text, answer text, passw text, cpassw text)")
	con.commit()
	con.close()
create_db()