import time


def fun1():
    while True:
        print("___func1执行了___")
        yield
        time.sleep(0.5)


def func2():
    while True:
        print("___func2执行了___")
        yield
        time.sleep(0.5)


def main():
    f1 = fun1()
    f2 = func2()
    while True:
        next(f1)
        next(f2)


if __name__ == '__main__':
    main()
