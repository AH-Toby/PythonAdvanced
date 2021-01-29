# throw(err)方法


def my_generator(n):
    yield "a"
    yield "b"
    yield "c"


g = my_generator(5)
print(next(g))
# a

print(g.throw(StopIteration))

print(next(g))
