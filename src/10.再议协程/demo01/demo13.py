def g2():
    yield 'a'
    return '这个是异常说明'
    yield 'b'


g = g2()
print(next(g))
# a
print(next(g))

