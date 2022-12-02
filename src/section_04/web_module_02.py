#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：web_module_02.py
@Author  ：Toby
@Date    ：2022/12/2 16:39 
@Description：网络编程udp服务端
"""
from socket import *


class RecvMSG(object):
    def __init__(self, ip, port):
        self.address = (ip, port)
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)

    def recv_msg(self):
        self.udp_socket.bind(self.address)
        msg = self.udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
        print(msg)
        self.udp_socket.close()


if __name__ == '__main__':
    ip = ""
    port = 8989
    rec = RecvMSG(ip=ip, port=port)
    rec.recv_msg()

