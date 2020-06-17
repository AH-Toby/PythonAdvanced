import threading
from time import sleep, ctime


def sing():
    for i in range(1, 4):
        print("唱歌---%s" % i)
        sleep(1)


def dance():
    for i in range(1, 4):
        print("跳舞---%s" % i)
        sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()

    while True:
        length = len(threading.enumerate())
        print(threading.enumerate())
        print('当前运行的线程数为：%d'%length)
        if length<=1:
            break

        sleep(0.5)
    # print(threading.enumerate())
