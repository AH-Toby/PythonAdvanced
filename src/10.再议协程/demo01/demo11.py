def g1():
    yield 1

g=g1()

print(next(g))
# 1

print(next(g))
# 异常
