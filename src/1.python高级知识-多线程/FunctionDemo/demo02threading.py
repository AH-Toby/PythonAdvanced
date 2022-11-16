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
    print("——————开始工作————:%s" % ctime())

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    sleep(5)
    print('---结束工作---:%s' % ctime())
