import pymysql
from dbconfig import db_config
from datetime import datetime
from time import strftime, localtime

dbConfig = db_config()
dbConfig['port'] = int(dbConfig['port'])

db = pymysql.connect(**dbConfig)

try:
    with db.cursor() as cursor:
        # sql = '''SELECT * FROM playerorm'''
        insert_sql = 'INSERT INTO playerorm (player_name,player_age,player_birthday,player_gender,player_education,player_created,player_updated) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        values = (
            ('特雷西·麦克格雷迪', 41, '1979-05-24', 1, '蒙特锡安山基督学院', datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            ('安东尼·戴维斯', 27, '1993-03-11', 1, '肯塔基大学', datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            ('斯蒂芬·库里', 33, '1988-03-14', 1, '戴维森学院', datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        )
        # value = ('特雷西·麦克格雷迪', 41, '1979-05-24', 1, '蒙特锡安山基督学院',datetime.now().strftime("%Y-%m-%d %H:%M:%S"),datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        cursor.executemany(insert_sql, values)
        # result = cursor.fetchone()
    db.commit()
except Exception as e:
    db.rollback()
    print(f'fetch error: {e}')

finally:
    db.close()
    print(cursor.rowcount)