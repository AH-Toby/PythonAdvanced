#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/25 16:56
# @Author  : toby
# @File    : 18.多态.py
# @Software: PyCharm
# @Desc:
class MiniOs(object):
    def __init__(self, name):
        self.name = name
        self.apps = []  # 安装的应用程序名称列表

    def __str__(self):
        return f"{self.name}安装的软件列表为{self.apps}"

    def install_app(self, app):
        """
        安装程序
        """
        # 判断是否已安装程序
        if app.name in self.apps:
            print(f"已安装程序：{app.name}无序再次安装")
        else:
            app.install()
            self.apps.append(app.name)


class App(object):
    def __init__(self, name, version, desc):
        self.name = name
        self.version = version
        self.desc = desc

    def __str__(self):
        return f"{self.name}的版本是{self.version}{self.desc}"

    def install(self):
        print(f"将{self.name}[{self.version}]的执行程序复制到程序目录...")


class PyCharm(App):
    pass


class Chrome(App):
    pass


linux = MiniOs("Linux")
print(linux)

pycharm = PyCharm("PyCharm", "1.0", "python 开发的 IDE 环境")
chrome = Chrome("Chrome", "2.0", "谷歌浏览器")

linux.install_app(pycharm)
linux.install_app(chrome)
linux.install_app(chrome)
print(linux)
