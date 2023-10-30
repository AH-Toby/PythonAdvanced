#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/27 16:32
# @Author  : toby
# @File    : 39.__len__方法的作用.py
# @Software: PyCharm
# @Desc:
class MyList:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def append(self, value):
        self.data.append(value)


# 创建一个 MyList 类的对象
my_list = MyList()

# 使用自定义类的方法添加元素
my_list.append(10)
my_list.append(20)
my_list.append(30)

# 使用 len() 函数获取对象的长度
length = len(my_list)
print(f"The length of my_list is {length}")
