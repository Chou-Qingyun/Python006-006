import pymysql
from sqlalchemy import Integer, String, Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

Base = declarative_base()

class Table1_table(Base):
    __tablename__ = 'table1'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    #  # 模型字段间不要加“，”（逗号）不然会报错 Mapper mapped class Table1_table->table1 could not assemble any primary key columns for mapped table 'table1'

    def __repr__(self):
        return "Table1_table(id='{self.id}',)" \
                f"name={self.name}".format(self=self)


class Table2_table(Base):
    __tablename__ = 'table2'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

    def __repr__(self):
        return "Table2_table(id='{self.id}',)" \
                f"name={self.name}".format(self=self)

dburl = "mysql+pymysql://root:root@127.0.0.1:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding='utf-8')

SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# table1_data = Table1_table(id=1, name='table1_table2')
# table1_data1 = Table1_table(id=2, name='table1')
table2_data = Table2_table(id=1, name='table1_table2')
table2_data1 = Table2_table(id=3, name='table2')
try:
    # session.add_all([table1_data, table1_data1])
    session.add_all([table2_data, table2_data1])
    session.commit()
except Exception as e:
    print(f'插入失败：{e}')
    session.rollback()






