
from flask import *
#将SQLAlchemy模块导入进来
from flask_sqlalchemy import SQLAlchemy
#将当前运行的主程序构建成Flask应用，以便接受用户的请求(request)并给出响应(response)
app = Flask(__name__)

#为app指定数据库的配置信息
app.config['SQLALVHEMY_DARABASE_URI']='mysql//root:123456@192.168.3.5:3306/flask'
#创建SQLAlchemy的实例，并将app指定给实例,表示程序正在使用的数据库，具备SQLAlchemy中的所有功能
db = SQLAlchemy(app)

#@app.route，Flask中的路由定义，只要定义用户的访问路径。'/'表示整个网站的根路径,必须从根开始
# @app.route('/')
#表示匹配@app.route()路径后的处理程序-视图函数，所有的属兔函数必须有return返回值，可以使字符串或者响应对象
# def index():
#     return 'hello'

#带一个参数的路由,<hello>和函数形参名称需保持一致
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
@app.route('/')
def index():
	return "hello world"









if __name__ == '__main__':
	#运行Flask应用(启动Flask服务) debug在开发是用True，生产环境用False
    app.run(debug=True,port=5000,host='0.0.0.0')