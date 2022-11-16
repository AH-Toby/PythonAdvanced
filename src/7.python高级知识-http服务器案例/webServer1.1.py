# -*- coding:utf-8 -*-
import re
import socket


def request_handle(sock):
    """处理数据"""
    request_data = sock.recv(1024).decode('utf-8')
    if not request_data:  # 没有消息
        print("client is disconnected。。。。")
        sock.close()
        return
    request_header_lines = request_data.splitlines()  # 切割请求头
    # 打印测试
    for request_header_line in request_header_lines:
        print(request_header_line)

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


def main():
    """入口"""
    # 1.创建socket套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.设置套接字复用
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 3.设置端口号和ip
    sock.bind(('', 8080))
    # 4.开启监听模式
    sock.listen(128)
    while True:
        # 5.等待客户端连接
        client_sock, client_ip = sock.accept()
        # 处理请求
        request_handle(client_sock)


# 这里配置服务器
DOCUMENTS_ROOT = "./html/html"  # 全局函数

if __name__ == '__main__':
    main()
