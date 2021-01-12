学习笔记
### Python连接MySQL的方法

Python3连接 MySQL:
- Python3安装的MySQLdb包叫做mysqlclient，加载的依然是MySQLdb
- shell> pip install mysqlclient
- python> import MySQLdb

其他DB-API:
- shell>pip install pymysql      # 流行度最高
- shell>pip install mysql-connector-python # MySQL官方

使用ORM(对象映射关系):
- shell>pip install sqlalchemy 


### SQL语言功能划分
DQL: Data Query Language, 数据查询语言，开发工程师学习的重点

DDL: Data Definition Language，数据定义语言，操作库和表结构。

DML: Data Manipulation Lanuage，数据操作语言，操作表中记录。

DCL: Data Control Language,数据控制语言，安全和访问权限控制。

#### MySQL是自动提交（隐式提交）


```
SELECT DISTINCT book_id, book_name, count(*) as number  # 5 提取指定的字段
FROM book JOIN author ON book.sn_id = author.sn_id      # 1  先join操作之后根据on的条件产生一个虚拟的表
WHERE pages > 500                                       # 2 where判断，产生符合条件新的虚拟表
GROUP BY book.book_id                                   # 3  分组                              
HAVING number > 10                                      # 4  分组过滤having操作
ORDER BY number                                         # 6 根据提取的字段，进行排序
LIMIT 5                                                 # 排序之后，获取前5行
```







