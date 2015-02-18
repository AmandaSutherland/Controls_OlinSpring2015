import serial 
data = serial.Serial('/dev/ttyACM0', 9600)
file_ = open('data/ice_test.csv', 'w')
while(1):
	a = data.readline()
	file_.write(a) 
