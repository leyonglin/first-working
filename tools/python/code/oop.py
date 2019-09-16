
# class Dog:                                                   #创建类
# 	def eat(self, food):                                     #创建实例方法(共性),self被赋值为实例对象
# 		print(self.color, '的', self.kinds, '正在吃', food)   #可以调用实例属性
# 		self.food=food                                       #保存对象自己的数据(个性)，该属性由dog1.eat('骨头') 执行后赋值的，和dog1.kinds='二哈'作用是一样的
# 	def show_food(self):
# 		# print(self.color, '的', self.kinds, '正在吃1', food) #会失败，显示food未定义  
# 		print(self.color, '的', self.kinds, '上次吃的是', self.food)

# dog1=Dog()                                                   #创建实例对象
# dog1.kinds='二哈'                                            #实例属性赋值
# dog1.color='白色'                                            #实例属性赋值
# print(dog1.color, '的', dog1.kinds)                          
# dog1.eat('骨头')                       
# dog1.show_food()                                             


# class A:
# 	v=0                    #类变量(属性)
# 	@classmethod
# 	def get_v(cls):
# 		return cls.v         #用cls访问类变量v
# 	@classmethod
# 	def set_v(cls,a):
# 		cls.v=a
# 		# print(cls.color)    类方法不能访问此类创建的对象的实例属性
# print('A.v=', A.get_v())   #调用类方法得到类变量的值
# A.set_v(100)               #使用方法调用改变类变量的值
# print('A.v=', A.get_v())
# # a.color = '白色'

# class A:
# 	@staticmethod            #静态方法
# 	def myadd(a, b):         #第一个形参不用是self,就像普通函数一样
# 		return a+b
# print(A.myadd(100,200))      #调用方式：类名.函数()
	
# class Human:
# 	def say(self, what):
# 		print("说", what)
# class Student(Human):
# 	def study(self, subject):
# 		print("正在学习", subject)
# h1=Student()
# h1.say("good")
# h1.study("python")


# class A:
# 	def work(self):
# 		print("A.work被调用")
# class B(A):
# 	def work(self):
# 		print("B.work被调用!!!")
# 	def super_work(self):
# 		self.work()                  #调用B类方法
# 		super(B, self).work()         #调用方法
# 		super().work()               #必须在方法内调用
# b=B()
# b.work()              #B被调用
# super(B, b).work()    #A.work被调用

		
# class Human:
# 	def __init__(self, n, a):
# 		self.name = n
# 		self.age = a
# 		print("Human类的初始化方法被调用...")
# 	def infos(self):
# 		print("姓名", self.name)
# 		print("年龄", self.age)
# class Student(Human):
# 	def __init__(self, n, a, s=0):                #s1=Student('张飞', 15, 80)调用该初始化方法，默认覆盖父类同名方法
# 		super(Student, self).__init__(n,a)        #将n，a传到父类初始化方法并调用
# 		self.score=s
# 		print("Student的初始化方法被调用...")

# s1=Student('张飞', 15, 80)
# s1.infos()


# class A:
# 	def __init__(self):
# 		self.__p1 = 100     #私有属性
# 		# self._p2 = 200      #不是私有属性
# 		# self.__p3__ = 300   #不是私有属性
# 	def show_info(self):
# 		print(self.__p1)    #此对象的实例方法可以访问和修改私有属性
# 		self.__m()            #调用私有方法
# 	def __m(self):
# 		print("A类对象的__m方法被调用")			
# a = A()
# a.show_info()     #只能使用该类的方法进行访问和修改
# # print(a.__p1)   #外部不允许访问私有属性
# # print(a._p2)    #可以访问
# # print(a.__p3__) #可以访问
# # a.__m()           #无法直接访问私有方法

# class Shape:
# 	def draw(self):
# 		print("Shape的draw()被调用")
# class Point(Shape):
# 	def draw(self):
# 		print('正在画一个点！')
# class Circle(Point):
# 	def draw(self):
# 		print('正在画一个圆！')
# def my_draw(s):
# 	s.draw()     #c++等语言有静态(编译时状态)，编译时会根据s的类型调用相应方法，python是弱类型的，因此只能在运行时，根据对象才能决定调用那个方法

# s1=Circle()
# my_draw(s1)

# s="I'm Teacher"
# print(str(s))
# print(repr(s))

# class MyNumber:
# 	def __init__(self, val):
# 		self.data = val
# 	# def __str__(self):
# 	# 	return "自定义数字： %d" % self.data
# 	# def __repr__(self):                          #此方法返回来的字符串一定是能表示self对象的表达式字符串
# 	# 	return "MyNumber(%d)" % self.data
		
# n1 = MyNumber(100)
# print('str(n1) =', str(n1))
# print(n1.__str__())
# print(n1)                    #在print内部会将n2用str(x)转为字符串再写到sys.stdout
# print('repr(n1 =', repr(n1))

