import sqlite3
import shutil
import json

def create_temperature_table():
	conn = sqlite3.connect('./static/temperatures.db')
	cur = conn.cursor()
	cur.execute("CREATE TABLE temps (timestamp DATETIME, chamberTemp NUMERIC, wortTemp NUMERIC, ambientTemp NUMERIC)")
	conn.commit();
	conn.close();
	
def log_data(chamberTemp, wortTemp, ambientTemp):
	conn = sqlite3.connect('./static/temperatures.db')
	curs = conn.cursor()

	curs.execute("INSERT INTO temps values(datetime('now'), ?, ?, ?)", (chamberTemp, wortTemp, ambientTemp))
	
	conn.commit()
	conn.close()
	
def drop_temperature_table():
	with open('./static/temperatures.json','w') as outfile:
		json.dump([], outfile)
		
	conn = sqlite3.connect('./static/temperatures.db')
	curs = conn.cursor()
						   
	curs.execute('drop table if exists temps')
	create_temperature_table()
	
	with open('./static/temperatures.json','w') as outfile:
		json.dump([], outfile)
	
def save_temperature_table(filename):
	shutil.copy2('./static/temperatures.db','./static/' + filename +'.db')
	
def load_temperature_table(filename):
	shutil.copy2('./static/' + filename +'.db', './static/temperatures.db',)