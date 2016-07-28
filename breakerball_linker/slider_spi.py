#
# Copyright (c) 2016 Lawrence King lawrencek52@gmail.com All Rights Reserved.
#
import serial
from array import array
import socket
import time
import sys
import spidev


PORT = 42001
HOST = '127.0.0.1'
if not HOST:
    sys.exit()

print("connecting...")
scratchSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
scratchSock.connect((HOST,PORT))
print("connected.")

spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=100000
channel_select=[0x01, 0x80, 0x00]

def sendScratchCommand(cmd):
    n = len(cmd)
    a = array('c')
    a.append(chr((n>>24) & 0xFF))
    a.append(chr((n>>16) & 0xFF))
    a.append(chr((n>>8) & 0xFF))
    a.append(chr((n) & 0xFF))
    scratchSock.send(a.tostring() + cmd)



if __name__ == '__main__':
	print("Welcome to the slide pot reader!!!")
	try:
		while True:
			adc_data = spi.xfer(channel_select)
			adc = ((adc_data[1]<<8)&0x300)|(adc_data[2]&0xFF)
			msg = str(((adc*351)/1024)-175)
        		sendScratchCommand("sensor-update \"slider\" %s" % msg)
#			print(msg)
			time.sleep(1.0/20)
	except KeyboardInterrupt:
		print("CTRL-C!! Exiting...")
