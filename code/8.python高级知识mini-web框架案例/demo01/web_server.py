# -*- coding:utf-8 -*-
import re
import time
import socket
import multiprocessing
from web import mini_web


class WsgiServer(object):
    def __init__(self, server_addr):
        """基本信息"""
        # 用来存储所有的新链接的socket
        self.g_socket_list = list()

        # 1.创建服务器socket
        self.server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2.允许立即使用上次绑定的port
        self.server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 3.绑定ip地址和端口号
        self.server_soc.bind(server_addr)

        # 4.设置为被动套接字，并制定长度
        self.server_soc.listen()

    def server_run(self):
        """运行web服务器，等待客户端的链接并为客户端服务"""
        while True:
            new_client_soc, new_client_addr = self.server_soc.accept()
            new_process = multiprocessing.Process(target=self.request_handler, args=(new_client_soc,))
            new_process.start()
            new_client_soc.close()

    def request_handler(self, sock):
        """
        处理请求
        """
        try:
            # 接收网络请求消息
            request_data = sock.recv(1024).decode('utf-8')
            print(request_data)

        except Exception as e:
            print(e)
            print("数据编码错误")

        else:
            # 判断消息是否有数据
            if not request_data:  # 没有消息
                print("client is disconnected。。。。")
            else:
                self.deal_data(request_data, sock)

            sock.close()

    def deal_data(self, request_data, sock):
        """"
        数据处理
        """

        # 切割请求头
        request_header_lines = request_data.splitlines()

        # 打印测试
        for request_header_line in request_header_lines:
            print(request_header_line)

        # 获取请求行行信息：因为它包含请求的资源
        http_request_line = request_header_lines[0]

        # 正则切割出请求资源的文件名,eg:GET / HTTP/1.1
        request_file_name = re.match('[^/]+(/[^ ]*)', http_request_line).group(1)
        print("_" * 100)
        print(request_file_name)

        #  判断是静态还是动态
        if request_file_name.endswith(".py"):  # 动态
            print("动态开始")
            url_dict = dict()
            web = mini_web.application(url_dict, self.set_response_headers)

            # 合并header和body
            response_header = "HTTP/1.1 {status}\r\n".format(status=self.headers[0])
            response_header += "Content-Type: text/html; charset=utf-8\r\n"
            response_header += "Content-Length: %d\r\n" % len(web)
            for temp_head in self.headers[1]:
                response_header += "{0}:{1}\r\n".format(*temp_head)

            response = response_header + "\r\n"
            response += web

            sock.send(response.encode('utf-8'))
            print(web)
            print("动态开始")

        # 静态
        else:
            request_file_name = g_static_document_root + request_file_name
            print(request_file_name)

            # 读取对应文件并返回
            try:
                f = open(request_file_name, 'rb')
            except IOError:
                # 404表示没有这个界面
                # 响应行
                response_header = 'HTTP/1.1 404  not found\r\n'
                # 响应内容
                response_content = '====sorry ,file not found===='.encode('utf-8')
                # 空行
                response_header += '\r\n'

            else:
                # 404表示没有这个界面
                # 响应行
                response_header = 'HTTP/1.1 200 OK\r\n'

                # 响应内容
                response_content = f.read()
                f.close()

            # 响应头
            response_header += 'Server: PythonWebServer1.0\r\n'
            # 解决长连接问题
            response_header += "Content-Type: text/html; charset=utf-8\r\n"
            response_header += "Content-Length:%d\r\n" % len(response_content)

            # 空行
            response_header += '\r\n'

            # 拼接发送
            print(response_header)
            response_data = (response_header.encode('utf-8')) + response_content
            sock.send(response_data)

    def set_response_headers(self, status, headers):
        """这个方法，会在 web框架中被默认调用"""
        response_header_default = [
            ("Data", time.ctime()),
            ("Server", "ItCast-python mini web server")
        ]

        # 将状态码/相应头信息存储起来
        # [字符串, [xxxxx, xxx2]]
        self.headers = [status, response_header_default + headers]
        print(self.headers)


# 设置服务器端口和ip
SERVER_ADDR = ("", 8080)
# 设置静态资源路径
g_static_document_root = './html/html'

# 设置动态资源访问路径
g_dynamic_document_root = "./web"


def main():
    """程序运行入口"""
    httpd = WsgiServer(SERVER_ADDR)
    httpd.server_run()


if __name__ == '__main__':
    main()
