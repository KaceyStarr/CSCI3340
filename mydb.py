import mysql.connector 

#Create data base connection with Django
dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Minecraft1999!',
	)

#middleware 
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE 3340database")
print("Hello data base 3340data")