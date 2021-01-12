from sqlalchemy import MetaData, create_engine, Integer, String, Table, Column
from sqlalchemy.ext.declarative import declarative_base
import pymysql
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Player_table(Base):
    __tablename__ = 'playerorm'
    player_id = Column(Integer(), primary_key=True)
    player_name = Column(String(20), index=True, unique=True)
    player_age = Column(Integer(), nullable=False)
    player_birthday = Column(String(20))
    player_gender = Column(Integer(), nullable=False) # 男性为： 1；女性为：0
    player_education = Column(String(20), nullable=False)
    player_created = Column(DateTime(), default=datetime.now)
    player_updated = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    def __repr__(self):
        return "Player_table(player_id='{self.player_id}',)" \
                f"player_name={self.player_name}, player_age={self.player_age}" \
                f"player_birthday={self.player_birthday}, player_gender={self.player_gender}" \
                f"player_education={self.player_education}".format(self=self)



# 创建引擎
dburl = "mysql+pymysql://root:root@127.0.0.1:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding='utf8')

# Base.metadata.create_all(engine)

# 创建会话
SessionClass = sessionmaker(bind=engine)
session = SessionClass()
# 添加数据
player_demo = Player_table(
    player_name="威金斯",
    player_age=25,
    player_birthday='1996-05-01',
    player_gender=1,
    player_education='闽南师范大学'
)
player_demo1 = Player_table(
    player_name="詹姆斯",
    player_age=31,
    player_birthday='1990-11-14',
    player_gender=1,
    player_education='圣文森特·圣玛丽高中'
)
# session.add(player_demo1)

# 查询
result = session.query(Player_table).all()
print([player.player_name for player in result])
print(session.query(Player_table.player_id, Player_table.player_name, Player_table.player_age, Player_table.player_gender, Player_table.player_education, Player_table.player_created, Player_table.player_updated).filter(Player_table.player_age > 27).first())
# 提交数据
session.commit()