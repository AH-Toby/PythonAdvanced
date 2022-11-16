import threading
from time import sleep


class MyThread(threading.Thread):
    def run(self):
        sleep(1)
        print("%s:线程运行了" % self.name)


if __name__ == '__main__':
    for i in range(10):
        a = MyThread()
        a.start()

