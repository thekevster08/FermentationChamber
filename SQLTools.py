import sqlite3, shutil, json, os

#creates a new database titled "temps" with three fields, "chamberTemp", "wortTemp", and "ambientTemp"
def create_temperature_table():
	conn = sqlite3.connect('/var/www/FermentationChamber/FermentationChamber/static/temperatures.db')
	cur = conn.cursor()
	cur.execute("CREATE TABLE temps (timestamp DATETIME, chamberTemp NUMERIC, wortTemp NUMERIC, ambientTemp NUMERIC)")
	conn.commit();
	conn.close();

#creates a new entry into the "temps" table in the "temperatures" database
def log_data(chamberTemp, wortTemp, ambientTemp):
	conn = sqlite3.connect('/var/www/FermentationChamber/FermentationChamber/static/temperatures.db')
	curs = conn.cursor()

	curs.execute("INSERT INTO temps values(datetime('now'), ?, ?, ?)", (chamberTemp, wortTemp, ambientTemp))
	
	conn.commit()
	conn.close()
	
#deletes the "temps" table in the "temperatures" database. Clears the JSON database.
def drop_temperature_table():
	conn = sqlite3.connect('/var/www/FermentationChamber/FermentationChamber/static/temperatures.db')
	curs = conn.cursor()
						   
	curs.execute('drop table if exists temps')
	create_temperature_table()
	
	with open('/var/www/FermentationChamber/FermentationChamber/static/temperatures.json','w') as outfile:
		json.dump([], outfile)

#creates a copy of the temperatures database 
def save_temperature_table(filename):
	src = '/var/www/FermentationChamber/FermentationChamber/static/'
	dst = '/var/www/FermentationChamber/FermentationChamber/static/'
	shutil.copy2(os.path.join(src, 'temperatures.db'), dst + filename + '.db')
	
def load_temperature_table(filename):
	shutil.copy('/var/www/FermentationChamber/FermentationChamber/static/' + filename + '.db', '/var/www/FermentationChamber/FermentationChamber/static/temperatures.db')