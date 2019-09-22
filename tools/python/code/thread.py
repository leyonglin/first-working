
#!/usr/bin/env python3
#coding=utf-8
'''
name: lin
email:999@qq.com
data: 2019-9
class:AID
introduce:Chatroom server
env:python3.5
'''

#处理僵尸进程os.wait()
# import os
# from time import sleep
# pid = os.fork()
# if pid < 0:
# 	print("error")
# elif pid == 0:
# 	sleep(3)
# 	print("child process pid",os.getpid())
# 	os._exit(2)
# else:
# 	pid,status = os.wait()         #阻塞函数，对退出进程进行处理
# 	print(pid,status)
# 	print(os.WEXITSTATUS(status))  #获取子进程退出状态
# 	while True:
# 		pass

# #处理僵尸进程os.waitpid()
# import os
# from time import sleep
# pid = os.fork()
# if pid < 0:
# 	print("error")
# elif pid == 0:
# 	sleep(3)
# 	print("child process pid",os.getpid())
# 	os._exit(2)
# else:
# 	while True:                                 #持续监测
# 		sleep(1)
# 		pid,status = os.waitpid(-1,os.WNOHANG)  #通过非阻塞的形式捕获子进程退出      
# 		if status != 0:                         #判断是否还有子进程，不然后面获取子进程退出状态会报错
# 			break
# 		else:
# 			print(pid,status)
# 			print(os.WEXITSTATUS(status))  #获取子进程退出状态

#创建二级子进程
# import os
# from time import sleep
# def f1():
# 	sleep(3)
# 	print("one thing")
# def f2():
# 	sleep(4)
# 	print("second thing")
# pid = os.fork()
# if pid<0:
# 	print("error")
# elif pid == 0:
# 	#创建二级子进程
# 	p = os.fork()
# 	if p ==0:
# 		f2()
# 	else:
# 		os._exit(0)
# else:
# 	os.wait() #等一级子进程退出
# 	f1()

# #chat-server
# from socket import *
# import os,sys
# def do_login(s,user,name,addr):
# 	if name in user or name == 'manager':
# 		s.sendto('this user has using'.encode(),addr)
# 		return
# 	s.sendto(b'ok',addr)
# 	#通知其他人
# 	msg = '\nwelcome %s come in chat' % name
# 	for i in user:
# 		s.sendto(msg.encode(),user[i])
# 	#插入用户
# 	user[name] = addr
# def do_quit(s,user,name):
# 	msg = '\n' + name + ' quit chat'
# 	for i in user:
# 		if i == name:
# 			s.sendto(b'EXIT',user[i])
# 		else:
# 			s.sendto(msg.encode(),user[i])
# 	#从字典删除用户
# 	del user[name]
# def do_chat(s,user,name,text):
# 	msg = '\n%s : %s'%(name,text)
# 	for i in user:
# 		if i != name:
# 			s.sendto(msg.encode(),user[i])
# #接收客户端请求
# def do_parent(s):
# 	user={}
# 	while True:
# 		msg,addr = s.recvfrom(1024)
# 		msglist = msg.decode().split(' ')
# 		#区分消息类型
# 		if msglist[0] == 'L':
# 			do_login(s,user,msglist[1],addr)	
# 		elif msglist[0] == 'C':
# 			do_chat(s,user,msglist[1],\
# 				' '.join(msglist[2:]))
# 		elif msglist[0] == 'Q':
# 			do_quit(s,user,msglist[1])
# #接收管理员喊话
# def do_child(s,addr):      #子进程发送消息给父进程，父进程接收后，对其他人进行转发
# 	while True:
# 		msg = input("manager message:")
# 		msg = 'C manager ' + msg
# 		s.sendto(msg.encode(),addr)
# #创建网络,创建进程，调用功能
# def main():
# 	#server address
# 	ADDR = ('0.0.0.0',8888)
# 	#创建套接字
# 	s = socket(AF_INET,SOCK_DGRAM)
# 	s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# 	s.bind(ADDR)
# 	#创建一个单独的进程处理管理员喊话功能
# 	pid = os.fork()
# 	if pid < 0:
# 		sys.exit('创建进程失败')
# 	elif pid == 0:
# 		do_child(s,ADDR)     
# 	else:
# 		do_parent(s)
# if __name__ == '__main__':
# 	main()


