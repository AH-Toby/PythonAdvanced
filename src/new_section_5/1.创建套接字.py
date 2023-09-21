#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/21 22:51
# @Author  : toby
# @File    : 1.创建套接字.py
# @Software: PyCharm
# @Desc:
import socket

# 创建一个ipv4 TCP套接字
ipv4_tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 创建一个ipv6 UDP套接字
ipv6_udp_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

# 创建一个UNIX域套接字
unix_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

print(ipv4_tcp_socket)
print(ipv6_udp_socket)
print(unix_socket)

ipv4_tcp_socket.close()
ipv6_udp_socket.close()
unix_socket.close()
