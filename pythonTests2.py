import os
import pythonTests

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
wortProbeFile = base_dir + '28-00000626d82b/w1_slave'
chamberProbeFile = base_dir + '28-00000626f736/w1_slave'

print pythonTests.read_temp(wortProbeFile)
print pythonTests.read_temp(chamberProbeFile)