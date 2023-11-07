#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/6 18:13
# @Author  : toby
# @File    : my_web.py
# @Software: PyCharm
# @Desc:
import re

template_root = "./templates"
address_params = dict()  # 路由表


def route(url):
    def set_func(func):
        def call_func(*args, **kwargs):
            return func(**args, **kwargs)

        address_params[url] = func
        return call_func

    return set_func


def read_html(file_name):
    try:
        file_name = file_name.replace(".py", ".html")
        file_path = template_root + file_name
        with open(file_path) as f:
            content = f.read()
            # --------更新-------
            # 动态数据
            data_from_mysql = "数据还没有敬请期待...."
            content = re.sub(r"\{%content%\}", data_from_mysql, content)
            return content
    except Exception as e:
        return f"{e}"


# @route('/index.py')
@route('/index.html')  # 伪静态
def index(file_name):
    return read_html(file_name)


# @route('/center.py')
@route('/center.html')
def center(file_name):
    return read_html(file_name)


def application(environ, start_response):
    start_response("200 ok", [('Content-Type', 'text/html')])
    url = environ["file_name"]
    print(f"获得的url地址为{url}")
    try:
        return address_params[url](url)
    except Exception as e:
        return f"{e}"
