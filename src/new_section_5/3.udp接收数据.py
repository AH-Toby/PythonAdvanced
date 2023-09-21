#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/21 23:50
# @Author  : toby
# @File    : 3.udp接收数据.py
# @Software: PyCharm
# @Desc:
import socket


class UDPReceiver(object):
    def __init__(self, my_addr: tuple):
        self.ipv4_udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ipv4_udp_socket.bind(my_addr)  # 绑定自己的ip地址和端口号

    def receive_msg(self):
        # 向指定地址发送信息
        rec_msg = self.ipv4_udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
        print(rec_msg)

    def __del__(self):
        # 调用完成自动关闭socket
        self.ipv4_udp_socket.close()


if __name__ == '__main__':
    ip = ""
    port = 8081
    udp_sender = UDPReceiver(my_addr=(ip, port))
    udp_sender.receive_msg()
