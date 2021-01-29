# send(arg)函数返回


def my_generator(n):
    for i in range(n):
        temp = yield i
        print(f"我是{temp}")


g = my_generator(5)
print(next(g))
# 0

print(next(g))
# 我是None
# 1

print(next(g))
# 我是None
# 2

a = g.send(100)
# 我是100

print(a)
# 3

print(next(g))
# 我是None
# 4

