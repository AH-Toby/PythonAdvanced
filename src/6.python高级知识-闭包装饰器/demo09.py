# -*- coding:utf-8 -*-
def set_func(func):
    def call_fun(*args, **kwargs):
        return func(*args, **kwargs)

    return call_fun


@set_func
def test(data):
    return "test is show%s" % data


print(test(100))
