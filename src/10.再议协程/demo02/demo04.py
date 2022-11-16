from inspect import getgeneratorstate  # 一定要导入
from time import sleep


def my_generator():
    for i in range(3):
        sleep(0.5)
        x = yield i + 1


def main(generator):
    try:
        print("生成器初始状态为:{0}".format(getgeneratorstate(g)))
        next(g)  # 激活生成器
        print("生成器初始状态为:{0}".format(getgeneratorstate(g)))
        g.send(100)
        print("生成器初始状态为:{0}".format(getgeneratorstate(g)))
        next(g)
        print("生成器初始状态为:{0}".format(getgeneratorstate(g)))
        next(g)
    except StopIteration:
        print('全部迭代完毕了')
        print("生成器初始状态为:{0}".format(getgeneratorstate(g)))


g = my_generator()  # 创建一个生成器对象
main(g)
