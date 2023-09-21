#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/21 23:40
# @Author  : toby
# @File    : 2.udp发送数据.py
# @Software: PyCharm
# @Desc:
import socket


class UDPSender(object):
    def __init__(self, dest_addr: tuple):
        self.dest_addr = dest_addr  # 目标机器的IP地址和端口号
        self.ipv4_udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_msg(self, msg: str):
        # 向指定地址发送信息
        self.ipv4_udp_socket.sendto(msg.encode(), self.dest_addr)

    def __del__(self):
        # 调用完成自动关闭socket
        self.ipv4_udp_socket.close()


if __name__ == '__main__':
    ip = "192.168.1.6"
    port = 8080

    udp_sender = UDPSender(dest_addr=(ip, port))
    msg = input("请输入要发送的信息:")
    udp_sender.send_msg(msg)
