# from pymongo import MongoClient
# #创建数据库连接
# conn = MongoClient('localhost',27017)
# #创建数据库对象
# db = conn.stu
# #创建集合对象
# myset = db.class1
# #数据库操作
# # print(dir(myset))  #查看提供的方法


# #插入数据
# # myset.insert({'name':'林','king':'皇帝'})
# # myset.insert_many([{'name':'wang','juese':'baobao'},{'name':'wang','juese':'laopo'}])   #插入多条记录(列表)

# #查找操作find(),返回一个结果游标对象
# # dic = myset.find_one({},{'_id':0})       #返回一个字典{'name': '林', 'king': '皇帝'}
# # print(dic)
# # cursor = myset.find({},{'_id':0})        #返回对象，类似迭代器一样<pymongo.cursor.Cursor object at 0x7f0b3ebc7ba8>
# # print(cursor)      
# # for i in cursor:
# # 	print(i)
# # 	print(i['name'],i['king'])

# #操作符使用
# # myset1 = db.class1
# # cursor = db.class1.find({'a':{$gt:'5',$lt:'8'}},{_id:0})

# #总结：在pymongo中所有操作符的用法同mongo shell相同,只是操作时加引号
# #cursor对象属性。next()  limit()  skip()  count()  sort()
# #for 或者 next 使游标位置不再指向原来的位置，调用limit skip  sort等会报错


# #关闭连接
# conn.close()



#将文件以grid方案存放到数据库(大文件,即>16M)
# from pymongo import MongoClient
# import gridfs
# conn = MongoClient('localhost',27017)
# #grid库
# db = conn.grid
# #获取gridfs对象
# fs = gridfs.GridFS(db)

# f = open('mm.jpg','rb')         #要求存入一定要是二进制的
# #将内容写入到数据库
# fs.put(f.read(),filename = 'mm.jpg')
# conn.close()

#取出数据库文件
# from pymongo import MongoClient
# import gridfs
# conn = MongoClient('localhost',27017)
# #grid库
# db = conn.grid
# #获取gridfs对象
# fs = gridfs.GridFS(db)
# files = fs.find()          #得到文件集合对象
# for i in files:
# 	# print(i)        		#获取文件对象
# 	print(i.filename)      #打印出每个文件的名称
# 	if i.filename == 'mm.jpg':
# 		with open(i.filename,'wb') as f:
# 			#从数据库读取内容
# 			data = i.read()
# 			#写入到本地
# 			f.write(data)
# conn.close()


# #小文件存储方案，直接转换二进制格式插入到数据库
from pymongo import MongoClient
import bson.binary
conn = MongoClient('localhost',27017)
#进入image数据库
db = conn.image
myset = db.mm

# #存储图片
# f = open('mm.jpg','rb')
# #将图片内容转换为可存储的二进制格式
# content = bson.binary.Binary(f.read())
# #插入文档,存入名为mm.jpg的图片
# myset.insert({'filename':'mm.jpg','data':content})
# conn.close()

#提取图片
img = myset.find_one({'filename':'mm.jpg'})
#将内容写入到本地
with open('mm.jpg','wb') as f:
	f.write(img['data'])
conn.close()