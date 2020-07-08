# -*- coding:utf-8 -*-
import socket


def request_handler(sock):
    """处理请求"""
    # 接收消息
    request_data = sock.recv(1024).decode('utf-8')
    if not request_data:  # 没有消息
        print("client is disconnected。。。。")
        sock.close()
        return
    print("接收到消息为%s" % request_data)
    # 响应行
    response_line = 'HTTP/1.1 200 OK\r\n'
    # 响应头
    response_header = 'Server: PythonWebServer1.0\r\n'
    # 响应内容
    response_content = 'Hello World!'

    response_data = response_line + response_header + '\r\n' + response_content

    # 发送响应
    sock.send(response_data.encode())
    sock.close()


def main():
    """程序运行入口"""
    # tcp
    # 创建socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置套接字复用地址，设置当服务器先close，即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时，可以立即绑定端口
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定ip地址和端口
    sock.bind(("", 8080))
    # 设置被动套接字
    sock.listen(128)
    # 等待连接
    while True:
        client_socket, client_add = sock.accept()
        # 处理请求
        request_handler(client_socket)


if __name__ == '__main__':
    main()
