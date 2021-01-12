from sqlalchemy import Integer, String, MetaData, create_engine, Table, ForeignKey, Column
import pymysql
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

Base = declarative_base()


class Book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(20), index=True)

    def __repr__(self):
        return "Book_table(book_id='{self.book_id}',)" \
               f"book_name={self.book_name}".format(self=self)


class Author_table(Base):
    __tablename__ = 'authororm'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


dburl = "mysql+pymysql://root:root@127.0.0.1:3306/testdb?charset=utf8mb4"

engine = create_engine(dburl, echo=True, encoding='utf-8')

SessionClass = sessionmaker(engine)
session = SessionClass()

# 更新
# query = session.query(Book_table).filter(Book_table.book_id == 1).update({Book_table.book_name: 'Python最佳入门实战'})
query = session.query(Book_table)
query = query.filter(Book_table.book_id == 1)
query.update({Book_table.book_name: '肖申克的救赎'})
new_book = query.first()
print(new_book.book_name)

# 删除
query = session.query(Book_table)
query = query.filter(Book_table.book_id == 3)
# session.delete(query.one())
query.delet()
print(query.first())
session.commit()
