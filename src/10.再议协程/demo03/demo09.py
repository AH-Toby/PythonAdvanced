# 1. 需要读取一段放在一个常量列表中的文本， 每个item表示一行文本, **空行用空字符串''表示。**
# 2. 每读入一行，如果不是空行，则先打印双小于号 "<<"，然后打印读入的文本行
# 3. 如果读入是空行，则打印"Error: Empty Line"


# 定义一个EmptyException异常
class EmptyException(Exception):
    pass


# 1. writer是一个协程coroutine。
# 　　1）用来模拟文本接收，每次接收一行
#    2）收到文本后，先打印">>" 然后打印收到的文本
#    3）如果接收时产生EmptyException异常， 则打印"Error: Empty Line"
# reader是一个协程， 它循环等待接收一行文本并打印输出

def writer():
    while True:
        try:
            t = yield
            print('>> %s' % t)
        except EmptyException:
            print('Error: Empty Line')


# 2. app是主线业务, 软件需求如下：
#     1）while循环中，每次通过读取text列表中的一个item
#     2）如果读到的不是空行，则直接将文本通过send发送给writer
#     3) 如果读到的是空行，则触发writer产生EmptyException异常
# app是定义的一个简单应用，将reader读出的值打印出来
def app(text):
    w = writer()
    w.send(None)  # 激活writer
    for line in text:
        if line == '':
            w.throw(EmptyException)
        else:
            w.send(line)


# 启动app应用
app(('a', 'b', '', 'c'))
