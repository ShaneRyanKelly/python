#!/usr/bin/python
#-*-coding: utf-8 -*-
# This script uses python to log the current date and time into a database
# the time is fetched using python's time module, the data is then logged
# in the sqlite database testTime.db

# the information in this database may be accessed by executing getTime.py

import time
import sqlite3 as lite
import sys

def logTime():
	con = None

	con = lite.connect('testTime.db')
	
	cur = con.cursor()

	xTime = time.strftime("%H:%M:%S")
	xDate = time.strftime("%d/%m/%Y")
		
	print "sending current date and time to database"

	cur.execute("INSERT INTO time VALUES(?, ?)", (xTime, xDate))

	con.commit()
	con.close()
	

	return


	
logTime()
