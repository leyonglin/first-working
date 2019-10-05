
#程序流程就是，该程序运行，启动一个应用程序，监听一个端口，客户端访问，则会执行响应的程序。如果执行完的程序中负责渲染的html跳转到其它url，也会先返回该主程序找到对应的执行代码
from flask import *
#将SQLAlchemy模块导入进来
from flask_sqlalchemy import SQLAlchemy
#支持原生的mysql操作，伪装成MYSQLdb
import pymysql
pymysql.install_as_MySQLdb()
#将当前运行的主程序构建成Flask应用，以便接受用户的请求(request)并给出响应(response)
app = Flask(__name__)

#为app指定数据库的配置信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/flask'
#自动提交，即省略db.session.commit()
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
#创建SQLAlchemy的实例，并将app指定给实例,表示程序正在使用的数据库，具备SQLAlchemy中的所有功能
db = SQLAlchemy(app)

#@app.route，Flask中的路由定义，只要定义用户的访问路径。'/'表示整个网站的根路径,必须从根开始
# @app.route('/')
#表示匹配@app.route()路径后的处理程序-视图函数，所有的属兔函数必须有return返回值，可以使字符串或者响应对象
# def index():
#     return 'hello'

#带一个参数的路由,<hello>和函数形参名称需保持一致
#报错：ValueError: urls must start with a leading slash，是因为route路径不是从根开始少了一个/,即写成show/<hello>，
# @app.route('/show/<hello>')
# def show(hello):
# 	return "<h1>传递进来的参数为:%s</h1>" % hello

#带多个参数,
# @app.route('/show/<name>/<age>')
# def show(name,age):
# 	return "<h1>姓名:%s,年龄:%s</h1>" % (name,age)

#指定参数类型的路由
# @app.route('/show/<name>/<int:age>')
# def show(name,age):
# 	return "<h1>姓名:%s,年龄:%d</h1>" % (name,age)

#多url,分页
# @app.route('/')
# @app.route('/<int:page>')
# page可传可不传
# def index(page=None):
# 	if page is None:
# 		page = 1
# 	return "您当前看的页数为:%d" % page

#url反向解析
# @app.route('/index')
# def index():
#  	return "这是首页"
# @app.route('/index/<name>')
# def show(name):
# 	return "参数的值为:%s" % name
# @app.route('/url')
# def url():
# 	#通过index()解析出对应的访问路径
# 	url_index = url_for('index')
# 	print('index():'+url_index)
# 	#通过show(name)解析出对应的访问路径
# 	url_show = url_for('show',name='jiayao')
# 	print('show(name):'+url_show)
# 	return "<a href=%s>访问show(name)</a>" % url_show



#Templates
#将01-template.html渲染成字符串再响应给客户端
# @app.route('/01-template')
# def template():
# 	#渲染01-template.html,并且传递变量
# 	return render_template('01-template.html',name="隔壁老王")

#template多参数传参
# @app.route('/01-template')
# def template():
# 	dic = {
# 		'music':'绿光',
# 		'author':'宝强'
# 	}
# 	return render_template('01-template.html',params=dic)

#多参数传参2
# @app.route('/01-template')
# def template():
# 	music='绿光'
# 	author='宝强'
# 	print(locals())
# 		#locals()将当前函数内变量封装成一个字典
# 	return render_template('01-template.html',params=locals())

#其它参数类型
# @app.route('/01-template')
# def template():
# 	music=['1','2','3']
# 	author=('4','5','6')
# 	name={'aa':'bb','cc':'dd'}

# 	print(locals())
# 		#locals()将当前函数内变量封装成一个字典
# 	return render_template('01-template.html',params=locals())


#过滤器
# @app.route('/01-template')
# def template():
# 	uname = 'my name is jiayao'
# 		#locals()将当前函数内变量封装成一个字典
# 	return render_template('01-template.html',params=locals())

#流程控制 if
# @app.route('/01-template')
# def if_views():
# 	return render_template('01-template.html')
# @app.route('/user/login')
# def login():
# 	return "模拟登陆地质"

#流程控制for
# @app.route('/01-template')
# def for_views():
# 	list = ["1","2","3","4","5"]
# 	dic = {
# 		"a":"a1",
# 		"b":"b1",
# 		"c":"c1",
# 		"d":"d1",
# 	}
# 	return render_template('01-template.html',params=locals())

#macro
# @app.route('/01-template')
# def for_views():
# 	list = ["1","2","3","4","5"]
# 	return render_template('01-template.html',params=locals())



