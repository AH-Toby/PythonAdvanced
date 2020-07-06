# -*- coding:utf-8 -*-
class Func(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("权限")
        return self.func(*args, **kwargs)


@Func
def test(data):
    return "test is show%s" % data


print(test(100))
