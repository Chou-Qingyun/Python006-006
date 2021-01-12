import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

Base = declarative_base()


class Book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(50), index=True)


class Author_table(Base):
    __tablename__ = 'authororm'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


# 实例一个引擎
dburl = "mysql+pymysql://root:root@127.0.0.1:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding='utf-8')

Base.metadata.create_all(engine)
