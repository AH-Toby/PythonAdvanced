#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/3 11:46
# @Author  : toby
# @File    : 5.web服务器多线程分流.py
# @Software: PyCharm
# @Desc:
import re
import socket
import threading


class WSGIServer(object):
    def __init__(self, server_addr):
        # 创建套接字
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 允许立即使用上次绑定的port
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定IP地址和端口
        self.sock.bind(server_addr)
        # 设置被动套接字，并制定队列的长度
        self.sock.listen(128)

    def server_forever(self):
        """
        循环运行web服务器，等待客户端的链接并为客户端服务
        """
        while 1:
            client_sock, client_ip = self.sock.accept()
            new_thread = threading.Thread(target=self.request_handle, args=(client_sock,))
            new_thread.start()
            # 因为线程是共享同一个套接字，所以主线程不能关闭，否则子线程就不能再使用这个套接字了
            # client_sock.close()

    def request_handle(self, sock):
        """
        处理请求
        """
        # 接收网络请求
        request_data = sock.recv(1024).decode("utf-8")

        # 判断消息是否有数据
        if not request_data:
            print("client is disconnected...")
            sock.close()
            return

        # 切割请求头
        request_header_lines = request_data.splitlines()

        # 打印测试
        for request_header_line in request_header_lines:
            print(request_header_line)

        # 获取请求行行信息：因为它包含请求的资源
        http_request_line = request_header_lines[0]

        # 正则切割出请求资源的文件名,eg:GET / HTTP/1.1
        request_file_name = re.match('[^/]+(/[^ ]*)', http_request_line).group(1)
        print(request_file_name)

        # 如果没有指定访问哪个页面。例如index.html
        # GET / HTTP/1.1
        if request_file_name == '/':
            request_file_name = DOCUMENTS_ROOT + "/index.html"
        else:
            request_file_name = DOCUMENTS_ROOT + request_file_name
        print(request_file_name)

        # 读取对应文件并返回
        try:
            f = open(request_file_name, 'rb')
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
            # 拼接发送
            print(response_header)
            response_data = (response_header.encode('utf-8')) + response_content
            sock.send(response_data)
            sock.close()


# 设置服务器端口和ip
SERVER_ADDR = ("", 8080)
# 设置静态资源路径
DOCUMENTS_ROOT = './html/html'


def main():
    """程序运行入口"""
    httpd = WSGIServer(SERVER_ADDR)
    httpd.server_forever()


if __name__ == '__main__':
    main()
