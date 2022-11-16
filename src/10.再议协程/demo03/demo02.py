def my_generator():
    for i in range(5):
        if i == 2:
            return '我被迫中断了'
        else:
            yield i


def main(generator):
    try:
        for i in generator:  # 不会显式触发异常，故而无法获取到return的值
            print(i)
    except StopIteration as exc:
        print(exc.value)


g = my_generator()  # 调用
main(g)