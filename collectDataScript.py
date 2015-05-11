import temperatureTools
import sqltools
import time
import os
import RPi.GPIO as GPIO

SETPOINT = 68

GPIO.setmode(GPIO.BOARD)

MOTOR = 22

GPIO.setup(MOTOR, GPIO.OUT)

p = GPIO.PWM(MOTOR, 50)

p.start(0)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
wortProbeFile = base_dir + '28-00000626d82b/w1_slave'
chamberProbeFile = base_dir + '28-00000626f736/w1_slave'

while True:
	wortTemperature = temperatureTools.read_temp(wortProbeFile)
	chamberTemperature = temperatureTools.read_temp(chamberProbeFile)
	
	if wortTemperature < SETPOINT:
		motorpv = 0
	elif wortTemperature > SETPOINT:
		motorpv = 100
		
	p.ChangeDutyCycle(motorpv)
	
	sqltools.LogData(wortTemperature, chamberTemperature, motorpv)
	time.sleep(5)