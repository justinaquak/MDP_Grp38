import time
import serial

ser = serial.Serial("/dev/ttyUSB1", baudrate = 115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
counter=0
try:
	ser.open()
except:
	print("Error")
while 1:
	#ser.write(b"Write counter: %d \n"%(counter))
	ser.write(b'b\0')
	line = ser.readline()
	print(line)
   #print("Printed")
	time.sleep(1)
	counter += 1

