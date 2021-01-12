import pymysql
from dbconfig import db_config

localhost = '127.0.0.1'
user = 'root'
password = 'root'
dbname = 'yike_crm'
db_config_server = db_config()
db_config_server['port'] = int(db_config_server['port'])
# db = pymysql.connect(host=localhost, user=user, password=password, db=dbname, port=3306)
db = pymysql.connect(**db_config_server)

try:
    with db.cursor() as cursor:
        sql = '''SELECT VERSION()'''
        # 使用 execute() 方法执行SQL查询
        # %s是占位符（固定占位符，是数字类型也是用%s）
        insert_sql = '''INSERT INTO book (id, name) VALUES (%s, %s)'''
        value = (1002, '红楼梦')
        cursor.execute(insert_sql, value)
        cursor.execute(sql)
        result = cursor.fetchone()
    db.commit()
except Exception as e:
    db.rollback()
    print(f'fetch error {e}')

finally:
    # 关闭数据库
    db.close()
    print(f'数据库版本：{result}')
    print(cursor.rowcount)  # 影响的行数
