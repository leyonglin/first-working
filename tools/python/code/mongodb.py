from pymongo import MongoClient
#创建数据库连接
conn = MongoClient('localhost',27017)
#创建数据库对象
db = conn.stu
#创建集合对象
myset = db.class1
#数据库操作

# print(dir(myset))  #查看提供的方法
# myset.insert({'name':'林','king':'皇帝'})
#插入多条记录(列表)
# myset.insert_many([{'name':'wang','juese':'baobao'},{'name':'wang','juese':'laopo'}])
#查找操作find(),返回一个结果游标对象
cursor = myset.find({},{'_id':0})
# print(cursor)
for i in cursor:
	print(i)
	print(i['name'],i['king'])

#关闭连接
conn.close()