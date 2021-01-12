from sqlalchemy import create_engine, Table, Column, MetaData, ForeignKey, Integer, String
import pymysql

dburl = "mysql+pymysql://root:root@127.0.0.1:3306/testdb"

engine = create_engine(dburl, echo=True)

metedata = MetaData(engine)

table1_table = Table('table1', metedata,
                     Column('id', Integer, primary_key=True),
                     Column('name', String(20))
                     )

table2_table = Table('table2', metedata,
                     Column('id', Integer, primary_key=True),
                     Column('name', String(20))
                     )

try:
    metedata.create_all()
except Exception as e:
    print(f'创建失败：{e}')