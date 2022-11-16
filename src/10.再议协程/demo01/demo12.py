def g2():
    yield 'a'
    return
    yield 'b'


g = g2()
print(next(g))
# a
# 异常
print(next(g))

