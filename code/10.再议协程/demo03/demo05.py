# reader是一个生成器， 每次调用，它将读取列表中一个值并返回
def reader(text):
    for line in text:
        yield line
    return 'done'


# app是定义的一个简单应用，将reader读出的值打印出来
def app(text):
    try:
        r = reader(text)
        while True:
            line = next(r)
            print('<< %s' % line)
    except StopIteration as e:
        print(e.value)


# 启动app应用
app(('a', 'b', 'c', 'd'))
