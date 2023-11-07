#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/7 22:56
# @Author  : toby
# @File    : 5.日志写入控制台和文件.py
# @Software: PyCharm
# @Desc:
import logging

# 第一步：创建一个logger对象
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # 设置日志等级总开关

# 第二步：创建一个handler,用于写入到文件
logfile = "./logfile.txt"
fh = logging.FileHandler(logfile, mode='a')  # open的打开模式这里可以进行参考
fh.setLevel(logging.DEBUG)  # 设置写入文件日志等级开关

# 第三部：再创建一个handler,用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)  # 设置输出到控制台日志等级

# 第四步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第五步，将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)

# 开始使用log功能
logger.debug('这是 loggging debug message')
logger.info('这是 loggging info message')
logger.warning('这是 loggging a warning message')
logger.error('这是 an loggging error message')
logger.critical('这是 loggging critical message')
