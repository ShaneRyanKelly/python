#!/usr/bin/python
import os
import time

"""Log Current Time, Temperature in Celsius and Fahrenheit
	Returns a list [time, tempC, tempF] """

def readTemp():
	tempfile = open("/sys/bus/w1/devices/28-000006964288/w1_slave")
	tempfile_text = tempfile.read()
	currentTime = time.strftime('%x %X %Z')
	tempfile.close()
	tempC = float(tempfile_text.split("\n")[1].split("t=")[1])/1000
	tempF = tempC * 9.0/5.0 + 32.0
	return [currentTime, tempC, tempF]

print readTemp()
