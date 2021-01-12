# sqlalchemy 连接MySQL数据库

import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

# 打开数据库
engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/testdb", echo=True)
# 创建元数据
metadata = MetaData(engine)

book_table = Table('book', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String(20)),
                   )

author_table = Table('author', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('book_id', None, ForeignKey('book.id')),
                     Column('author_name', String(128), nullable=False)
                     )

try:
    metadata.create_all()
except Exception as e:
    print(f'create error {e}')
