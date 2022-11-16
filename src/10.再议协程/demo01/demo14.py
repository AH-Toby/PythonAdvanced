def g3():
    yield 'a'
    return '这是错误说明'
    yield 'b'


g = g3()

try:
    print(next(g))  # a
    print(next(g))  # 触发异常
except StopIteration as e:
    result = e.value
    print(result)

