import mysql.connector
database = mysql.connector.connect(
	host = 'localhost',
	user = 'sarge',
	password = '27121994'
	)
#prepare cursor object
cursorObject = database.cursor()

#create Database
cursorObject.execute("CREATE DATABASE dcrmdb")

print("All done")


