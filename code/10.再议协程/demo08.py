def my_generator():
    yield 'a'
    yield 'b'
    yield 'c'
    yield 'd'
    yield 'e'

g = my_generator()

# 启动生成器
a = g.send(None)
print(a)
# a

print(next(g))
# b

print(next(g))
# c






