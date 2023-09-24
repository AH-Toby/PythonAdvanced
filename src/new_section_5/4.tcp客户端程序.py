#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/22 10:48
# @Author  : toby
# @File    : 4.tcp客户端程序.py
# @Software: PyCharm
# @Desc:
import socket


class TCPClient(object):
    def __init__(self, dest_addr: tuple):
        self.ipv4_tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ipv4_tcp_socket.connect(dest_addr)  # 连接服务器

    def send_msg(self, msg):
        self.ipv4_tcp_socket.send(msg.encode())

    def receive_msg(self):
        msg = self.ipv4_tcp_socket.recv(1024).decode()
        print(msg)

    def __del__(self):
        self.ipv4_tcp_socket.close()


if __name__ == '__main__':
    ip = "10.4.28.188"
    port = 8848
    tcp_client = TCPClient((ip, port))
    tcp_client.send_msg("发送信息")
    tcp_client.receive_msg()
