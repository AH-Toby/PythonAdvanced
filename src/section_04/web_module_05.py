#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：web_module_05.py
@Author  ：Toby
@Date    ：2022/12/2 16:49 
@Description：TCP服务端
"""
from socket import *

# 1. socket创建一个套接字
server_socker = socket(AF_INET, SOCK_STREAM)

# 2. bind绑定ip和port
ip = '192.168.43.127'
port = 8848
server_socker.bind((ip, port))

# 3. listen使套接字变为可以被动链接
server_socker.listen(128)

# 4. accept等待客户端的链接
client_socket, client_ip = server_socker.accept()

# 5. recv/send接收发送数据
# 接收对方发送过来的数据
recv_data = client_socket.recv(1024)  # 接收1024个字节
print('接收到的数据为:', recv_data.decode())

# 发送一些数据到客户端
client_socket.send("thank you !".encode())

client_socket.close()
