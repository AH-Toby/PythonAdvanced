# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
# type("类名",(父类1,父类2),{属性:值})


class A(object):
    num = 100

    @classmethod
    def test(cls):
        print("test is show")


@classmethod
def test(cls):
    print("test type is show")


B = type("B", (object,), {"num": 300, "test": test})

a = A()
a.test()

b = B()
b.test()
