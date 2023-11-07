#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/6 16:52
# @Author  : toby
# @File    : mini_web.py
# @Software: PyCharm
# @Desc:


import time


def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)
    return f'{str(environ)}==Hello world from a simple WSGI application!--->{time.ctime()}\n'
