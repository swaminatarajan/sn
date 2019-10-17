import pymysql
import csv

db= pymysql.connect(host='localhost',port=3306,user='root',password='password',database='boa')
cursor = db.cursor()

with open("d:/realestate2.csv","r") as fobj:
    header = fobj.readline()
    reader = csv.reader(fobj)
    for line in reader:
        data = tuple(line)
        query = "insert into realestate values('()','()','()','()','()','()','()','()','()','()','()','()')".format(*data)
        cursor.execute(query)
        
db.commit()
db.close()
        
