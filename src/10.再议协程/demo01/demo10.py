def my_generator():
    yield 'a'
    yield 'b'
    yield 'c'
    yield 'd'
    yield 'e'

g = my_generator()

# 启动生成器
print(next(g))
# a

print(next(g))
# b

g.close()
# StopIteration

print(next(g))







