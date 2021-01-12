import pymysql
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import join
from datetime import datetime
from sqlalchemy import DateTime

'''
请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。
'''
Base = declarative_base()


class User_table(Base):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)

    def __repr__(self):
        return 'User_table(id={self.id},name={self.name})'.format(self=self)


class Account_table(Base):
    __tablename__ = 'account'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    user_id = Column(Integer(), nullable=False)
    account = Column(Integer(), nullable=False)

    def __repr__(self):
        return "Account_table(id={self.id}, user_id={self.user_id}, account={self.account})".format(self=self)


class Record_table(Base):
    __tablename__ = 'record'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    transfer_id = Column(Integer(), nullable=False)
    transfered_id = Column(Integer(), nullable=False)
    transfer_num = Column(Integer(), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)

    def __repr__(self):
        return "Record_table(id={self.id}, transfer_id={self.transfer_id}," \
               " transfered_id={self.transfered_id}, transfer_num={self.transfer_num})" \
                ",created_on={self.created_on}".format(self=self)


engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/testdb?charset=utf8mb4")
SessionClass = sessionmaker(bind=engine)
session = SessionClass()


# 添加User表数据
# user_data = User_table(name="张三")
# user_data1 = User_table(name="李四")

def addUser(insert_data=[]):
    insert_array = []
    for item in insert_data:
        insert_array.append(User_table(name=str(item)))

    try:
        session.add_all(insert_array)
        session.commit()
    except Exception as e:
        print(f"用户表新增数据失败：{e}")
        session.rollback()
    finally:
        session.close()


def updateAccount(user_id, account):
    query_instance = session.query(Account_table).filter(Account_table.user_id == user_id)
    return query_instance.update({Account_table.account: account})


def findAccount(user_id):
    query = session.query(Account_table, User_table.name).filter(Account_table.user_id == user_id)
    return query.join(User_table,User_table.id == Account_table.user_id).first()


def addRecord(user_id=0, accpet_id=0, account=0):
    record_data = Record_table(transfer_id=user_id, transfered_id=accpet_id, transfer_num=account)
    session.add(record_data)
    session.flush()
    return record_data.id


def from_transfer_to(from_user_id, accept_id=0, account=0):
    from_info = findAccount(from_user_id)
    accept_info = findAccount(accept_id)
    from_account_info = from_info.Account_table
    accept_account_info = accept_info.Account_table
    if int(from_account_info.account) < account:
        raise Exception(f'{from_info.name}的账户余额不够')
        exit(100)

    from_new_account = int(from_account_info.account) - account
    accept_new_account = int(accept_account_info.account) + account
    try:
        if updateAccount(from_user_id, from_new_account) \
                and updateAccount(accept_id, accept_new_account)\
                    and addRecord(user_id=from_user_id, accpet_id=accept_id, account=account):
            session.commit()
            print(f"{from_info.name}转账成功~")
        else:
            session.rollback()
            print(f"{from_info.name}转账失败！")
    except Exception:
        raise Exception

    finally:
        session.close()


# 往账户表添加各自存款
# account_data = Account_table(user_id=1, account=10)
# account_data1 = Account_table(user_id=2, account=200)


# try:
#     # session.add_all([user_data, user_data1])
#     # session.add_all([account_data, account_data1])
#     session.commit()
# except Exception as e:
#     print(f"数据插入失败：{e}")
#     session.rollback()
if __name__ == '__main__':
    # print(updateAccount(1, 50))
    # session.commit()
    try:
        from_transfer_to(from_user_id=1, accept_id=2, account=10)
    except Exception as e:
        print(f"{e}")
