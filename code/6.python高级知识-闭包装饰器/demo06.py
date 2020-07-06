# -*- coding:utf-8 -*-
def set_func(func):
    def call_fun(data):
        func(data)

    return call_fun


@set_func
def test(data):
    print("test is show%s" % str(data))


test(100)
