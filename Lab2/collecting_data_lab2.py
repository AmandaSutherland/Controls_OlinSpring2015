import serial 
import platform
import time
if platform.system() == 'Linux':
    data = serial.Serial('/dev/ttyACM0', 9600)
elif platform.system() == 'Darwin':
    data = serial.Serial('/dev/tty.usbmodem1451')

file_ = open('data/Part2_1_8V.csv', 'w')
wait = time.time() + 1
while time.time() < wait:
    pass
stop = time.time() + 6
while time.time() < stop:
	a = data.readline()
	file_.write(a)