# #chat-client
# from socket import *
# import sys,os
# #创建套接字，登陆，创建子进程
# def send_msg(s,name,addr):
# 	while True:
# 		text = input('talk:')
# 		#输入quit表示退出
# 		if text.strip() == 'quit':
# 			msg = 'Q ' + name
# 			s.sendto(msg.encode(),addr)
# 			sys.exit('quit chat')
# 		msg = 'C %s %s'%(name,text)
# 		s.sendto(msg.encode(),addr)
# def recv_msg(s):
# 	while True:
# 		data,addr = s.recvfrom(2048)
# 		#接收EXIT，退出进程
# 		if data.decode() == 'EXIT':
# 			sys.exit(0)
# 		print(data.decode() + '\n发言：',end="")
# def main():
# 	#从命令行获取服务地址
# 	if len(sys.argv) < 3:
# 		print('argv need three')
# 		return
# 	HOST = sys.argv[1]
# 	PORT = int(sys.argv[2])
# 	ADDR = (HOST,PORT)
# 	#创建套接字
# 	s = socket(AF_INET,SOCK_DGRAM)
# 	while True:
# 		name = input('input	your name:')
# 		msg = 'L ' + name
# 		#发送登陆请求
# 		s.sendto(msg.encode(),ADDR)
# 		#等待服务器回复
# 		data,addr = s.recvfrom(1024)
# 		if data.decode() == 'ok':
# 			print('login success')
# 			break
# 		else:
# 			print(data.decode())
# 	#创建父子进程收发消息
# 	pid = os.fork()
# 	if pid < 0:
# 		sys.exit('create process failed')
# 	elif pid == 0:
# 		send_msg(s,name,ADDR)
# 	else:
# 		recv_msg(s)

# if __name__ == '__main__':
# 	main()


# import multiprocessing as mp
# from time import sleep
# import os
# def fun1():
# 	sleep(3)
# 	print('子进程事件1',os.getpid())
# def fun2():
# 	sleep(2)
# 	print('子进程事件2',os.getpid())
# #创建进程对象
# thing = [fun1,fun2]
# L = []
# for i in thing:
# 	p = mp.Process(target = i)
# 	L.append(p)
# 	#启动进程
# 	p.start()
# for j in L:
# 	#阻塞/超时回收进程
# 	j.join()

# #自定义进程类
# from multiprocessing import Process
# import time
# class ClockProcess(Process):
# 	def __init__(self,value):
# 		self.value = value
# 		super(ClockProcess,self).__init__()
# 	def run(self):
# 		for i in range(3):
# 			print('the time is {}'.format(time.ctime()))
# 			time.sleep(self.value)

# #创建自定义进程类的对象
# p = ClockProcess(2)
# #自动调用run
# p.start()
# p.join()


#进程池
# from multiprocessing import Pool
# from time import sleep,ctime
# def worker(msg):
# 	sleep(2)
# 	print(msg)
# 	return msg
# result = []
# #创建进程池
# # pool = Pool(4)
# pool = Pool(processes = 4)
# for i in range(10):
# 	msg = 'hello %d' % i
# 	#将事件放入进程池队列，等待执行
# 	# pool.apply(func = worker,args = (msg,))  #同步
# 	# pool.apply_async(func = worker,args = (msg,))
# 	r = pool.apply_async(func = worker,args = (msg,))
# 	result.append(r)
# #关闭进程池
# pool.close()
# #回收
# pool.join()
# for i in result:	
# 	print(i.get())

# from multiprocessing import Pool
# import time
# def fun(n):
# 	time.sleep(1)
# 	print("执行pool_map事件")
# 	return n*n
# pool = Pool(4)
# #使用map将事件放入进程池
# r = pool.map(fun,range(10))
# pool.close()
# pool.join()
# print(r)

#管道通信
# from multiprocessing import Process,Pipe
# import os,time
# #创建管道对象
# fd1,fd2 = Pipe()
# def fun(name):
# 	time.sleep(3)
# 	#向管道写入内容
# 	fd1.send("hello "+ str(name))
# jobs = []
# for i in range(5):
# 	p = Process(target=fun,args = (i,))
# 	jobs.append(p)
# 	p.start()
# for i in range(5):
# 	#读取管道
# 	data = fd2.recv()
# 	print(data)
# for j in jobs:
# 	j.join()

