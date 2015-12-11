import TemperatureTools
import SQLTools
import time
import os
from random import randint

import contextlib
import sqlite3
import json
import sys
#import RPi.GPIO as GPIO



	
	#GPIO.setmode(GPIO.BOARD)
	
#	MOTOR = 22
	
	#GPIO.setup(MOTOR, GPIO.OUT)
	
	#p = GPIO.PWM(MOTOR, 50)
	
	#p.start(0)
	
#	os.system('modprobe w1-gpio')
#	os.system('modprobe w1-therm')
	
#	base_dir = '/sys/bus/w1/devices/'
#	wortProbeFile = base_dir + '28-00000626d82b/w1_slave'
#	chamberProbeFile = base_dir + '28-00000626f736/w1_slave'


SQLTools.drop_temperature_table()

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