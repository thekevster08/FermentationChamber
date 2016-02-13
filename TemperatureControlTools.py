import RPi.GPIO as GPIO

HEATER_PIN = 22

def heatOn():
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(HEATER_PIN, GPIO.OUT)
    GPIO.output(HEATER_PIN, 1) 

def heatOff():
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(HEATER_PIN, GPIO.OUT)
    GPIO.output(HEATER_PIN, 0)