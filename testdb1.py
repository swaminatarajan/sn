import pymysql

db = pymysql.connect(host="localhost", port=3306, user="root", password="password", database="boa")

cursor = db.cursor()

selQuery = "select * from employee"

cursor.execute(selQuery)

for record in cursor.fetchall() :
    print(record)
    
db.close()    