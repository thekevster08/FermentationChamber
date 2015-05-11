import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

motor = 1

GPIO.setup(motor, GPIO.OUT)

print "turning on"

GPIO.output(motor, GPIO.HIGH)

sleep(2)

print "stopping"
GPIO.output(motor, GPIO.LOW)

GPIO.cleanup()