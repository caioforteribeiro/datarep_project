import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="project"
)

cursor = db.cursor()
sql="CREATE TABLE cat (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250), sex VARCHAR(250), age INT, breed VARCHAR(250))"

cursor.execute(sql)

db.close()
cursor.close()