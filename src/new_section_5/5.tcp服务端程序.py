#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/22 11:20
# @Author  : toby
# @File    : 5.tcp服务端程序.py
# @Software: PyCharm
# @Desc:
import socket


class TCPServer(object):
    def __init__(self, my_addr: tuple):
        self.ipv4_tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ipv4_tcp_socket.bind(my_addr)  # 绑定端口
        self.ipv4_tcp_socket.listen(128)  # 设置监听
        self.client_socket, self.client_ip = self.ipv4_tcp_socket.accept()  # 等待客户端连接

    def send_msg(self, msg):
        self.client_socket.send(msg.encode())

    def receive_msg(self):
        msg = self.client_socket.recv(1024).decode()
        print(msg)

    def __del__(self):
        self.ipv4_tcp_socket.close()


if __name__ == '__main__':
    ip = "10.4.28.188"
    port = 8848
    tcp_server = TCPServer((ip, port))
    tcp_server.send_msg("tcp服务端发送数据")
    tcp_server.receive_msg()
