#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/21 11:47
# @Author  : toby
# @File    : 64.协程-窗体程序假死.py
# @Software: PyCharm
# @Desc:
import tkinter as tk  # 导入 Tkinter 库
import time


class Form:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x300')
        self.root.title('窗体程序')  # 设置窗口标题

        self.button = tk.Button(self.root, text="开始计算", command=self.calculate)
        self.label = tk.Label(master=self.root, text="等待计算结果")

        self.button.pack()
        self.label.pack()
        self.root.mainloop()

    def calculate(self):
        time.sleep(3)  # 模拟耗时计算
        self.label["text"] = 300


if __name__ == '__main__':
    form = Form()
