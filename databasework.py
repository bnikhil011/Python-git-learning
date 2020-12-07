import mysql.connector as con

mydb = con.connect(host="localhost",
                   user="root",
                    password="",
                   database="myhibernatdb")
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM parents")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)