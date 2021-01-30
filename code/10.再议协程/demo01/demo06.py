def my_generator():
    try:
        yield 'a'
        yield 'b'
        yield 'c'
        yield 'd'
        yield 'e'
    except StopIteration:
        print("触发 StopIteration")
    except KeyError:
        print("触发 KeyError")


g = my_generator()
print(next(g))
# a
print(next(g))
# b
g.throw(StopIteration)
# 触发 StopIteration

print(next(g))

print(next(g))
g.throw(KeyError)
print(next(g))

