def my_generator():
    while True:
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

print('-------------------------')
print(g.throw(StopIteration))
# 触发 StopIteration
# a
print('-------------------------')


print(next(g))
# b
print(next(g))
# c

print('-------------------------')
print(g.throw(KeyError))
# 触发 KeyError
# a
print('-------------------------')

# 触发 KeyError
print(next(g))
# b

