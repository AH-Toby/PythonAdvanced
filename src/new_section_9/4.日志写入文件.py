#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/7 22:54
# @Author  : toby
# @File    : 4.日志写入文件.py
# @Software: PyCharm
# @Desc:
import logging

logging.basicConfig(level=logging.WARNING,
                    filename="./log.txt",
                    filemode="w",
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# 开始使用log功能
logging.info('这是 loggging info message')
logging.debug('这是 loggging debug message')
logging.warning('这是 loggging a warning message')
logging.error('这是 an loggging error message')
logging.critical('这是 loggging critical message')
