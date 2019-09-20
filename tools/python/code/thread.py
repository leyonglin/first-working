
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
