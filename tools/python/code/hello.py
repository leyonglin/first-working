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

































