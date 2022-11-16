# 定义一个EmptyException异常
class EmptyException(Exception):
    pass


def before():
    print("文本开始处理前需要做的一些事情")


def after():
    print("文本结束处理后需要做的一些事情")


# 子生成器
def writer():
    while True:
        try:
            t = yield
            print('>> %s' % t)
        except EmptyException:
            print('Error: Empty Line')


# 代理
def proxyWriter():
    before()
    w = writer()
    w.send(None)  # 启动生成器
    while 1:
        t = yield
        w.send('>> %s' % t)


def app(text):
    w = proxyWriter()
    w.send(None)  # 激活writer
    for line in text:
        if line == '':
            w.throw(EmptyException)
        else:
            w.send(line)


# 启动app应用
app(('a', 'b', '', 'c'))
