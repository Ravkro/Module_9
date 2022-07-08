import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  database="pysports"
)

mycursor = mydb.cursor()

sql = "SELECT \
  player.id, \
  first.name \
  last.name \
  team.name \
  FROM users \
  LEFT JOIN players"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
