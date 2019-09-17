# import socket
# #创建套接字
# #参数：socket_family：选择地址族类型    socket_type套接字类型(必须相同类型的套接字才能通信)    proto:选择子协议类型，通常为0     返回值：返回套接字对象
# sockfd = socket.socket(socket_family = AF_INET, socket_type = SOCK_STREAM, proto = 0)
# #绑定服务端地址
# #功能：绑定IP地址  参数：元组 (ip, port)
# #localhost 127.0.0.1  本机网卡ip   0.0.0.0
# sockfd.bind(addr)
# #设置监听套接字
# #功能：将套接字设置为监听套接字，创建监听队列   参数：n表示监听队列大小
# sockfd.listen(n)
# #等待处理客户端连接请求
# #功能：阻塞等待处理客户端连接  返回值：connfd 客户端连接套接字  addr连接的客户端地址
# #阻塞函数：程序运行过程中遇到阻塞函数则暂停运行直到某种组设条件达成再继续运行
# #connfd套接字，为分裂出来为当前客户端连接收发信息的
# #connfd, addr = sockfd.accept()
# #消息收发
# #功能：接收对应客户端消息   参数：一次最多接收多少字节  返回值：接收到的内容   如果没有消息则会阻塞
# connfd.recv(buffersize)
# #发送消息给对应客户端  参数：要发送的内容，必须时bytes格式   返回值：返回实际发送消息的大小
# n=connfd.send(data)
# #关闭套接字
# sockfd.close()

#服务端
# from socket import *     #import socket  会报错，郁闷
# #创建套接字
# sockfd = socket(AF_INET, SOCK_STREAM)
# #绑定地址
# sockfd.bind(('0.0.0.0', 8888))
# #设置监听
# sockfd.listen(5)
# #等待接受连接
# print("waiting for connetct...")
# connfd, addr = sockfd.accept()
# print("connetct from", addr)
# #收发消息
# data = connfd.recv(1024)
# print(data)
# n = connfd.send(b'Receive you message')
#print("发送了%d字节" % n)
# #关闭套接字
# connfd.close()
# sockfd.close()

# #客户端，必须相同套接字才能通信
# from socket import *
# #创建套接字
# sockfd = socket(AF_INET, SOCK_STREAM)
# #发起连接
# server_addr = ('127.0.0.1', 8888)
# sockfd.connect(server_addr)
# #消息发送接收
# data = input("发送>>")
# sockfd.send(data.encode())
# data = sockfd.recv(1024)
# print("接受到", data.decode())

# #关闭套接字
# sockfd.close()

# #服务端,循环发送
# from socket import *
# #创建套接字
# sockfd = socket(AF_INET, SOCK_STREAM)
# #绑定地址
# sockfd.bind(('0.0.0.0', 8888))
# #设置监听
# sockfd.listen(5)
# #等待接受连接
# print("waiting for connetct...")
# connfd, addr = sockfd.accept()
# print("connetct from", addr)
# while True:
# 	#收发消息
# 	data = connfd.recv(1024).decode()
# 	if data == "##":
# 		break
# 	print(data)
# 	n = connfd.send(b'Receive you message')
# 	print("发送了%d字节" % n)
# #关闭套接字
# connfd.close()
# sockfd.close()

# # 客户端，必须相同套接字才能通信
# from socket import *
# #创建套接字
# sockfd = socket(AF_INET, SOCK_STREAM)
# #发起连接
# server_addr = ('127.0.0.1', 8888)
# sockfd.connect(server_addr)
# while True:
# 	#消息发送接收
# 	data = input("发送>>")
# 	sockfd.send(data.encode())
# 	if data == "##":
# 		break
# 	data = sockfd.recv(1024)
# 	print("接受到", data.decode())

# #关闭套接字
# sockfd.close()

#服务端,循环发送，当前连接断开，等待下一个连接
from socket import *
#创建套接字
sockfd = socket(AF_INET, SOCK_STREAM)
#绑定地址
sockfd.bind(('0.0.0.0', 8888))
#设置监听
sockfd.listen(5)
#等待接受连接
while True:
	print("waiting for connetct...")
	connfd, addr = sockfd.accept()
	print("connetct from", addr)
	while True:
		#收发消息
		data = connfd.recv(1024).decode()
		if not data:
			break
		print(data)
		n = connfd.send(b'Receive you message')
		print("发送了%d字节" % n)
	#关闭套接字
	connfd.close()
sockfd.close()

# 客户端，必须相同套接字才能通信
from socket import *
#创建套接字
sockfd = socket(AF_INET, SOCK_STREAM)
#发起连接
server_addr = ('192.168.3.10', 8888)
sockfd.connect(server_addr)
while True:
	#消息发送接收
	data = input("发送>>")
	sockfd.send(data.encode())
	if not data:
		break
	data = sockfd.recv(1024)
	print("接受到", data.decode())

#关闭套接字
sockfd.close()