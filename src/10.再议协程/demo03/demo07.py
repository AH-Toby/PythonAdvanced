def before():
    print("文本开始处理前需要做的一些事情")


def after():
    print("文本结束处理后需要做的一些事情")


# reader是一个生成器，不变化
def reader(text):
    for line in text:
        yield line
    return 'done'


# 添加一个代理
def proxyReader(text):
    before()  # 开始读之前运维需求处理
    r = reader(text)
    try:
        while True:
            line = next(r)
            yield line
    except StopIteration as e:
        after()  # 结束读之后运维需求处理
        return e.value


# app是定义的一个简单应用，将reader读出的值打印出来
def app(text):
    try:
        r = proxyReader(text)
        while True:
            line = next(r)
            print('<< %s' % line)
    except StopIteration as e:
        print(e.value)


# 启动app应用
app(('a', 'b', 'c', 'd'))
