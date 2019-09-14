
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


















