学习笔记
## 正则表达式
'*','+',和'?'修饰符都是贪婪的；它们在字符串进行尽可能多的匹配。有时候并不需要这种行为。如果正则式<.*>希望找到'<a> b<c>'，它将会匹配整个字符串，而不仅是‘<a>’。在修饰符之后添加之后添加？将使样式以非贪婪`方式或者:dfn:`最小方式进行匹配；尽量少的字符将被匹配。使用正则式<.*?>将会仅仅匹配'<a>'。

## 常见的模块
time
datetime
logging
random
json
pathlib
os.path

## 高级数据类型
collections  //容器数据类型
nametuple()  //命名元组
deque        //双端队列
Counter      //计数器
OrderedDict  //有顺序的字典

### 心得
自己是从事php开发的。刚接触python有些地方，感觉有点乱了。譬如获取当前时间戳，php：time() 就可以获取时间戳。python需要引入time, time.time();
之前对正式表达式的贪婪匹配一知半解的。通过python的官方文档对正则表达式的解读之后，理解了贪婪的匹配。