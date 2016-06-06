This directory contains a number of python scripts used over the course of the 
Embedded Linux course I took at SUNY New Paltz in the Spring of 2016. The functions
of these programs are outlined below:

logTemp.py -- A simple python script used to retrieve time/temperature information
from a raspberry pi temperature sensor. This information is then logged to a sqlite
 database where it can be retrieved by using the readTemperature.py program. Time
and Temperature information were gathered twice hourly using a cronjob

numSort.py -- A simple script used to measure hardware capabilities of multiple 
networked devices by generating a random array of integers and then using the 
bubble sort algorithm to sort those integers.




