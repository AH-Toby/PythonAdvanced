#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/26 17:13
# @Author  : toby
# @File    : 25.property类属性方式.py
# @Software: PyCharm
# @Desc:
class MyClass:
    def __init__(self):
        self._my_property = None

    def get_my_property(self):
        print("Getting my_property")
        return self._my_property

    def set_my_property(self, value):
        print("Setting my_property to", value)
        self._my_property = value

    def del_my_property(self):
        print("Deleting my_property")
        del self._my_property

    my_property = property(get_my_property, set_my_property, del_my_property, "This is a custom property.")


# 创建对象
obj = MyClass()

# 访问属性
print(obj.my_property)
obj.my_property = 42  # 调用set_my_property方法

# 获取属性的文档字符串
print(MyClass.my_property.__doc__)

del obj.my_property  # 调用del_my_property方法

