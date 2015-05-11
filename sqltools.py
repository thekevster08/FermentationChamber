import sqlite3

def CreateTempTable():
	conn = sqlite3.connect('temperatures.db')
	cur = conn.cursor()
	cur.execute("CREATE TABLE temps (timestamp DATETIME, chamberTemp NUMERIC, wortTemp NUMERIC, motorpv NUMERIC)")
	conn.commit();
	conn.close();
	
def LogData(chamberTemp, wortTemp, motorpv):
	conn = sqlite3.connect('temperatures.db')
	curs = conn.cursor()

	curs.execute("INSERT INTO temps values(datetime('now'), ?, ?, ?)", (chamberTemp, wortTemp, motorpv))
	
	conn.commit()
	conn.close()
	
def DropTempTable():
	conn = sqlite3.connect('temperatures.db')
	curs = conn.cursor()
						   
	curs.execute('drop table if exists temps')
	CreateTempTable()