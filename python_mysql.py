import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='45ltpsale'
)

mycursor = mydb.cursor()
mycursor.execute('select * from 商品表')
for x in mycursor:
    print(x)