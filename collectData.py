import TemperatureTools
import SQLTools
import time
import os
import RPi.GPIO as GPIO

import contextlib
import sqlite3
import json
import sys
import time

SETPOINT = 68

GPIO.setmode(GPIO.BOARD)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
wortProbeFile = base_dir + '28-00000626d82b/w1_slave'
chamberProbeFile = base_dir + '28-00000626f736/w1_slave'
ambientProbeFile = base_dir + '28-0000062883c0/w1_slave'

while True:
	wortTemperature = TemperatureTools.read_temp(wortProbeFile)
	chamberTemperature = TemperatureTools.read_temp(chamberProbeFile)
	ambientTemperature = TemperatureTools.read_temp(ambientProbeFile)
	
	SQLTools.LogData(wortTemperature, chamberTemperature, ambientTemperature)
	
	with contextlib.closing(sqlite3.connect('temperatures.db')) as database:
		with contextlib.closing(database.cursor()) as cursor:
			cursor.execute('select strftime("%s", timestamp)*1000, chamberTemp, wortTemp, ambientTemp from temps')
			temperatures = []
			for timestamp, chamberTemp, wortTemp, motorpv in cursor:
				temperatures.append([timestamp, chamberTemp, wortTemp, motorpv])

with open('./static/temperatures.json','w') as outfile:
	json.dump(temperatures, outfile)
time.sleep(5)