#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：file_multiprocessing.py
@Author  ：Toby
@Date    ：2022/11/23 10:20 
@Description：文件赋值进程
"""
# 完成将一个文件夹和文件复制到另一个文件夹中
import os
import multiprocessing

# 1.定义一个文件夹复制器的类


class FolderCopy(object):
    def __init__(self):

        self.file_names = []
        self.file_name = None

        self.source_file_name = None
        self.dest_file_name = None

        self.queue = None

        self.source_folder_path = input("输入原文件地址:")
        self.source_folder_name = input("输入原文件名:")
        self.dest_folder_path = input("输入存文件的地址：")

        self.dest_folder_name = r"%s/%s[副本]" % (self.dest_folder_path, self.source_folder_name)

        # self.source_file_name = r"%s\%s" % (self.old_folder_path, self.old_folder_name)
        # self.new_folder = r"%s\%s[副本]" % (self.new_folder_path, self.old_folder_name)

    def get_file_names(self):
        """获取原文件夹中文件列表"""
        if os.path.exists(self.source_folder_path):  # 判断原文件是否存在
            self.file_names = os.listdir(self.source_folder_path)
        else:
            print("源文件不存在")
        return self.file_names

    def make_folder(self):
        """根据原有文件夹创建新的文件夹"""
        # 判断该文件夹是否存在
        if os.path.exists(self.dest_folder_name):
            print("该文件夹存在")
            self.dest_folder_name = None
        else:
            os.mkdir(self.dest_folder_name)

    def copy_file(self, *args):
        """将原有文件夹中文件复制到新文件夹中"""
        queue, file_name, source_file_name, dest_file_name = args
        print("%s正在复制文件%s" % (os.getpid(), file_name))

        # 复制原有文件
        try:
            with open(source_file_name, "rb") as f:
                content = f.read()
        except Exception as e:
            content = None
            print("读取%s文件有%s问题" % (file_name, e))

        write_ok = None

        # 判断读取出来的值是否为空
        if content is not None:
            try:
                with open(dest_file_name, "wb") as f:
                    f.write(content)
            except Exception as e:
                write_ok = False
                print("写入%s文件有%s问题" % (file_name, e))

            if write_ok is False:
                queue.put("%s-文件复制有问题" % file_name)
            else:
                queue.put("%s" % file_name)
        else:
            queue.put("%s-文件复制有问题" % file_name)

    def display(self):
        """电子显示"""

        all_file_num = len(self.file_names)
        while True:
            file_name = self.queue.get(timeout=2)

            if file_name.find("-") != -1:
                file_name = file_name.split("-")[0]

            if file_name in self.file_names:
                self.file_names.remove(file_name)

            copy_rate = (all_file_num - len(self.file_names)) * 100 / all_file_num
            print("\r%.2f...(%s)" % (copy_rate, file_name) + " " * 50, end="")

            if copy_rate >= 100:
                break

    def run(self):
        # 创建文件夹
        self.make_folder()
        # 获取文件列表
        self.file_names = self.get_file_names()
        print(self.file_names)

        # 创建进程对象
        pool = multiprocessing.Pool(2)
        self.queue = multiprocessing.Manager().Queue()  # 进程队列用来存数据
        # 开始建任务
        for file_name in self.file_names:
            # 向进程池中添加任务
            self.file_name = file_name
            self.source_file_name = r"%s/%s" % (self.source_folder_path, self.file_name)
            self.dest_file_name = r"%s/%s" % (self.dest_folder_name, self.file_name)
            pool.apply_async(self.copy_file,
                             args=(self.queue, self.file_name, self.source_file_name, self.dest_file_name,))

        pool.close()  # 禁止再添加新任务
        self.display()
        print()


if __name__ == '__main__':
    folder_copy = FolderCopy()
    folder_copy.run()
# /Users/toby/Downloads/PythonAdvanced/code/2.python高级知识-多进程/案例文件夹/原文件夹
# 原文件夹
# /Users/toby/Downloads/PythonAdvanced/code/2.python高级知识-多进程/案例文件夹/复制到的文件夹
