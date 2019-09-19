
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

