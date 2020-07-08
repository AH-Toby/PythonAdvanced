# -*- coding:utf-8 -*-
# epoll
import select
import socket

# 1.创建套接字
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.设置重复使用
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 3.绑定主机信息
server_sock.bind(("", 8080))
# 4.被动监听
server_sock.listen(128)

# 用来打印套接字对应的文件描述符
# print(server_sock.fileno())
# print(select.EPOLLIN|select.EPOLLET)

# 5.创建一个epoll对象
epoll = select.poll()

# 6.注册事件到epoll中
# epoll.register(fd, eventmask])
# 注意，如果fd已经注册过，则会发生异常
# 将创建的套接字添加到epoll的事件监听中
epoll.register(server_sock.fileno(), select.EPOLLIN)

# 创建两个字典来保存新连接的客户端信息
# 为什么要用字典而不是列表是为了，自动去重复
connections = {}
addresses = {}

# 7.循环等待客户端的到来或者对方发送数据
while True:
    # 8.epoll 进行 fd 扫描的地方 -- 未指定超时时间则为阻塞等待,获取共享空间中的事件和文件描述符
    epoll_List = epoll.poll()  # 结果：((文件描述符,事件)(文件描述符,事件)(文件描述符,事件))

    # 9.对事件进行判断
    for fd, events in epoll_List:
        # 如果是socket创建的套接字被激活
        if fd == server_sock.fileno():
            # 接收数据
            # 得到新客户端socket
            new_sock, new_addr = server_sock.accept()
            print('有新的客户端到来%s' % str(new_addr))
            connections[new_sock.fileno()] = new_sock
            addresses[new_sock.fileno()] = new_addr

            # 向epoll中注册新socket的可读事件
            epoll.register(new_sock.fileno(), select.EPOLLIN)

        # 如果是客户端发送数据
        elif events == select.EPOLLIN:
            # 直接接受数据
            recv_data = connections[fd].recv(1024).decode('utf-8')

            # 删除烂数据
            if recv_data:
                print('recv:%s' % recv_data)
            else:
                # 从 epoll 中移除该 连接 fd
                epoll.unregister(fd)

                # server 侧主动关闭该 连接 fd
                connections[fd].close()
                print("%s---offline---" % str(addresses[fd]))
                del connections[fd]
                del addresses[fd]

