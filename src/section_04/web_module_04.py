#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：web_module_04.py
@Author  ：Toby
@Date    ：2022/12/2 16:47 
@Description：TCP客户端
"""
from socket import *

# 创建套接字
tcp_client = socket(AF_INET, SOCK_STREAM)

# 连接服务端
ip = '192.168.43.127'
port = 8848

tcp_client.connect((ip, port))

# 发送数据
tcp_client.send('hello'.encode('utf-8'))  # str--->bytes

# 接受数据
data = tcp_client.recv(1024).decode('utf-8')
print(data)

# 关闭套接字
tcp_client.close()