import mysql.connector

db_cf = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "1234567",
    database = "arduino",
) 
cursor = db_cf.cursor()
sql = """
select * from bme680_data
"""
cursor.execute(sql)
op = cursor.fetchall()

for i in op:
    print(i)
