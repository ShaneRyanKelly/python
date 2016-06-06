#!/usr/bin/python
# -*- coding: utf-8 -*-
# a simple script for pulling the logged times and dates from
# the sqlite database testTime.db
# times may be logged into the database by executing logTime.py
import sqlite3 as lite
import sys

def fetchTime():
	con = lite.connect('testTime.db')

	with con:
		cur = con.cursor()
		cur.execute("SELECT * FROM time")

		rows = cur.fetchall()
		
		for row in rows:
			print row

	return

fetchTime()