#http_request：from flask import request
# @app.route('/01-template')
# def request_views():
# 	#查看有什么方法
#     print (dir(request)) 
#     #查看http相应方法的内容   
#     args = request.args
#     cookies = request.cookies
#     return render_template('01-template.html',params=locals())


#models，与数据库交互
#创建模型类-Models
#创建Users类，映射到数据库中叫users表
class Users(db.Model):
    __tablename__="users"
#创建字段：id，主键和自增
    id=db.Column(db.Integer,primary_key=True)
#创建字段：username，长度为80的字符串，不允许为空，值必须唯一
    username=db.Column(db.String(80),nullable=False,unique=True)
#创建字段：age，整数，允许为空
    age=db.Column(db.Integer,nullable=True)
#创建字段：email，长度为120的字符串，必须唯一
    email=db.Column(db.String(120),unique=True)
#初始化传入的参数，在这里是为了传入的字段值
    def __init__(self,username,age,email):
    	self.username = username
    	self.age = age
    	self.email = email

    #函数重写
    def __repr__(self):
        return "<Users:%r>" % self.username


#将创建好的实体类映射回数据库
db.create_all()


#访问则会提交下列数据
# @app.route('/')
# def index():
# 	#创建Users对象并赋值
# 	user = Users('jiayao','33','aaaa@163.com')
# 	#添加行数据
# 	db.session.add(user)
# 	db.session.commit()
# 	return "hello world"


#从01-template页面获取用户输入数据并提交到数据库
# @app.route('/01-template',methods=['POST','GET'])
# def register_views():
#     if request.method == 'GET':
#         return render_template('01-template.html')
#     else:
#         username = request.form.get('username')
#         age = request.form.get('age')
#         email = request.form.get('email')
#         user = Users(username,age,email)
#         db.session.add(user)
#         return "Register ok"

#查询
# @app.route('/01-template')
# def query_views():
#     #测试query()函数
#     # print(db.session.query(Users))
#     # print(db.session.query(Users,Course))
#     # print(db.session.query(Users.username,Users.email))
#     users = db.session.query(Users).all()        #查询执行函数,下面结果是因为重写__repr__函数
#     for user in users:
#         print("姓名:%s，年龄:%d,邮箱:%s" % (user.username,user.age,user.email))
#     #执行多项查询
#     query = db.session.query(Users)
#     user = query.first()
#     print(user)
#     count = query.count()
#     print('共有%d条数据' % count)
#     return "Query OK"


#过滤器函数
# @app.route('/01-template')
# def queryall_views():
#     #查询过滤器函数-filter()
#     #查询年龄大雨30的Users的信息
#     result = db.session.query(Users).filter(Users.age > 30).all()
#     print(result)
    # return "Query OK"


# #使用Models查询数据
# @app.route('/01-template')
# def query_models():
#     user = Users.query.filter(Users.id==1).first()
#     # user = Users.query.filter_by(id=3).first()
#     print(user)
#     return "Query OK"


#a在网页中以表格的形式打印出来
# @app.route('/01-template')
# def queryall_views():
#     users = db.session.query(Users).all()
#     return render_template('01-template.html',users=users)

#完成a+b
@app.route('/02-template',methods=['GET','POST'])
def update_views():
    if request.method=='GET':
        #接收前端传递过来的用户id
        id = request.args.get('id','')
        # return "用户的🆔id为："+id
        #将id对应的应乎的信息读取出来
        # user = db.session.query(Users).filter(Users.id==id).first()
        user = db.session.query(Users).filter_by(id=id).first()
        #将读取出来的实体对象发送到02-template.html上显示,执行修改操作
        return render_template('02-template.html',user=user)
    else:
        #接收前端传递过来的四个值(id,username,age,email)
        id=request.form.get('id')
        username = request.form.get('username')
        age = request.form.get('age')
        email = request.form.get('email')
        user = Users(username,age,email)
        #根据id查询出对应的users信息
        user=Users.query.filter_by(id=id).first()
        #将username,age,email的值分别再赋值给user对应的属性
        user.username=username
        user.age=age
        user.email=email
        #将user的信息保存回数据库
        db.session.add(user)
        #响应：重定向回01-template
        return redirect('/01-template')




if __name__ == '__main__':
	#运行Flask应用(启动Flask服务) debug在开发是用True，生产环境用False
    app.run(debug=True,port=5000,host='0.0.0.0')