#消息队列简单使用
# from multiprocessing import Queue
# from time import sleep
# #创建队列
# q = Queue(3)       #创建消息队列
# q.put(1)           #存入数据
# sleep(0.5)
# print(q.empty())  
# q.put(2)
# print(q.full())
# q.put(3)
# print(q.qsize())
# # q.put(4.True,3)   #True 表示非阻塞，但是队列满了会报错，3表示超时时间
# print(q.get())      #获取队列数据，先进先出
# q.close()        #关闭队列

#消息队列
# from multiprocessing import Process,Queue
# import time
# #创建消息队列
# q = Queue()
# def fun1():
# 	time.sleep(1)
# 	q.put({'a':1})
# def fun2():
# 	time.sleep(2)
# 	print(q.get())
# p1=Process(target = fun1)
# p2=Process(target = fun2)
# p1.start()
# p2.start()
# p1.join()
# p2.join()

#共享内存
# from multiprocessing import Process,Value
# import time
# import random
# #创建共享内存
# money = Value('i',2000)

# def deposite():
# 	for i in range(100):
# 		time.sleep(0.05)
# 		#对value属性操作即操作共享内存数据
# 		money.value += random.randint(1,200)
# def withdraw():
# 	for i in range(100):
# 		time.sleep(0.04)
# 		money.value -= random.randint(1,180)
# d = Process(target = deposite)
# w = Process(target = withdraw)
# d.start()
# w.start()
# d.join()
# w.join()
# print('余额：', money.value)

#共享内存
# from multiprocessing import Process,Array
# import time
# #创建共享内存，初始放入列表
# # shm = Array('i',[1,2,3,4,5])
# #创建共享内存，开辟5个整形空间
# # shm = Array('i',5)
# #存入字符串,要求是bytes格式
# shm = Array('c',b'Hello')
# def fun():
# 	for i in shm:
# 		# shm[3] = 100      #子进程修改，父进程可以打印出来修改后内容
# 		shm[0] = b'h'
# p = Process(target = fun)
# p.start()
# p.join()
# #遍历整形
# # for i in shm:
# # 	print(i)	
# print(shm.value) #打印字符串

#信号通信
# import os
# import signal
# #向20959发送信号
# os.kill(20959,signal.SIGKILL)   #输出已杀死

# import signal
# import time
# signal.alarm(3)    #输出闹钟
# time.sleep(2)
# signal.alarm(5)    #第二个如果执行会覆盖第一个时间
# while True:
# 	time.sleep(1)
# 	print("sleep")

#信号修改
# import signal
# from time import sleep
# signal.alarm(5)
# #使用默认信号
# # signal.signal(signal.SIGALRM,signal.SIG_DFL)
# #忽略信号
# signal.signal(signal.SIGALRM,signal.SIG_IGN)
# while True:
# 	sleep(2)
# 	print("wait")

# from signal import *
# import time
# #信号处理函数
# def handler(sig,frame):
# 	if sig == SIGALRM:
# 		print("接收到时钟信号")
# 	else:
# 		print("就不结束")
# alarm(5)
# signal(SIGALRM,handler)       #接收到信号，将信号传给函数第一个形参，再调用函数
# signal(SIGINT,handler)
# while True:
# 	time.sleep(2)
# 	print("wait")

#信号量   第一次打印7句，第二次打印4句，第3次打印2句 
# from multiprocessing import Semaphore,Process
# from time import sleep
# import os
# #创建信号量
# sem = Semaphore(3)
# def fun():
# 	print("1进程%d等待信号量"%os.getpid())   #4遍
# 	#消耗一个信号量
# 	sem.acquire()
# 	print("2进程%d消耗信号量"%os.getpid())   #3+1遍
# 	sleep(3)
# 	sem.release()
# 	print("3进程%d添加信号量"%os.getpid())  #3+1遍
# jobs = []
# for i in range(4):
# 	p = Process(target = fun)
# 	jobs.append(p)
# 	p.start()
# for i in jobs:
# 	i.join()
# print(sem.get_value())

#同步，共同操作一个临界区，人为设置操作顺序
# from multiprocessing import Event,Process
# from time import sleep
# def wait_event():
# 	print('想操作临界区')
# 	e.wait()
# 	print('开始操作临界区资源',e.is_set())
# 	with open('file') as f:
# 		print(f.read())
# def wait_timeout_event():
# 	print('也想操作临界区')
# 	e.wait(2)
# 	if e.is_set():
# 		with open('file') as f:
# 			print(f.read())
# 	else:
# 		print('不能读取文件')
# #事件对象
# e = Event()
# p1 = Process(target = wait_event)
# p1.start()
# p2 = Process(target = wait_timeout_event)
# p2.start()
# print('主进程操作')
# sleep(3)
# with open('file','w') as f:
# 	f.write('I love China')
# e.set()
# print('释放临界区')
# p1.join()
# p2.join()

