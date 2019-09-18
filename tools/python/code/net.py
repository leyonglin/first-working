#! /usr/bin/env python3
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
# #connfd, addr = sockfd.accept()
# #消息收发
# #功能：接收对应客户端消息   参数：一次最多接收多少字节  返回值：接收到的内容   如果没有消息则会阻塞
# connfd.recv(buffersize)   #收
# connfd.send(data)         #发
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
# connfd, addr = sockfd.accept()   #connfd套接字，是与当前连接的套接字
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

# #服务端,循环发送，当前连接断开，等待下一个连接,优雅退出
# from socket import *
# #创建套接字
# sockfd = socket(AF_INET, SOCK_STREAM)
# #绑定地址
# sockfd.bind(('0.0.0.0', 8888))
# #设置监听
# sockfd.listen(5)
# #等待接受连接
# while True:
# 	print("waiting for connetct...")
# 	connfd, addr = sockfd.accept()
# 	print("connetct from", addr)
# 	while True:
# 		#收发消息
# 		data = connfd.recv(1024).decode()
# 		if not data:
# 			break
# 		print(data)
# 		n = connfd.send(b'Receive you message')
# 		print("发送了%d字节" % n)
# 	#关闭套接字
# 	connfd.close()
# sockfd.close()

# # 客户端，必须相同套接字才能通信
# from socket import *
# #创建套接字
# sockfd = socket(AF_INET, SOCK_STREAM)
# #发起连接
# server_addr = ('192.168.3.10', 8888)
# sockfd.connect(server_addr)
# while True:
# 	#消息发送接收
# 	data = input("发送>>")
# 	sockfd.send(data.encode())
# 	if not data:
# 		break
# 	data = sockfd.recv(1024)
# 	print("接受到", data.decode())

# #关闭套接字
# sockfd.close()


# #udp服务端
# from socket import *
# #创建数据报套接字
# sockfd = socket(AF_INET,SOCK_DGRAM)
# #绑定服务端地址
# server_addr = ('0.0.0.0', 8888)
# sockfd.bind(server_addr)
# #消息收发
# while  True:
# 	data, addr = sockfd.recvfrom(1024)
# 	print("Receive from %s:%s" %\
# 		(addr,data.decode()))
# 	sockfd.sendto('收到你的消息'.encode(),addr)
# sockfd.close()



# #udp客户端
# from socket import *
# import sys
# if len(sys.argv) < 3:
# 	print('''
# 		argv is error!
# 		run as
# 		python3 udp_client.py 127.0.0.1 8888''')
# #从命令行输入ip，端口
# HOST = sys.argv[1]
# PORT = int(sys.argv[2])
# ADDR = (HOST,PORT)
# # try:
# #     HOST = sys.argv[1]
# #     PORT = int(sys.argv[2])
# #     ADDR = (HOST,PORT)
# # except:
# #     print('''
# # argv is error!
# # run as
# # python3 udp_client.py 127.0.0.1 8888''')
# #     sys.exit()
# #创建套接字
# sockfd = socket(AF_INET,SOCK_DGRAM)
# #消息收发
# while True:
# 	data = input("message")
# 	if not data:
# 		break
# 	sockfd.sendto(data.encode() ,ADDR)
# 	data,addr = sockfd.recvfrom(1024)
# 	print("Receive message from server", data.decode())
# sockfd.close()

# # udp之广播
# # udp_gb_server.py
# '''服务端（UDP协议局域网广播）'''
# import socket
# from time import sleep
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# PORT = 1060
# while True:
#     network = '192.168.3.255'
#     s.sendto('Client broadcast message!'.encode('utf-8'), (network, PORT))
#     sleep(5)

# # udp_gb_client.py
# '''客户端（UDP协议局域网广播）'''
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# PORT = 1060
# s.bind(('0.0.0.0', PORT))
# print('Listening for broadcast at ', s.getsockname())
# while True:
#     data, address = s.recvfrom(65535)
#     print('Server received from {}:{}'.format(address, data.decode('utf-8')))
 
