# 需求
# 1. 需要读取一段放在一个常量列表中的文本， 每个item表示一行文本。
# 2. 每读入一行，则先打印双小于号 "<<"，然后打印读入的文本行
# 3. 如果文本全部成功读取，则最后打印“done”表示应用正常结束
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