# #互斥，锁控制进程执行顺序
# from multiprocessing import Process,Lock
# import sys
# from time import sleep
# lock = Lock()
# def writer1():
# 	lock.acquire()
# 	for i in range(20):
# 		sleep(0.05)
# 		sys.stdout.write('1我想向终端写入\n')
# 	lock.release()
# def writer2():
# 	lock.acquire()
# 	for i in range(20):
# 		sleep(0.05)
# 		sys.stdout.write('2我想向终端写入\n')
# 	lock.release()
# w1 = Process(target = writer1)
# w2 = Process(target = writer2)
# w1.start()
# w2.start()
# w1.join()
# w2.join()


#创建线程
# import threading
# from time import sleep
# import os
# a = 1
# #线程函数
# def music():
# 	global a                          #修改全局变量，不加会报错
# 	print('分支线程a = ', a)
# 	for i in range(2):
# 		sleep(1)
# 		print('listen music')
# 	a = 100
# #创建线程对象
# t = threading.Thread(target = music)
# t.start()
# t.join()
# print('主线程a =',a)                  #主线程和分支线程使用的是同一个进程的资源和空间

# #线程锁
# import threading
# from time import sleep
# s = None
# e = threading.Event()
# def bar():
# 	print("bar1")
# 	global s
# 	s = "anhao"
# def foo():
# 	print('koulig')
# 	sleep(2)
# 	if s == "anhao":
# 		print('zijierne')
# 	else:
# 		print('zouta')
# 	e.set()    #验证完毕在执行
# def fun():
# 	print("hehe")
# 	sleep(1)
# 	global s
# 	s = "xiaoji"
# b = threading.Thread(target = bar)
# f = threading.Thread(target = foo)
# b.start()
# f.start()
# e.wait()   #运行bf之后其他内容不准许执行
# fun()
# b.join()
# f.join()

# import threading
# a = b = 0
# lock = threading.Lock()
# def value():
# 	while True:
# 		lock.acquire()     #可以上锁，如果有锁存在则阻塞
# 		if a != b:
# 			print('no equel')
# 		lock.release()     #解锁
# t = threading.Thread(target = value)
# t.start()
# while True:
# 	with lock:           #可以上锁，如果有锁存在则阻塞
# 	a += 1
# 	b += 1
# t.join()


#多进程基于fork完成多进程网络并发，发送消息
# from socket import *
# import os,sys
# #客户端处理函数
# def client_handler(c):
# 	print('client:',c.getpeername())
# 	while True:
# 		data = c.recv(1024)
# 		if not data:
# 			break
# 		print(data.decode())
# 		c.send(b'Receive your message')
# 	c.close()
# 	sys.exit(0)   #将子进程销毁
# #创建套接字
# HOST = '0.0.0.0'
# PORT = 8888
# ADDR = (HOST,PORT)
# #创建tcp套接字
# s = socket()  
# #套接字重用
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind(ADDR)
# s.listen(5)
# #循环等待客户端退出
# print('listen to the port 8888...')
# while True:
# 	try:
# 		c,addr = s.accept()
# 	except KeyboardInterrupt:
# 		sys.exit('exit server')
# 	except Exception as e:
# 		print('Error',e)
# 		continue
# #创建新的进程处理客户端请求
# 	pid = os.fork()
# #子进程处理客户端请求，因为在循环里，所以循环也是fork之后的语句
# 	if pid == 0:
# 		p = os.fork()  #创建子进程处理僵尸进程
# 		if p == 0:
# 			s.close()
# 			client_handler(c)
# 		else:
# 			os.exit(子进程未创建成功)
# #父进程或者创建进程失败都继续邓艾下个客户端连接	
# 	else:
# 		c.close()
# 		os.wait('子进程退出处理') #处理退出子进程
# 		continue

# #tcp客户端
# from socket import *
# #创建套接字
# sockfd = socket(AF_INET, SOCK_STREAM)
# #发起连接
# server_addr = ('127.0.0.1', 8888)
# sockfd.connect(server_addr)
# #消息发送接收
# while True:
#     data = input("发送>>")
#     if not data:
#         break
#     sockfd.send(data.encode())
#     data = sockfd.recv(1024)
#     print("接受到", data.decode())
# #关闭套接字
# sockfd.close()

