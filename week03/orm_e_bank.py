from sqlalchemy import Table, Column, create_engine, Integer, String
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import DateTime
from datetime import datetime

'''
张三给李四通过网银转账 100 极客币，现有数据库中三张表：

一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，
第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。

请合理设计三张表的字段类型和表结构；
请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。
'''

Base = declarative_base()

class User_table(Base):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)


class Account_table(Base):
    __tablename__ = 'account'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    user_id = Column(Integer(), nullable=False)
    account = Column(Integer(), nullable=False)

class Record_table(Base):
    __tablename__ = 'record'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    transfer_id = Column(Integer(), nullable=False)
    transfered_id = Column(Integer(), nullable=False)
    transfer_num = Column(Integer(), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)

# 实例引擎
db_url = "mysql+pymysql://root:root@127.0.0.1:3306/testdb?charset=utf8mb4"
engine = create_engine(db_url, echo=True)

Base.metadata.create_all(engine)