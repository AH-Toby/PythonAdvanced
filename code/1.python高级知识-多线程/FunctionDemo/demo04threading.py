import threading


class MyThread(threading.Thread):
    def run(self):
        print("%s:线程运行了" % self.name)


if __name__ == '__main__':
    a = MyThread()
    a.start()
    b = MyThread()
    b.start()
