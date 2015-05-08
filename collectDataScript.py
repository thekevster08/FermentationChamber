import temperatureTools
import sqltools
import time
import os

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
wortProbeFile = base_dir + '28-00000626d82b/w1_slave'
chamberProbeFile = base_dir + '28-00000626f736/w1_slave'

while True:
	sqltools.log_temperature(temperatureTools.read_temp(wortProbeFile), temperatureTools.read_temp(chamberProbeFile))
	time.sleep(5)