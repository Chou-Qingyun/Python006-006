> 1. 
- 将修改字符集的配置项、验证字符集的 SQL 语句作为作业内容提交
- 将增加远程用户的 SQL 语句作为作业内容提交

查看字符集
```buildoutcfg
show variables like 'character_set_%';
```
修改数据库字符集
临时修改
```buildoutcfg
SET GLOBAL character_set_server=utf8mb4
```
永久修改
编辑/etc/mysql/my.cnf（根据安装目录查找）,在
```buildoutcfg
[mysql]
characher-set-server=utf8mb4
default-character-set=utf8mb4
[mysqld]
character-set-server=utf8mb4
```
添加远程数据库用户
```buildoutcfg
CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'testpassword';
```
给用户赋予权限
```buildoutcfg
GRANT ALL PRIVILEGES  ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpassword';
FLUSH PRIVILEGES;
```


> 3. 为以下sql语句标注执行顺序：
```buildoutcfg
SELECT DISTINCT player_id, player_name, count(*) as num  # 5 筛选字段
FROM player JOIN team ON player.team_id = team.team_id   # 1  from，join操作根据on产生虚拟表
WHERE height > 1.80                                      # 2  where条件，产生符合条件的虚拟表
GROUP BY player.team_id                                  # 3  分组
HAVING num > 2                                           # 4  分组过滤
ORDER BY num DESC                                        # 6  排序
LIMIT 2                                                  # 7  提取前2行
```