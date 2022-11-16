def my_generator():
    for i in range(5):
        if i == 2:
            return '我被迫中断了'
        else:
            yield i


# 委派生成器
def wrap_my_generator(generator):  # 定义一个包装“生成器”的生成器，它的本质还是生成器
    result = yield from generator  # 自动触发StopIteration异常，并且将return的返回值赋值给yield from表达式的结果，即result
    print(result)


def main(generator):
    for j in generator:
        print(j)


g = my_generator()
wrap_g = wrap_my_generator(g)
main(wrap_g)  # 调用
