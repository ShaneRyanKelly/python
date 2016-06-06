import sqlite3 as lite
import sys

def fetchTemp():
	con = lite.connect('dateTimeTemp.db')
	
	with con:
		cur = con.cursor()
		cur.execute("SELECT * FROM temp")

		rows = cur.fetchall()

		for row in rows:
			print row

	return

fetchTemp()
