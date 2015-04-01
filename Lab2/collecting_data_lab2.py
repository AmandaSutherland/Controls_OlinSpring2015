import serial 
import platform
import time
if platform.system() == 'Linux':
    data = serial.Serial('/dev/ttyACM0', 9600)
elif platform.system() == 'Darwin':
    data = serial.Serial('/dev/tty.usbmodem1451')

file_ = open('data/Part1_3_600mA.csv', 'w')
wait = time.time() + 3
while time.time() < wait:
    pass
stop = time.time() + 10
while time.time() < stop:
	a = data.readline()
	file_.write(a)
