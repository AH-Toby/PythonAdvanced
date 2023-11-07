#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 11:37
# @Author  : toby
# @File    : 1.返回固定的数据的web服务器.py
# @Software: PyCharm
# @Desc:
import socket


def request_handle(sock):
    # 接收消息
    request_data = sock.recv(1024).decode("utf-8")
    if not request_data:
        print("client is disconnected....")
        sock.close()
        return
    print("接收到消息")
    response_line = "HTTP/1.1 200 OK\r\n"
    response_header = "Server:PythonWebServer1.0\r\n"
    response_content = "Hello World!"
    response_data = response_line + response_header + "\r\n" + response_content
    # 发送响应
    sock.send(response_data.encode())
    sock.close()


def main():
    # 创建socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置套接字复用地址，设置当服务器先close，即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时，可以立即绑定端口
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定ip地址和端口
    sock.bind(("", 8080))
    sock.listen(128)
    while 1:
        client_socket, client_add = sock.accept()
        # 处理请求
        request_handle(client_socket)


if __name__ == '__main__':
    main()
