import TemperatureTools
import SQLTools
import time
import os
from random import randint

import contextlib
import sqlite3
import json
import sys

while True:
	wortTemperature = randint(65,70)
	chamberTemperature = wortTemperature + 5
	ambientTemperature = wortTemperature + 10
	
	SQLTools.log_data(wortTemperature, chamberTemperature, ambientTemperature)
	
	with contextlib.closing(sqlite3.connect('./static/temperatures.db')) as database:
		with contextlib.closing(database.cursor()) as cursor:
			cursor.execute('select strftime("%s", timestamp)*1000, chamberTemp, wortTemp, ambientTemp from temps')
			temperatures = []
			for timestamp, chamberTemp, wortTemp, motorpv in cursor:
				temperatures.append([timestamp, chamberTemp, wortTemp, motorpv])
	
	with open('./static/temperatures.json','w') as outfile:
		json.dump(temperatures, outfile)
	time.sleep(5)