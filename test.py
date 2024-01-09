from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import gspread
import mysql.connector
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
cerds = ServiceAccountCredentials.from_json_keyfile_name("cerds.json", scope)
client = gspread.authorize(cerds)
sheet = client.open("test_data_logger").worksheet('ชีต1') # เป็นการเปิดไปยังหน้าชีตนั้นๆ
data = sheet.get_all_records()  # การรับรายการของระเบียนทั้งหมด
list_t = []
for i in data:
    print(i["อุณหภูมิ"])
    list_t.append(i["อุณหภูมิ"])
    
#db
db = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "1234567",
    database = "arduino",
) 
cursor = db.cursor()
sql ="""
insert into bme680_data (time,temperature) values (%s);
"""
cursor.executemany(sql, [(temp,) for temp in list_t])
db.commit()
print(f"insert {str(cursor.rowcount)} row")
print([(temp,) for temp in list_t])