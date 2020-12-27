学习笔记
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