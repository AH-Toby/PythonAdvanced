#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 11:59
# @Author  : toby
# @File    : 2.返回固定页面数据的web服务器.py
# @Software: PyCharm
# @Desc:
import re
import socket


def request_handle(sock):
    # 接收消息
    request_data = sock.recv(1024).decode("utf-8")
    if not request_data:
        print("client is disconnected....")
        sock.close()
        return
    print("接收到消息")
    requests_header_lines = request_data.splitlines()  # 切割请求头

    # 打印测试
    for requests_header_line in requests_header_lines:
        print(requests_header_line)

    https_request_line = requests_header_lines[0]
    # 正则切割出请求资源的文件名
    request_file_name = re.match("[^/]+(/[^ ]*)", https_request_line).group(1)
    print(request_file_name)

    # 如果没有指定页面
    if request_file_name == "/":
        request_file_name = DOCUMENTS_ROOT + "/index.html"
    else:
        request_file_name = DOCUMENTS_ROOT + request_file_name

    # 读取指定文件并返回
    try:
        f = open(request_file_name, "rb")
    except IOError:
        # 404表示没有这个界面
        # 响应行
        response_header = 'HTTP/1.1 404  not found\r\n'

        # 响应头
        response_header += 'Server: PythonWebServer1.0\r\n'

        # 空行
        response_header += '\r\n'

        # 响应内容
        response_content = '====sorry ,file not found===='.encode('utf-8')
    else:
        # 404表示没有这个界面
        # 响应行
        response_header = 'HTTP/1.1 200 OK\r\n'

        # 响应头
        response_header += 'Server: PythonWebServer1.0\r\n'

        # 空行
        response_header += '\r\n'

        # 响应内容
        response_content = f.read()
        f.close()
    finally:
        response_data = (response_header.encode("UTF-8")) + response_content
        # 发送响应
        sock.send(response_data)
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


# 这里配置服务器
DOCUMENTS_ROOT = "./html/html"
if __name__ == '__main__':
    main()