# #ftp服务器,未完成，自己写
# from socket import *
# import os,sys,time,signal
# #定义全局变量
# file_path = '/root/'
# host = '0.0.0.0'
# port = 8888
# addr = (host,port)
# #将文件服务器功能写在类中
# class Ftpserver(object):
# 	pass
# #创建套接字，接收客户端连接，创建新的进程
# def main():
# 	sockfd = socket()
# 	sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# 	sockfd.bind(ADDR)
# 	sockfd.listen(5)
# 	#处理子进程退出
# 	signal.signal(signal.SIGCHLD,signal.SIG_IGN)  #忽略该信号
# 	print('listen the port 8000...')
# 	while True:
# 		try:
# 			connfd,addr = s.accept()
# 		except KeyboardInterrupt:
# 			sockfd.close()
# 			sys.exit('exit server')
# 		except Exception as e:
# 			print('Error',e)
# 			continue
# 		print('connect server',addr)
# 		#创建子进程
# 		pid = os.fork()
# 		if pid == 0:
# 			sockfd.close()
# 			pass
# 		else:
# 			connfd.close()
# 			continue

# if __name__ == '__main__':
# 	main()



# #ftp客户端
# from socket import *
# import sys
# import time
# class Ftpclient():
# 	pass


# import traceback
# a = 10
# try:
#  	b = a / 0
# except Exception as e:
#  	# print(e)
#  	traceback.print_exc()
# print('程序打印完毕')

#集成模块的使用
# from socketserver import *
# #创建服务器类
# class Server(ForkingMixIn,TCPServer):
# 	pass
# class Handler(StreamRequestHandler):
# 	def handle(self):
# 		#self.request ==> accept 返回的套接字
# 		print("connect from",\
# 			self.request.getpeername())
# 		while True:
# 			data = self.request.recv(1024)
# 			if not data:
# 				break
# 			print(data.decode())
# 			self.request.send(b'receive')
# if __name__ == '__main__':
# 	server_addr = ('0.0.0.0',8888)
# 	#创建服务器对象
# 	server = Server(server_addr,Handler)   
# 	#启动服务器
# 	server.serve_forever()               #自动监听地址server_addr，调用Handler处理请求

#udp收发消息
# data = self.rfile.readline()
# self.wfile.write()

#协程greenlet
# from greenlet import greenlet
# def test1():
# 	print(123)
# 	gr2.switch()
# 	print(789)
# def test2():
# 	print(222)
# 	gr1.switch()
# 	print(666)
# #协程对象
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
# gr1.switch()

#gevent
# import gevent
# from time import sleep
# def foo(a,b):
# 	print('a = %d,b = %d'%(a,b))
# 	gevent.sleep(2)                     #协程特有阻塞条件
# 	print('running foo again')
# def bar():
# 	print('running in bar')
# 	gevent.sleep(3)
# 	print('running bar again')
# #生成协程
# f = gevent.spawn(foo,1,2)
# g = gevent.spawn(bar)
# # sleep(3)
# print('=====')
# gevent.joinall([f,g])        #设置协程阻塞，触发阻塞，阻塞自动跳转

#gevent协程服务器，协程通过加载多次handler(加载成多个协程空间)
# import gevent
# from gevent import monkey
# monkey.patch_all()
# from socket import *
# from time import ctime
# def server(port):
# 	s=socket()
# 	s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# 	s.bind(('0.0.0.0',port))
# 	s.listen(3)
# 	while True:
# 		c,addr = s.accept()
# 		print('connect from',addr)
# 		# handler(c)              #循环服务器
# 		gevent.spawn(handler,c)   #协程服务器
# def handler(c):
# 	while True:
# 		data = c.recv(1024)
# 		if not	data:
# 			break
# 		print(data.decode())
# 		c.send(ctime().encode())
# 	c.close()
# if __name__ == '__main__':
# 	server(8888)

#普通tcp客户端
# from socket import *
# #创建套接字
# sockfd = socket(AF_INET, SOCK_STREAM)
# #发起连接
# server_addr = ('127.0.0.1', 8888)
# sockfd.connect(server_addr)
# #消息发送接收
# while True:
#     data = input("发送>>")
#     if not data:
#         break
#     sockfd.send(data.encode())
#     data = sockfd.recv(1024)
#     print("接受到", data.decode())
# #关闭套接字
# sockfd.close()
