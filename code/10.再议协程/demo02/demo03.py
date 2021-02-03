def average():
    total = 0.0  # 数字的总和
    count = 0  # 数字的个数
    avg = None  # 平均值
    while True:
        num = yield avg
        total += num
        count += 1
        avg = total / count


# 定义一个函数，通过这个函数向average函数发送数值
def sender(generator):
    print(next(generator))  # 启动生成器
    print(generator.send(10))  # 10
    print(generator.send(20))  # 15
    print(generator.send(30))  # 20
    print(generator.send(40))  # 25


g = average()
sender(g)
