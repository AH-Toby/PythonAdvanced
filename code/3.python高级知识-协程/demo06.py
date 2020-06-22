import time
from greenlet import greenlet


def fun1():
    while True:
        print("___func1执行了___")
        g2.switch()
        time.sleep(0.5)


def func2():
    while True:
        print("___func2执行了___")
        g1.switch()
        time.sleep(0.5)


g1 = greenlet(fun1)
g2 = greenlet(func2)


# 切换到gr1中运行
g1.switch()
