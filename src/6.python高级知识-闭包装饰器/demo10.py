# -*- coding:utf-8 -*-


def set_func1(func):
    print("set_fun1执行了")

    def call_fun(*args, **kwargs):
        print("call_fun1执行了")
        return func(*args, **kwargs)

    return call_fun


def set_func2(func):
    print("set_fun2执行了")

    def call_fun(*args, **kwargs):
        print("call_fun1执行了")
        return func(*args, **kwargs)

    return call_fun


@set_func2
@set_func1
def test():
    return "test is show"


print(test())
