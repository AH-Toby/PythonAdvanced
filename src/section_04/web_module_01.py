#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：web_module_01.py
@Author  ：Toby
@Date    ：2022/12/2 16:37 
@Description：网络编程UDP客户端
"""
from socket import *


class SendMSG(object):
    """udp发送消息"""

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        # 1. 创建udp套接字
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)
        # 2. 准备接收方的地址
        # '192.168.1.10'表示目的ip地址
        # 8080表示目的端口
        self.dest_addr = (ip, port)  # 注意 是元组，ip是字符串，端口是数字

    def send_msg(self, msg):
        # 3. 从键盘获取数据
        send_data = msg

        # 4. 发送数据到指定的电脑上的指定程序中
        self.udp_socket.sendto(send_data.encode(), self.dest_addr)

        # 5. 关闭套接字
        self.udp_socket.close()


if __name__ == '__main__':
    ip = "10.5.8.20"
    port = 8080
    udp = SendMSG(ip=ip, port=port)
    msg = input("请输入要发送的数据:")
    udp.send_msg(msg=msg)
