from flask import *

app=Flask(__name__)


# @app.route('/01-ajax')
# def xhr():
#     return render_template('01-ajax.html')

# #a,get
# @app.route('/02-ajax')
# def ajax_get():
#     return render_template('02-ajax.html')

# @app.route('/02-server')
# def server02():
#     return "这是我的第一个ajax请求"

# #a,带参数get
# @app.route('/01-ajax')
# def get_param():
#     return render_template('01-ajax.html')

# @app.route('/03-server')
# def server03():
#     uname = request.args.get('uname')
#     return "欢迎：%s" % uname


#a post
# @app.route('/01-ajax')
# def post():
#     return render_template(01-ajax.html)

# @app.route('/04-server',methods=['POST'])
# def server04():
#     uname=request.form['uname']
#     age = request.form['age']
#     return "姓名:%s,年龄:%s" % (uname,age)






if __name__ == '__main__':
    app.run(debug=True)