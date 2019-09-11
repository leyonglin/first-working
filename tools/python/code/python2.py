
# def power2(x):
# 	return x**2

# for x in map(power2, range(1, 10)):
# 	print(x)

# print(sum(map(lambda x: x**2, range(1, 10))))
# def mypow(x,y):
# 	return x**y
# for i in map(mypow,[1,2,3,4],(4,3,2,1)):
# 	print(i)

L=[1,-2,5,-3]
L1=sorted(L,key=abs,reverse=True)
print(L1)