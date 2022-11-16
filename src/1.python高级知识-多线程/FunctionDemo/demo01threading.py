import threading


def saySomething():
    print("hello world!")


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=saySomething)
        t.start()
