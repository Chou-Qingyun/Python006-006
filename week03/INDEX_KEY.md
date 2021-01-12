> 5. 使用 MySQL 官方文档，学习通过 sql 语句为上题中的 id 和 name 增加索引，并验证。根据执行时间，增加索引以后是否查询速度会增加？请论述原因，并思考什么样的场景下增加索引才有效。

根据name查询表table1的结果
```buildoutcfg
EXPLAIN SELECT * FROM table1 WHERE table1.name = 'table1'
```
##### 结果：
id|select_type|table|parttions|type|possible_keys|key|key_len|ref|rows|filtered|Extra|
---|---|---|---|---|---|---|---|---|---|---|---|
1|SIMPLE|table1|NULL|ALL|NULL|NULL|NULL|NULL|2|50.00|Using where

总耗时： 0.010 sec

从以上的表格数据可以看出该条sql语句执行了全表扫描（type类型），没有使用索引，扫描的行数为全表的行数

根据id查询表table1的结果
```buildoutcfg
EXPLAIN SELECT * FROM table1 WHERE table1.id = 1
```
##### 结果：
id|select_type|table|parttions|type|possible_keys|key|key_len|ref|rows|filtered|Extra|
---|---|---|---|---|---|---|---|---|---|---|---|
1|SIMPLE|table1|NULL|const|PRIMARY|PRIMARY|4|const|1|100.00|NULL
总耗时： 0.007 sec

因为id是table1的主键，同时从以上的表格数据可以看出type类型为const，索引为主键索引，扫描行数为符合条件的1行

为表table1的字段name加上索引，
```buildoutcfg
ALTER TABLE table1 ADD INDEX `name_index` (`name`);
```
再次执行name条件查询数据
```buildoutcfg
EXPLAIN SELECT * FROM table1 WHERE table1.name = 'table1'
```

##### 结果：
id|select_type|table|parttions|type|possible_keys|key|key_len|ref|rows|filtered|Extra|
---|---|---|---|---|---|---|---|---|---|---|---|
1|SIMPLE|table1|NULL|ref|name_index|name_index|83|const|1|100.00|Using index
总耗时： 0.004 sec

从以上的表格数据可以看出这次查询走了索引，type类型为ref,扫描行数为1（rows:1），相比之前的全表扫描快了很多。

在数据库表中，若某些字段经常被作为条件查询，却该字段长度较小，可为该字段添加索引。提升查询效率。如果需要多个字段，则可考虑联合索引。