# -*- coding:utf-8 -*-

# 封装成类
import re
import sys
import socket
import select


class WsgiServer(object):
    def __init__(self, server_address):
        # 1.创建套接字
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 2.允许立即使用上次绑定的port
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 3.绑定ip地址和端口
        self.sock.bind(server_address)

        # 4.设置被动套接字,并制定队列的长度
        self.sock.listen(128)

        # 5.设置socket为非阻塞
        self.sock.setblocking(False)

        # 6.创建一个epoll对象
        self.epoll = select.epoll()

        # 7.将tcp服务器套接字加入到epoll中进行监听
        self.epoll.register(self.sock.fileno(), select.EPOLLIN | select.EPOLLET)

        # 8.创建添加fd对应的套接字
        self.fd_socket = dict()

    def server_forever(self):
        """循环运行web服务器，等待客户端的链接并为客户端服务"""
        while True:
            # epoll 进行 fd 扫描的地方 -- 未指定超时时间则为阻塞等待,获取共享空间中的事件和文件描述符
            epoll_lists = self.epoll.poll()

            # 循环事件和文件描述符
            for fd, events in epoll_lists:

                # 判断事件和文件描述符类型是否属于客户端socket或者是服务端socket
                if fd == self.sock.fileno():  # 是服务端socket
                    try:
                        client_sock, client_ip = self.sock.accept()  # 结收客户端信息
                    except:
                        print("没有新的客户端连接。。。。。。。。")
                    else:
                        try:
                            client_sock.setblocking(False)
                        except:
                            print("客户端没有数据。。。。")
                        else:
                            # 向epoll中注册连接socket的可读事件
                            self.epoll.register(client_sock.fileno(), select.EPOLLET | select.EPOLLIN)
                            # 记录这个数据
                            self.fd_socket[client_sock.fileno()] = client_sock

                # 接收到数据说明这个socket是有数据的是客户端socket
                elif events == select.EPOLLIN:

                    request = self.fd_socket[fd].recv(1024).decode('utf-8')
                    # 判断数据是否存在
                    if request:
                        self.data_process(request, self.fd_socket[fd])
                    else:
                        # 在epoll中注销客户端的信息
                        self.epoll.unregister(fd)
                        # 关闭客户端的文件句柄
                        self.fd_socket[fd].close()
                        # 在字典中删除与已关闭客户端相关的信息
                        del self.fd_socket[fd]

    def data_process(self, request_data, sock):
        if not request_data:
            return

        """处理数据"""
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
            print(response_header)
            response_data = (response_header.encode('utf-8')) + response_content
            sock.send(response_data)


# 设置静态资源路径
DOCUMENTS_ROOT = './html/html'


def main():
    """程序运行入口"""
    # python3 xxxx.py 7890
    if len(sys.argv) == 2:
        port = sys.argv[1]
        if port.isdigit():
            port = int(port)
    else:
        print("运行方式如: python3 xxx.py 7890")
        return
    SERVER_ADDR = ('', port)
    print("http服务器使用的port:%s" % port)
    httpd = WsgiServer(SERVER_ADDR)
    httpd.server_forever()


if __name__ == '__main__':
    main()
