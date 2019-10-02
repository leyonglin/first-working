from flask import Flask
#将当前运行的主程序构建成Flask应用，以便接受用户的请求(request)并给出响应(response)
app = Flask(__name__)

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
# def index(page=None):
# 	if page is None:
# 		page = 1
# 	return "您当前看的页数为:%d" % page

 
if __name__ == '__main__':
	#运行Flask应用(启动Flask服务) debug在开发是用True，生产环境用False
    app.run(debug=True)