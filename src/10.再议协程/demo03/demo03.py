def my_generator():
    for i in range(5):
        if i == 2:
            return '我被迫中断了'
        else:
            yield i


def main(generator):
    try:
        print(next(generator))  # 每次迭代一个值，则会显式出发StopIteration
        print(next(generator))
        print(next(generator))
        print(next(generator))
        print(next(generator))
    except StopIteration as exc:
        print(exc.value)  # 获取返回的值


g = my_generator()
main(g)