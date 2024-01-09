from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import gspread
import mysql.connector
from datetime import datetime
import schedule
import time
def job():
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    cerds = ServiceAccountCredentials.from_json_keyfile_name("cerds.json", scope)
    client = gspread.authorize(cerds)
    sheet = client.open("datafromsensor").worksheet('main')
    data_fromgs = sheet.get_all_records()
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
    data_fromdb = cursor.fetchall()
    for i in data_fromdb:
        print(i)
    print(f"number of row from google sheet is {len(data_fromgs)} ")
    print(f"number of row from database is {len(data_fromdb)} ")
    n = len(data_fromgs) - len(data_fromdb)
    print(f"number of the different between row from gs and db is {n}")
    start = len(data_fromdb) -1
    data_fromgs_list = []
    for i in range(n):
        datas = list((data_fromgs[start].values()))
        original_datetime_str = datas[0]
        original_datetime = datetime.strptime(original_datetime_str, '%d/%m/%Y, %H:%M:%S')
        formatted_datetime_str = original_datetime.strftime('%Y-%m-%d %H:%M:%S')
        datas[0] = formatted_datetime_str
        data_fromgs_list.append(datas)
        start += 1

    sql2 = """
    insert into bme680_data (time,temperature,humidity,pressure,VOCs,ALT) values(%s,%s,%s,%s,%s,%s)
    """
    cursor.executemany(sql2,data_fromgs_list)
    db_cf.commit()
    print(f"insert {str(cursor.rowcount)} row")

schedule.every(5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)