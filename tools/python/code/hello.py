# print("hello world")
#1.
# a=5
# b=6
# #a,b=b,a
# # print("a =",a)
# # print("b =",b)
# # help("__main__")
# print(id(a))
# print(a > b)
# 2.
# x=123.455
# b=123.45500001      
# print(round(x))
# print(round(x,2))
# print(round(b,2))    #因为计算机会先进行二进制转换在进行四舍五入
# print(round(x,-1))   #小数往左
# 3.
# x = -100
# print(abs(x))  #绝对值
# 4.
# s = input('请输入：')
# print('你输入:',s)
# 5.
# print(1,2,3,sep='#')
# print("hello world",sep="##")
# print(5,6,7,end='###\n')
# 6.
# hour = input("num:")
# print(hour * 60)       #字符串是可以相乘的
# hour = int(hour)
# print(hour * 60)
# if 100:
# 	print("Ture")
# s = 'aaa\nbbb'
# print(s)
# s1 = '''aaa   #三引号可以自动折行
# bbb'''
# print(s1)
# fmt = "name: %s, age: %d"
# s= fmt % ('lly', 35)
# print(s)
# pi=3.141592535897932
# print("-+%07.2f"  %  pi)
# s = int(input('请输入整数：'))
# i = 1
# j = 1 
# while j <= s:
# 	j +=1
# 	# i += 1/2**j
# 	print(1/2**j)
# i = int(input('请输入整数：'))
# j = 0
# while j < i:
#     print(' ' * j + '*' * (i-j))
#     j += 1

# for x in range(4,0,-1):
# 	print(x)

# i=6
# for x in range(1,i):          #这里的range只被调用一次
# 	print('x=',x,'i=',i)
# 	i -=1

# a = int(input('num:'))
# for x in range(1,a+1):        #该range只被掉用一次
# 	print('x=',x)
# 	for y in range(1,a+1):
# 		print(y,end=" ")
# 	print()
# 	x+2

# a=input('请输入')
# b=input('请输入')
# c=input('请输入')
# L=[]
# 1.
# L += a
# L += b
# L += c
# 2.
# L += [a]
# L += [b]
# L += [c]
# 3.
# L=[a,b,c]
# print(L)

# L = [1, 2, 3, 4]
# print(L[1::2])
# L[1::2] = "ab"
# #L[1::2] = "abc"    这个会报错，左右个数不一致
# print(L) 

# L = [1, 2, 3, 4]
# L2=L
# print(L,L2)
# L2[1] = 1000
# print(L,L2)

# import copy
# L=[3.1, 3.2]
# L1=[1,2,L]
# # L2=L1.copy()        #浅拷贝
# L2=copy.deepcopy(L1)  #深拷贝
# print(L,L1,L2)
# L2[2][0]=3.14
# print(L,L1,L2)

# begin=int(input('num1:'))
# end=int(input('num2:'))
# print([i for i in range(begin,end) if i % 2 ==0])

# s='1,2,3'
# print(s.split(','))
# print([int(i) for i in s.split(',')])

# d1=dict((['name', 'lin'], 'ab'))
# print(d1)
# d2=dict(name='lin', age=15)
# print(d2)

# d={1:'one', 2:'two',3:'three'}
# # for i in d.values():
# # for i in d.keys():
# for i,j in d.items():
# 	print(i,j)

# L=[]
# a=0
# b=1
# while len(L) < 40:
# 	L.append(b)
# 	a, b=b, a+b
# 	# c=a+b
# 	# a=b
# 	# b=c
# print(L)

# L=[1,1]
# while len(L) < 40:
# 	L.append(L[-1]+L[-2])
# print(L)
# print(set({1:1, 2:2}.items()))
# def say_hello():
# 	print("hello world")
# say_hello()
# v=say_hello()
# print(v)

# def myfun(a,b,c):
#   print(a,b,c)
# myfun(b=2,c=3,a=1)

# def myfun(a,b,c):
#   print(a,b,c)
# d1={'c':300, 'b':200, 'a':100}
# myfun(**d1)

# def myfun(a,b,c):
#   print(a,b,c)
# s1=[1,2]
# myfun(3,*s1)

# def func(a, b, *args):
# 	print(a, b)
# 	print(len(args), args)
# # func()
# func(0, 1, 2, 3)

# def mymax(a, *args):
# 	if not args:
# 		return max(a)
# 	else:
# 		return max(a, *args)
# print(mymax([6, 8, 3, 5]))
# print(mymax(1, 3, 5, 7))

# def myfun(a, *, b, c):
# 	print(a, b,c)
# myfun(1, b=2, c=3)

# def myfun2(a, *args, c, d):
# 	print(a, args, c, d)
# myfun2(1, 2, 3, c=5, d=6)
# myfun2(1, **{'d':4, 'c':3})

# def fun(**kwargs):
# 	print('num=', len(kwargs))
# 	print('kwargs=', kwargs)
# fun(name='lin', age=35, address='CN')
# fun(a=1, b='b', c=[2,3], d=True)

# def myfun(a,b,c):
#   print(a,b,c)
# s1={1,2,3}
# myfun(*s1)

# a=1
# def fx(b):
# 	c=3
# 	print(a,b,c)
# fx(2)


# a=1
# c=3
# def fn(c,d):
# 	e=300
# 	print('locals() 返回：', locals())
# 	print('globals() 返回：', globals())
# 	print(c,globals()['c'])
# fn(100,200)

# def fn():
# 	print("hello world")
# f1=fn
# print(f1,fn)
# print(f1())

# def f1():
# 	print('hello f1')
# def f2():
# 	print('hello f2')
# def fx(fn):
# 	print(fn)
# 	fn()	

# fx(f1)

# def myinput(fn):
# 	L = [1, 3, 5]
# 	return fn(L)
# print(myinput(max))

# def get_num():
# 	return max
# L=[1, 3, 5, 7]
# f=get_num()
# print(f(L))

# v=1
# def fn():
# 	global v
# 	# v=2
# fn()
# print(v)

# fx = lambda n: (n ** 2 + 1) % 5 == 0
# fx = lambda n: True if (n ** 2 + 1) % 5 == 0 else False
# print(fx(3))

s='1+2+3'  
print(exec(s))




































































































