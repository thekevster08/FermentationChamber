#!/usr/bin/env python3
import contextlib
import sqlite3
import json
import sys
import time

def record_JSON():
	while True:
		with contextlib.closing(sqlite3.connect('temperatures.db')) as database:
			with contextlib.closing(database.cursor()) as cursor:
				cursor.execute('select strftime("%s", timestamp)*1000, chamberTemp, wortTemp, motorpv from temps')
				temperatures = []
				for timestamp, chamberTemp, wortTemp, motorpv in cursor:
					temperatures.append([timestamp, chamberTemp, wortTemp, motorpv])
	
		with open('temperatures.json','w') as outfile:
			json.dump(temperatures, outfile)
	
		time.sleep(5)