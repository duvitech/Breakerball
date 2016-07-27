# Copyright (c) 2016 Lawrence King
# lawrencek52@gmail.com
# All rights reserved
import serial
import pyupm_i2clcd
from array import array
import socket
import time
import sys

PORT = 42001
HOST = '127.0.0.1'
if not HOST:
    sys.exit()
print("connecting...")
scratchSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
scratchSock.connect((HOST,PORT))
print("connected.")

ard = serial.Serial('/dev/tty96B0', 9600)
lcd = pyupm_i2clcd.Jhd1313m1(0, 0x3e, 0x62)

def sendScratchCommand(cmd):
    n = len(cmd)
    a = array('c')
    a.append(chr((n>>24) & 0xFF))
    a.append(chr((n>>16) & 0xFF))
    a.append(chr((n>>8) & 0xFF))
    a.append(chr((n) & 0xFF))
    scratchSock.send(a.tostring() + cmd)

def showSlider(pos):
	lcd.clear()
	lcd.setCursor(0, 0)
	lcd.write("Position: " + pos)
	lcd.setColor(255, 180, 180)

if __name__ == '__main__':
	print("Welcome to the slide pot reader!!!")
	try:
		while True:
			ardOut = ard.readline()
			if ardOut.find("p:") != -1:
				ardSlider = ardOut.split('p:')[1]
				msg = str(((int(ardSlider)*351/1024)-175))
				showSlider(msg)
        			sendScratchCommand("sensor-update \"slider\" %s" % msg)
	except KeyboardInterrupt:
		lcd.setColor(0,0,0)
		lcd.clear()
		print("CTRL-C!! Exiting...")
