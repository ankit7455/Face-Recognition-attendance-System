import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="student"
)

mycursor = mydb.cursor()

sql = "select * from attedance"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected") 