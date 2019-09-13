
class Dog:                                                   #创建类
	def eat(self, food):                                     #创建实例方法(共性),self被赋值为实例对象
		print(self.color, '的', self.kinds, '正在吃', food)   #可以调用实例属性
		self.food=food                                       #保存对象自己的数据(个性)，该属性由dog1.eat('骨头') 执行后赋值的
	def show_food(self):
		print(self.color, '的', self.kinds, '上次吃的是', self.food)

dog1=Dog()                                                   #创建实例对象
dog1.kinds='二哈'                                            #实例属性赋值
dog1.color='白色'                                            #实例属性赋值
print(dog1.color, '的', dog1.kinds)                          
dog1.eat('骨头')                       
dog1.show_food()                                             
