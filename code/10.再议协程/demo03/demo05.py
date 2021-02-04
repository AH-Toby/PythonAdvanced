def average():
    print(1111)


def grouper(generator):
    result = yield from generator
    print(result)


def main(generator):
    for j in generator:
        print(j)


g = average()
wrap_g = grouper(g)
main(wrap_g)  # 调用
