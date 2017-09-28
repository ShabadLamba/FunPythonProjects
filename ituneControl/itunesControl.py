####################################
# Arduino iTunes Controler v1.0
# written by Shabad Lamba
# created 2016.01.07
####################################

import serial
import os

connected = False

ser = serial.Serial("/dev/cu.usbmodem1421"	,9600)
print ser

flag=1

while not connected:
	serin = ser.readline() #reading a line from the serial port
	serinNew = serin.split('\r')[0] 
	print serinNew
	if serinNew == "Detected!":
		if flag == 1:
			os.system('/Users/shabadlamba/Documents/Arduino/./itunes.sh play')
			flag=0
		else:
			os.system('/Users/shabadlamba/Documents/Arduino/./itunes.sh pause')
			flag=1
	if serin == "exit":  
		connected = True

ser.close()