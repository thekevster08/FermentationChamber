import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)

def heatOn():
    GPIO.output(22,1)
    print "heaton"

def heatOff():
    GPIO.output(22,0)
    print "heatoff"

def coldOn():
    GPIO.output(21,1)
    print "coldon"

def coldOff():
    GPIO.output(21,0)
    print "coldoff"