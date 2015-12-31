import sqlite3, shutil, json, os

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(PROJECT_ROOT, 'static', 'temperatures.db')

#creates a new database titled "temps" with three fields, "chamberTemp", "wortTemp", and "ambientTemp"
def create_temperature_table():
	conn = sqlite3.connect('var/www/FermentationChamber/FermentationChamber/static/temperatures.db')
	cur = conn.cursor()
	cur.execute("CREATE TABLE temps (timestamp DATETIME, chamberTemp NUMERIC, wortTemp NUMERIC, ambientTemp NUMERIC)")
	conn.commit();
	conn.close();

#creates a new entry into the "temps" table in the "temperatures" database
def log_data(chamberTemp, wortTemp, ambientTemp):
	conn = sqlite3.connect('var/www/FermentationChamber/FermentationChamber/static/temperatures.db')
	curs = conn.cursor()

	curs.execute("INSERT INTO temps values(datetime('now'), ?, ?, ?)", (chamberTemp, wortTemp, ambientTemp))
	
	conn.commit()
	conn.close()
	
#deletes the "temps" table in the "temperatures" database. Clears the JSON database.
def drop_temperature_table():
	# conn = sqlite3.connect('./static/temperatures.db')
	conn = sqlite3.connect('var/www/FermentationChamber/FermentationChamber/static/temperatures.db')
	curs = conn.cursor()
						   
	curs.execute('drop table if exists temps')
	create_temperature_table()
	
	with open('var/www/FermentationChamber/FermentationChamber/static/temperatures.json','w') as outfile:
		json.dump([], outfile)

#creates a copy of the temperatures database 
def save_temperature_table(filename):
	shutil.copy2('var/www/FermentationChamber/FermentationChamber/static/temperatures.db','var/www/FermentationChamber/FermentationChamber/static/' + filename +'.db')
	
def load_temperature_table(filename):
	shutil.copy2('var/www/FermentationChamber/FermentationChamber/static/' + filename +'.db', './static/temperatures.db',)