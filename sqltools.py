import sqlite3

def CreateTempTable():
	conn = sqlite3.connect('temperatures.db')
	cur = conn.cursor()
	cur.execute("CREATE TABLE temps (timestamp DATETIME, chamberTemp NUMERIC, wortTemp NUMERIC)")
	conn.commit();
	conn.close();
	
def log_temperature(chamberTemp, wortTemp):
	conn = sqlite3.connect('temperatures.db')
	curs = conn.cursor()

	curs.execute("INSERT INTO temps values(datetime('now'), ?, ?)", (chamberTemp, wortTemp,))
	
	conn.commit()
	conn.close()
	
def DropTempTable():
	conn = sqlite3.connect('temperatures.db')
	curs = conn.cursor()
						   
	curs.execute('drop table if exists temps')
	CreateTempTable()