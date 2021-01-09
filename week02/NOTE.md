学习笔记

# 基于TCP的socket编程
Socket API
- socket()
- bind()
- listen()
- accept()
- recv()
- send()
- close()
- 
# 异常捕获

所有内置的非系统退出的异常都派生自Exception类

#### StopIteration 异常示例：

```
gennumber = ( i for i in range(0, 2))
    print(next(gennumber))
    print(next(gennumber))
    
try:
    print(next(gennumber))
    
except StopIteration:
    print('最后一个元素')
```

#### 异常处理机制的原理

- 异常也是一个类
- 异常捕获过程：

1. 异常类把错误消息打包到一个对象
2. 然后该对象会自动查找到调用栈
3. 直到运行系统找到明确声明如何处理这些类异常的位置

- 所有异常继承自BaseException
- Tracebak 显示了出错的位置，显示的顺序和异常信息对象传播的方向是相反的


#### 异常信息与异常捕获
- 异常信息在Traceback信息的最后一行，有不同的类型
- 捕获异常可以使用try...except语法
- try...except支持多重异常处理

##### 常见的异常类型主要有：
1. LookupError 下的IndexError和KeyError
2. IOError
3. NameError
4. TypeError
5. AttributeError
6. ZeroDivisionError



```
抛出异常：raise 
```
自定义的异常需要继承Exception类

第三方异常库：pretty_errors

python 编码规范：PEP-8 / Google Python 风格指引

不使用开源框架，基于 TCP 协议改造 echo 服务端和客户端代码，实现服务端和客户端可以传输单个文件的功能。
（需提交代码作业）
使用 requests 库抓取知乎任意一个话题下排名前 15 条的答案内容 (如果对前端熟悉请抓取所有答案)，并将内容保存到本地的一个文件