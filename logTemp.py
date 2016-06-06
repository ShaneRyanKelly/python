#!/usr/bin/python
#-*-coding: utf-8 -*-
# This script uses python to log the current date, time and temperature, into
# a database

import time
import sqlite3 as lite
import sys
import os

def logTemp():
	con = None
	
	con = lite.connect('dateTimeTemp.db')

	cur = con.cursor()
	
	xTime = time.strftime("%H:%M:%S")
	xDate = time.strftime("%d/%m/%Y")
	tempfile = open("/sys/bus/w1/devices/28-000006964288/w1_slave")
	tempfile_text = tempfile.read()
	tempfile.close()
	tempC = float(tempfile_text.split("\n")[1].split("t=")[1])/1000
	tempF = tempC * 9.0/5.0 + 32.0

	print "sending current date, time, and temp to database"

	cur.execute("INSERT INTO temp VALUES(?, ?, ?, ?)", (xDate, xTime, tempC, tempF))

	con.commit()
	con.close()

	return

logTemp()
