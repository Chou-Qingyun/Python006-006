> 4. 以下两张基于 id 列，分别使用 INNER JOIN、LEFT JOIN、 RIGHT JOIN 的结果是什么?
##### INNER JOIN连接
```
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
INNER JOIN Table2
ON Table1.id = Table2.id;

```

id |  name | id | name |
---|---|---|---|
1 | table1_table2 | 1 | table1_table2

##### LEFT JOIN 左连接

```
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
LEFT JOIN Table2
ON Table1.id = Table2.id;
```
id |  name | id | name |
---|---|---|---|
1 | table1_table2 | 1 | table1_table2
2 | table1 | null | null|

##### RIGHT JOIN 右连接
```
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
RIGHT JOIN Table2
ON Table1.id = Table2.id;
```

id |  name | id | name |
---|---|---|---|
1 | table1_table2 | 1 | table1_table2
 null | null | 3 | table2 |

INNER JOIN连接表操作时，返回的结果是两个表都有的结果集，即两表的交集
LEFT JOIN连接操作时，返回的结果会以左表的数据为主，返回所有左表的数据，右表则是满足条件的显示数据，不满足的则是返回null
RIGHT JOIN连接表操作，则是与LEFT JOIN的结果集相反,以右表为主返回所有右表的数据，左表数据满足条件的返回数据，不满足则返回null