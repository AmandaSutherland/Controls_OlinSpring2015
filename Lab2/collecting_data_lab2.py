import serial 
import platform
import time
if platform.system() == 'Linux':
    data = serial.Serial('/dev/ttyACM0', 9600)
elif platform.system() == 'Darwin':
    data = serial.Serial('/dev/tty.usbmodem1451')

file_ = open('data/Part1_2_5V.csv', 'w')
stop = time.time() + 3
while time.time() < stop:
	a = data.readline()
	file_.write(a)
