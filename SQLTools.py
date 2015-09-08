import sqlite3

def create_temperature_table():
	conn = sqlite3.connect('temperatures.db')
	cur = conn.cursor()
	cur.execute("CREATE TABLE temps (timestamp DATETIME, chamberTemp NUMERIC, wortTemp NUMERIC, motorpv NUMERIC)")
	conn.commit();
	conn.close();
	
def log_data(chamberTemp, wortTemp, motorpv):
	conn = sqlite3.connect('temperatures.db')
	curs = conn.cursor()

	curs.execute("INSERT INTO temps values(datetime('now'), ?, ?, ?)", (chamberTemp, wortTemp, motorpv))
	
	conn.commit()
	conn.close()
	
def drop_temperature_table():
	conn = sqlite3.connect('temperatures.db')
	curs = conn.cursor()
						   
	curs.execute('drop table if exists temps')
	create_temperatTable()