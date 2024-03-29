#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/3 16:16
# @Author  : toby
# @File    : 7.非阻塞式web服务器.py
# @Software: PyCharm
# @Desc:
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/3 15:11
# @Author  : toby
# @File    : 6.web服务器协程分流.py
# @Software: PyCharm
# @Desc:
import re
import socket
import asyncio


class WSGIServer(object):
    def __init__(self, server_addr):
        # 用来存储所有的新链接的socket
        self.g_socket_list = list()

        # 创建套接字
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 允许立即使用上次绑定的port
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定IP地址和端口
        self.sock.bind(server_addr)
        # 设置被动套接字，并制定队列的长度
        self.sock.listen(128)
        # 5.设置socket为非阻塞
        # 将套接字设置为非堵塞
        # 设置为非堵塞后，如果accept时，恰巧没有客户端connect，那么accept会
        # 产生一个异常，所以需要try来进行处理
        self.sock.setblocking(False)

    async def server_forever(self):
        """
        循环运行web服务器，等待客户端的链接并为客户端服务
        """
        while 1:
            await asyncio.sleep(1)
            try:
                client_sock, client_ip = self.sock.accept()
                print("获取到新的客户端连接")
            except:
                print("没有新的客户端连接。。。。。。。。")
            else:
                print("有新的客户端连接过来。。。。。。。。")
                try:
                    client_sock.setblocking(False)
                except:
                    print("客户端没有数据。。。。")
                else:
                    self.g_socket_list.append(client_sock)
                    await self.request_handle()
            # new_thread = threading.Thread(target=self.request_handle, args=(client_sock,))
            # new_thread.start()
            # 因为线程是共享同一个套接字，所以主线程不能关闭，否则子线程就不能再使用这个套接字了
            # client_sock.close()

    async def request_handle(self):
        """
        处理请求
        """
        for sock in self.g_socket_list[:]:  # 浅拷贝获取一个全新的列表
            try:
                # 接收网络请求
                request_data = sock.recv(1024).decode("utf-8")
            except:
                print("数据编码错误")
            else:
                # 判断消息是否有数据
                if not request_data:  # 没有消息
                    print("client is disconnected。。。。")

                    self.g_socket_list.remove(sock)  # 删除无用socket
                else:
                    await self.data_prrocess(request_data, sock)
                sock.close()

    async def data_prrocess(self, request_data, sock):
        # 判断消息是否有数据
        if not request_data:
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

            # 解决长连接问题
            response_header += "Content-Type: text/html; charset=utf-8\r\n"
            response_header += "Content-Length:%d\r\n" % len(response_content)

            # 空行
            response_header += '\r\n'

        else:
            # 404表示没有这个界面
            # 响应行
            response_header = 'HTTP/1.1 200 OK\r\n'

            # 响应头
            response_header += 'Server: PythonWebServer1.0\r\n'
            # 响应内容
            response_content = f.read()
            # 解决长连接问题
            response_header += "Content-Type: text/html; charset=utf-8\r\n"
            response_header += "Content-Length:%d\r\n" % len(response_content)

            # 空行
            response_header += '\r\n'

            f.close()
        finally:
            # 拼接发送
            response_data = (response_header.encode('utf-8')) + response_content
            sock.send(response_data)


# 设置服务器端口和ip
SERVER_ADDR = ("", 8080)
# 设置静态资源路径
DOCUMENTS_ROOT = './html/html'


async def main():
    """程序运行入口"""
    httpd = WSGIServer(SERVER_ADDR)
    await httpd.server_forever()


if __name__ == '__main__':
    asyncio.run(main())
