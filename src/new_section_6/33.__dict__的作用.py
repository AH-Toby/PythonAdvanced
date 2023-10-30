#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/27 14:23
# @Author  : toby
# @File    : 33.__dict__的作用.py
# @Software: PyCharm
# @Desc:
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# 创建一个 MyClass 类的对象
obj = MyClass(10, 20)

# 使用 __dict__ 获取对象的属性和值
obj_dict = obj.__dict__

# 输出对象的属性和值
for key, value in obj_dict.items():
    print(f"Attribute: {key}, Value: {value}")

# 修改对象的属性值
obj.__dict__["x"] = 100

# 再次输出修改后的对象属性值
print(f"Modified x: {obj.x}")
