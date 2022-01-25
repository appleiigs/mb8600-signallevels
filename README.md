# mb8600-signallevels
Query Motorola MB8600 cable modem signal levels &amp; save to CSV file

I made this in my quest to figure out Comcast's problem with my house. I scheduled it to run every 5 minutes to record the data.

Usage: python mb8600_signallevels.py

Notes:
Assumes that the MB8600 home page is at https:////192.168.100.1/ Edit the "modemURL" variable to change that.
Edit the "mb8600UserName" and "mb8600Password" variables to match the username and password that you've chosen.  Or add code to pass them in as command-line arguments.
Outputs the tables to a CSV file named mb8600.csv. Edit the "outputFileName" to change that.

Requirements:
Python 3
webbot
selenium 3.14 (webbot doesn't work with Selenium 4)