# class MyList:
# 	def __init__(self, iterable=()):
# 		self.__data = [x for x in iterable]     #私有属性
# 	def __repr__(self):
# 		return 'MyList(%s)' % self.__data
# 	def __len__(self):
# 		return len(self.__data)
# myl = MyList([1, 0, 2, -1])
# print(myl)
# print(len(myl))                                #len()内建函数，需要上面的函数重写，自定义的类创建的实例才能够使用内建函数进行操作

# #此示例将自定义的类MyList创建的对象制作称为可迭代对象
# class MyList:
# 	def __init__(self, iterable=()):
# 		self.__data = [x for x in iterable]     #私有属性
# 	def __repr__(self):
# 		return 'MyList(%s)' % self.__data
# 	def __iter__(self):         #此方法用于返回一个能访问self对象的迭代器
# 		print("被调用")
# 		return MyListIterator(self.__data)    #返回跌掉其，是因为由__next__方法
# class MyListIterator:              #此类用来描述能够访问MyList类型的对象的迭代器
# 	def __init__(self,lst):
# 		self.data_lst=lst 
# 		self.cur_index=0          #迭代器访问的起始位置
# 	def __next__(self):           #此方法用来实现迭代器协议
# 		if self.cur_index >= len(self.data_lst):
# 			raise StopIteration
# 		r = self.data_lst[self.cur_index]
# 		self.cur_index += 1
# 		return r

# myl = MyList([1, 0, 2, -1])
# it = iter(myl)                #等同于调用it=myl.__iter__()
# print(next(it))
# for x in myl:                 #TypeError: 'MyList' object is not iterable
# 	print(x)

# class A:         #此类的对象可以用于with语句进行管理
# 	def __enter__(self):                    #第一步，进入with语句
# 		print("此方法是在with语句内执行的")  
# 		return self   #self将被with中的as变量绑定
# 	def __exit__(self, exc_type, exc_val, exc_tb):
# 		print("您已离开with语句")           #第三步，退出with语句
# with A() as a:                     
# 	print("这是with语句内部输出")            #第二步
# print("程序正常执行")                       #第四步

# class MyNumber:
# 	def __init__(self, v):
# 		self.data = v      #self.data用来保存对象的数据
# 	def __repr__(self):
# 		return "MyNumber(%d)" % self.data
# 	# def add(self, other):          #定制self+other的规则
# 	# 	v = self.data + other.data
# 	# 	return MyNumber(v)
# 	def __add__(self, other):          #特殊的方法名，是n3 = n1 + n2，能执行并且不报错
# 		return MyNumber(self.data + other.data)

# n1 = MyNumber(100)
# n2 = MyNumber(200)
# # n3 = n1.add(n2)
# n3 = n1 + n2   #等同于n3=n1.__add__(n2)
# print(n3)

# class MyList:
# 	def __init__(self, iterable=()):
# 		self.data = [x for x in iterable]  
# 	def __repr__(self):
# 		return 'MyList(%s)' % self.data
# 	def __neg__(self):                  #负号运算符重载
# 		G = (-x for x in self.data)
# 		return MyList(G)

# L1 = MyList([1,-2,3,-4,5])
# L2 = -L1
# print(L2)


# class MyList:
# 	def __init__(self, iterable=()):
# 		self.data = [x for x in iterable]  
# 	def __repr__(self):
# 		return 'MyList(%s)' % self.data


# L1=MyList([1,-2,3,-4,5])
# if 1 in L1:                  #等同于if not L1.__contains__(4)
# 	print("2在L1内")
# else:
# 	print('2不在L1内')

# class Student:
# 	def __init__(self, s):
# 		self.__score=s
# 	@property
# 	def score(self):			#getter用来获取数据
# 		print("getter被调用")   #作用和getscore的函数一样
# 		return self.__score
# 	# def getscore(self):         #获取数据
# 	# 	return self.__score 	
# 	@score.setter
# 	def score(self, s):      #此方法使用setter，用来设置值加以限制以保证数据的准确性
# 	# def setscore(self, s)
# 		print("setter被调用")
# 		if 0<= s <= 100:
# 			self.__score=s

# s = Student(50)
# # s.setscore(100)
# score = s.score                 #访问特性属性score,实质是调用原s.getscore()
# print('成绩是：', score)
# s.score=100                     #修改特性属性score的值,实质是调用原s.setscore()
# print('成绩是：', score)

# class MyList:
#     def __init__(self, iterable=()):
#         self.__data = list(iterable)               #可以用别的数据类型
#     def __repr__(self):
#         return "MyList(%s)" % self.__data
#     def __getitem__(self, i):
#         print('i的值是：', i)
#         return self.__data[i]
#     # def __setitem__(self,i,v):  
#     #     print("call __setitem__", i, v)
#     #     self.__data[i] = v
#     # def __delitem__(self,i):
#     #     self.__data.pop(i)

# L = MyList([1, -2, 3, 5, 6])
# # x = L[1]                                            #调用__getitem__方法
# # print(x)
# # print(L)
# # L[3] = 400                                          #调用__getitem__方法
# # print(L)
# # del L[3]
# # print(L)                                            #调用__delitem__方法
# print(L[::2])                                         #等同于printL[slice(None, None, 2)]
 