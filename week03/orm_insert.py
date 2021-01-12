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
                "book_name={self.book_name}".format(self=self)


class Author_table(Base):
    __tablename__ = 'authororm'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)



# Float
# Decimal
# Boolean
# Text
# autoincrement
dburl = "mysql+pymysql://root:root@127.0.0.1:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding='utf-8')

# 创建session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 增加数据
book_demo = Book_table(book_name='肖申克的救赎')
book_demo1 = Book_table(book_name='活着')
book_demo2 = Book_table(book_name='三国演义')
# 多条数据
# session.add(book_demo)
# session.add(book_demo1)
# session.add(book_demo2)
# session.flush()
# result = session.query(Book_table).all()
# one = session.query(Book_table).first() # first()只返回第一个
# one() # 查询的结果如果不是一个就会抛出异常 (sqlalchemy.orm.exc.MultipleResultsFound: Multiple rows were found for one())
# scalar() 返回第一结果的第一元素，没有结果就返回none 多于一行的话就会返回异常
for res in session.query(Book_table):
    print(f'res:{res}')

# 指定查询字段
session.query(Book_table.book_name).first()

# 排序
from sqlalchemy import desc
# for result in session.query(Book_table.book_name,Book_table.book_id).order_by(desc(Book_table.book_id)):
#     print(result)

# 限制数量
# query = session.query(Book_table.book_name, Book_table.book_id).order_by(desc(Book_table.book_id)).limit(2)
# print([result.book_name for result in query])

# from sqlalchemy import func # 使用函数
# result = session.query(func.count(Book_table.book_name)).first()
# print(result)
# 条件查询
print(session.query(Book_table).filter(Book_table.book_id < 20).first())
# 多条件
# filter(Book_table.book_id > 10, Book_table.book_id < 20)

# from sqlalchemy import and_, or_, not_
# session.query(Book_table).filter(
#     or_(
#         Book_table.book_id.between(10, 20),
#         Book_table.book_name.contains('book')
#     ),
#     and_(
#         Book_table.book_id == 1,
#     )
# ).first()
session.commit()
