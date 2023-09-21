#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/21 11:49
# @Author  : toby
# @File    : 65.协程-窗体程序异步假死.py
# @Software: PyCharm
# @Desc:
import tkinter as tk  # 导入 Tkinter 库
import asyncio


class Form:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x300')
        self.root.title('窗体程序')  # 设置窗口标题

        self.button = tk.Button(self.root, text="开始计算", command=self.get_loop)
        self.label = tk.Label(master=self.root, text="等待计算结果")

        self.button.pack()
        self.label.pack()

        self.root.mainloop()

    # 定义一个异步方法，模拟耗时计算任务
    async def calculate(self):
        await asyncio.sleep(3)
        self.label["text"] = 300

    # asyncio任务只能通过事件循环运行，不能直接运行异步函数
    def get_loop(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.calculate())
        loop.close()


if __name__ == '__main__':
    form = Form()
