# -*- coding:utf-8 -*-
import re
import sys
import socket
import multiprocessing


# from dynamic import my_web


class WsgiServer(object):
    def __init__(self, address, module):
        self.status = None
        self.params = None
        self.module = module
        # 1.创建套接字
        self.server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2.设置socket为自动释放
        self.server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 3.绑定地址
        self.server_soc.bind(address)
        # 4.变成监听套接字
        self.server_soc.listen(128)

    def run_server(self):
        """运行服务器"""
        while True:
            # 等待客户端连接
            new_soc, client_addr = self.server_soc.accept()
            # 创建进程启动服务
            p = multiprocessing.Process(target=self.service_client, args=(new_soc,))
            p.start()
            new_soc.close()

    def service_client(self, sock):
        """服务端处理接收的请求"""
        try:
            request_data = sock.recv(1024).decode('utf-8')
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

    def deal_data(self, data, sock):
        """处理数据"""
        # 切割请求头
        request_header_lines = data.splitlines()

        # 打印测试
        for request_header_line in request_header_lines:
            print(request_header_line)

        # 获取请求行行信息：因为它包含请求的资源
        http_request_line = request_header_lines[0]

        # 正则切割出请求资源的文件名，eg:GET / HTTP/1.1
        request_file_name = re.match(r'[^/]+(/[^ ]*)', http_request_line).group(1)

        print("请求的文件名为：%s" % request_file_name)

        #  判断是静态还是动态
        if request_file_name.endswith(".html"):  # 伪静态
            environ = dict()
            environ['file_name'] = request_file_name
            body = self.module.application(environ, self.set_head_params)

            header = "HTTP/1.1 %s\r\n" % self.status

            # 去拼接我们的头部
            for temp in self.params:
                header += "%s:%s\r\n" % (temp[0], temp[1])
            content = header + '\r\n' + body
            sock.send(content.encode('utf-8'))
        else:
            # 从静态返回数据

            try:
                f = open("./static" + request_file_name, "rb")
            except:
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                response += "------file not found-----"
                sock.send(response.encode("utf-8"))
            else:
                html_content = f.read()
                f.close()
                # 2.1 准备发送给浏览器的数据---header
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                # 2.2 准备发送给浏览器的数据---boy
                # response += "hahahhah"

                # 将response header发送给浏览器
                sock.send(response.encode("utf-8"))
                # 将response body发送给浏览器
                sock.send(html_content)
        sock.close()

    def set_head_params(self, status, params):
        """回调返回状态码和头部信息"""
        print(status, params)
        self.status = status
        self.params = params


def main():
    # if len(sys.argv) == 2:
    #     print(sys.argv[1])
    #     try:
    #         port = int(sys.argv[1])
    #         addr = ("", port)
    #         web_server = WsgiServer(addr)
    #         web_server.run_server()
    #     except Exception as e:
    #         print(e)
    #         print("请按照格式 xxx.py 端口号输入")
    # else:
    #     print("请按照格式 xxx.py 端口号输入")
    try:
        with open('./wsgi.config') as f:
            content = f.read()
        # 转成字典
        port = eval(content)['port']
        addr = ("", port)
        sys.path.append("./dynamic")
        module = __import__("my_web")

        web_server = WsgiServer(addr, module)
        web_server.run_server()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