# #下面两端是自己写的，为啥不起作用呢？
# from socket import *
# #创建套接字
# s = socket(AF_INET, SOCK_DGRAM)
# #设置套接字可以发送接收广播
# s.setsockopt(SOL_SOCKET, SO_BROADCAST,1)
# #固定接收端口
# s.bind(('0.0.0.0',9999))
# while True:
#         try:
#                 msg,addr = s.recvfrom(1024)
#                 print("从{}获取信息：{}".\
#                         format(addr,msg.decode()))     #与格式化字符串%作用差不多
#         except Exception as e:
#                 print(e)
# s.close()

# from socket import *
# from time import sleep
# #设置目标地址
# dest = ('192.168.3.255',9999)
# s = socket(AF_INET, SOCK_DGRAM)
# #设置能够发送广播：
# s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
# while True:
#         sleep(2)
#         s.sendto("来啊，带你去看晴空万里".encode(),dest)
# s.close()


# #http服务端
# from socket import *
# #创建tcp套接字
# s = socket()
# s.bind(('0.0.0.0', 8000))
# s.listen(5)
# while  True:
# 	c,addr = s.accept()
# 	print("connect",addr)
# 	data = c.recv(4096)
    # request_lines = data.splitlines()   #将request请求按行分隔
    # for line in request_lines:
    #     print(line.decode())
# 	print("*********************************")
# 	#print(data)   #浏览器发来的http请求
# 	print("*********************************")
# 	#组织响应内容
# 	data = '''HTTP/1.1 200 OK
# 	Content-Encoding: gzip
# 	Content-Type: text/html
# 	<h1>Welcome to phili</h1>
# 	'''
# 	c.send(data.encode())
# 	c.close()
# s.close()

# #客户端，传输文件
# from socket import *
# s = socket()
# s.bind(('0.0.0.0,8888'))
# s.listen(3)
# c,addr = s.accept()
# print("Connect from",addr)
# f=open('a.txt','wb')
# while True:
# 	data = c.recv(1024)
# 	if not data:
# 		break
# 	f.write(data)
# f.close()
# c.close()
# s.close()

# #服务端
# from socket import *
# s = socket()
# s.connect(('127.0.0.1',8888))
# f.open('b.txt','rb')
# while Tru:
# 	data = f.read(1024)
# 	if not data:
# 		break
# 	s.send(data)
# f.close()
# s.close()

# #非阻塞
# from socket import *
# from time import sleep,ctime
# s = socket()
# s.bind(('127.0.0.1',8888))
# s.listen(3)
# #将套接字设置为非阻塞
# s.setblocking(False)
# 将套接字设置超时时间
# s.settimeout(5)
# while True:
# 	print("waiting for connect...")
# 	try:
# 		c,addr = s.accept()
# 	except BlockingIOError:
# 		sleep(2)
# 		print(ctime())
# 		continue
# 	else:
# 		print("Connect from",addr)
# 		while  True:
# 			data = c.recv(1024).decode()
# 			if not data:
# 				break
# 			print(data)
# 			c.send(ctime().encode())
# 		c.close()


#io多路复用
from select import select
from socket import *
#创建套接字作为关注io
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)
rlist = [s]
wlist = []
xlist = []
while  True:
	#提交监测关注的io等待io发生
	print('waiting')
	rs,ws,xs = select(rlist, wlist, xlist)
	for r in rs:                          #遍历，知道那个io准备就绪了
		if r is s:                        #通过判断，是初始关注io则做不同的io事件
			c,addr = r.accept()
			print('connect from',addr)
			rlist.append(c)               #将连接io添加到列表，这样连接io也是关注io，就能持续通信
		else:                             #上面会有多个if判断，最后这里，相当于除了初始关注的io，其它的都是已连接的，能直接通信
			data = r.recv(1024)
			if not data:                  #这里本来是判断无数据发送，则该io执行下列语句，但好像试不出来
				rlist.remove(r)           #如果结束通信，则将连接io从关注列表移除
				r.close()                 #关闭套接字
			else:                         #如果断开(if匹配)则不再发送数据
				print(data.decode())
				r.send(b'Receive your message\n')
	# print('有io事件发生')
	# c,addr = rs[0].accept()
	# print(rs)
	# print('connect from',addr)