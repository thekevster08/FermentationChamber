import threading
import TemperatureTools
import SQLTools
import time
import os
from random import randint
from ConfigParser import SafeConfigParser

import contextlib
import sqlite3
import json
import sys

class CollectDataThread(threading.Thread):
	config = SafeConfigParser()
	
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
		self.mutex = threading.Lock()
		self.paused = False
		self.start()
		self.pause()
		
	def pause(self):
		if(not self.paused):
			self.mutex.acquire()
			self.paused = True
			
	def unpause(self):
		self.mutex.release()
		self.paused = False
		
	def run(self):
		print "starting" + self.name
		while True:
			self.mutex.acquire()
			print "collectingData"
			self.config.read('config.ini')
			wortTemperature = randint(50,60)
			chamberTemperature = wortTemperature + 5
			ambientTemperature = wortTemperature + 10
			# primarySetpoint = 50
			
			primarySetpoint = int(self.config.get('controller', 'setpoint'))
			secondarySetpoint = 25
			primaryControllerOutput = 70
			secondaryControllerOutput = 20
			coldOn = randint(0,1) #GPIO.input(22)
			hotOn = randint(0,1) #GPIO.input(21)
	
		 	SQLTools.log_data(wortTemperature, chamberTemperature, ambientTemperature, primarySetpoint, secondarySetpoint, primaryControllerOutput, secondaryControllerOutput, coldOn, hotOn)
	
			with contextlib.closing(sqlite3.connect('./static/temperatures.db')) as database:
				with contextlib.closing(database.cursor()) as cursor:
 					cursor.execute('select strftime("%s", timestamp)*1000, chamberTemp, wortTemp, ambientTemp, primarySetpoint, secondarySetpoint, primaryControllerOutput, secondaryControllerOutput, coldOn, hotOn from temps')
 					temperatures = []
 					for timestamp, chamberTemp, wortTemp, ambientTemp, primarySetpoint, secondarySetpoint, primaryControllerOutput, secondaryControllerOutput, coldOn, hotOn in cursor:
 						temperatures.append([timestamp, chamberTemp, wortTemp, ambientTemp, primarySetpoint, secondarySetpoint, primaryControllerOutput, secondaryControllerOutput, coldOn, hotOn])
	
 			with open('./static/temperatures.json','w') as outfile:
 				json.dump(temperatures, outfile)
 			self.config.read('config.ini')
 			time.sleep(int(self.config.get('main', 'sampleTime')))
			
			self.mutex.release()
		
		
		
		
		
# while True:
# 	wortTemperature = randint(65,70)
# 	chamberTemperature = wortTemperature + 5
# 	ambientTemperature = wortTemperature + 10
	
# 	SQLTools.log_data(wortTemperature, chamberTemperature, ambientTemperature)
	
# 	with contextlib.closing(sqlite3.connect('./static/temperatures.db')) as database:
# 		with contextlib.closing(database.cursor()) as cursor:
# 			cursor.execute('select strftime("%s", timestamp)*1000, chamberTemp, wortTemp, ambientTemp from temps')
# 			temperatures = []
# 			for timestamp, chamberTemp, wortTemp, motorpv in cursor:
# 				temperatures.append([timestamp, chamberTemp, wortTemp, motorpv])
	
# 	with open('./static/temperatures.json','w') as outfile:
# 		json.dump(temperatures, outfile)
# 	time.sleep(5)