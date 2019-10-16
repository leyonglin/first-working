from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
# Create your views here.
# def index_views(request):
#     return HttpResponse("这是网站首页")
# def login_views(request):
#     return HttpResponse("login_views")
# def register_views(request):
#     return HttpResponse("register_views")
from django.template import loader
from django.urls import reverse

from index.form import RemarkForm, WidgetForm1, WidgetForm2
from .models import *


# def temp_views(request):
#     #通过loader加载模板得到模板对象t
#     t = loader.get_template('01-template.html')
#     #将加载好的模板渲染成字符串,得到html
#     html = t.render()
#     #通过HttpRequest将字符串进行响应并返回
#     return HttpResponse(html)

# def temp_views(request):
#     return render(request,'01-template.html')

# def var_views(request):
#     name = "jiayao"
#     age = 30
#     gender = '女'
#     massage = "漂亮也是生产力"
#     tup = ("lin","jiayao","leyong","xihuan")
#     list=["shijian","haoba","you","1"]
#     dic = {
#     'name':'jiayao',
#     'age':30,}
#     show = showMsg()    
#     dog = Dog()
#     dog.name = "memeda"  
#     print(locals())
#     return render(request,'02-var.html',locals())

# def showMsg():
#     return "this is function"

# class Dog():
#     name = "jiayao"
#     age = 18

#     def eat(self):
#         return "xihuanwo"

# def static_views(request):
#     return render(request,'03-static.html')

# def add_views(request):
    # #通过entry.objects.create()实现数据的增加
    # try:
    #     author = Author.objects.create(name='MrWang',age=18,email='wangwc@163.com')
    #     print('ID:'+str(author.id))
    #     print('Name:'+author.name)
    #     print('age:'+str(author.age))
    # except Exception as e:
    #     print(e)

    #通过Entry对象的save()方法完成增加
    # author = Author(name='weilaoshi',age=35,email='wei@163.com')
    # author.save()


    #通过字典构建Entry对象并通过save()完成增加
    # dic = {
    #     'name':'哲学类',
    #     'age':18,
    #     'email':'laolv@123.com'
    # }
    # author = Author(**dic)
    # author.save()
    # print('新元素的id为:'+str(author.id))
    # return HttpResponse('Add zhe Ok')
    # return HttpResponse('add ok')

# def query_views(request):
    # #通过all()查询所有的数据
    # authors = Author.objects.all()
    # #print(authors.query)  #输出查询的语句
    # #print(authors)    #这里需要在models重写__repr__，输出看起来更方便
    # for author in authors:
    #     print('***********')
    #     print('ID:%d' % author.id)
    #     print('姓名:%s' % author.name)
    #     print('年龄：%d' % author.age)
    #     print('邮箱：%s' % author.email)

    #通过values()查询部分列的数据
    # author = Author.objects.values()
    # print(authors)
    # for author in authors:
    #     print('***********')
    #     print('姓名：%s' % author['name'])

    #通过filter()按条件筛选数据
    #查询id=1的Author的信息,无数据则为空列表
    # authors=Author.objects.filter(id=1)
    #查询id=1并且name='wang'的Author的信息,多条件用逗号隔开
    # authors=Author.objects.filter(id=1,name='wang')
    # return HttpResponse('query ok')

# def update_views(request):
#     #修改单个实体
#     # author=Author.objects.get(id=1)
#     # author.name='rapwang'
#     # author.save()
#     #批量修改
#     Author.objects.all().update(isActive=True)
#     return HttpResponse('update ok')

#查询数据库
# def queryall_views(request):
#     #查询Author实体中所有的数据
#     authors = Author.objects.all()
#     return render(request,'09-queryall.html',locals())

# def delete_views(request,id):
#     #id表示要删除的用户id
#     au = Author.objects.get(id=id)
#     au.delete()
#     #使用redirect()完成重定向
#     return HttpResponseRedirect('/09-queryall')

# def homework_views(request):
#     #查询年龄大于平均年龄的数据
#     avgAge = Author.objects.aggregate(avgAge=Avg('age'))['avgAge']
#     print(avgAge)
#     return HttpResponse('query ok') 


# def oto_views(request):
#     #通过夫人查找对应的author信息
#     # wife = Wife.objects.get(name = 'jiayao')
#     # author = wife.author
#     #通过author查找wife的信息
#     author = Author.objects.get(name = 'linlaoshi')
#     wife = author.wife

#     print("夫人:%s,年龄:%d" % (wife.name,wife.age))
#     print("作者:%s,年龄:%d" % (author.name,author.age))
#     #通过王老师查找对应的wife信息
#     return HttpResponse('query ok')

# def otm_views(request):
#     #查询id为1的图书信息，并查找对应的出版社
#     # book = Book.objects.get(id=1)
#     # publisher = book.publisher
#     # print("书名:%s,出版时间：%s" % (book.title,book.publicate_date))
#     # print("出版社:%s,城市:%s" % (publisher.name,publisher.city))

#     #查询id为1的出版社的信息，并查找出对应的所有书籍
#     pub = Publisher.objects.get(id=2)
#     books = pub.book_set.all()
#     print("出版社:%s,城市:%s" % (pub.name,pub.city))
#     for book in books:
#         print("书名:%s,出版时间：%s" % (book.title,book.publicate_date))
#     return HttpResponse("otm ok")

# def mtm_views(request):
#     #通过Book查询Author
#     book = Book.objects.get(id=3)
#     print('书名:' + book.title)
#     authors = book.authors.all()
#     print("编写作者")
#     for au in authors:
#         print("姓名"+au.name)
#     print("*************")
#     #通过Author查询Book
#     author = Author.objects.get(name="linlaoshi")
#     print('作者姓名:'+author.name)
#     books = author.book_set.all()
#     print("编写的书籍:")
#     for book in books:
#         print(book.title)
#     return HttpResponse('mtm ok')

# def objects_views(request):
#     count = Author.objects.isactive_count()
#     return HttpResponse("isActive为True的数量为:%d" % count)


# def request_views(request):
#     print(dir(request))
#     scheme = request.scheme
#     path = request.path
#     body = request.body
#     full_path = request.get_full_path()
#     host = request.get_host()
#     method = request.method
#     get = request.GET
#     post = request.POST
#     cookies = request.COOKIES
#     meta = request.META
#     return render('01-template.html',locals())
    # return HttpResponse(scheme)


#GET,http://192.168.3.5/02-request/?year=2018&month=10&day=11
# def request02_views(request):
#     year = request.GET.get('year','1900')
#     month = request.GET.get('month','01')
#     day = request.GET.get('day','01')
#     print("传递的数据：%s年%s月%s日" %  (year,month,day))
#     return HttpResponse("get ok")

# def post_views(request):
#     if request.method == "GET":
#         return render(request,'01-template.html')
#     else:
#         uname = request.POST.get('uname')
#         upwd = request.POST.get('upwd')
#         return HttpResponse("用户名：%s，用户密码：%s" % (uname,upwd))

#注册用户
# def register_views(request):
#     if request.method == "GET":
#         return render(request,'01-template.html')
#     else:
#         #接收前端传递过来的数据
#         name = request.POST.get('name')
#         age = request.POST.get('age')
#         email = request.POST.get('email')
#         #将数据封装成author的对象
#         au = Author()
#         au.name = name 
#         au.age = age
#         au.email = email
#         #嗲用author的save()将数据保存到数据库
#         au.save()
#     return HttpResponse('register ok')


#form模块
# def form_views(request):
#     if request.method == 'GET':
#         #导入RemarkForm,创建RemarkForm的对象，并发送到06-form.html中
#         form = RemarkForm()
#         return render(request,'01-template.html',locals())
#     else:
#         # subject = request.POST.get('subject')
#         # email = request.POST.get('email')
#         # message = request.POST.get('message')
#         # topic = request.POST.get('topic')
#         # #复选框取值
#         # isSaved = request.POST.get('isSaved','0')
#         # return HttpResponse("subject:%s,email:%s,message:%s,topic:%s,isSaved:%s" % (subject,email,message,topic,isSaved))
        
#         #使用forms对象来接收提交的数据
#         #将request.POST的数据提交给 RemarkForm
#         form = RemarkForm(request.POST)
#         #让RemarkForm的对象通过验证
#         if form.is_valid():
#             #通过验证后再获取各个控件的值
#             cd = form.cleaned_data
#             print(cd)
#             print(cd['email'])
#             # #如果存入数据库，保证model和form模块字段名一致的情况下
#             # au = Author(**form.cleaned_data)
#             # au.save()
#         return HttpResponse("form_post ok")

#form模块的小部件
# def widget1_views(request):
#     if request.method == "GET":
#         form = WidgetForm1()
#         return render(request,'01-template.html',locals())

# def widget2_views(request):
#     if request.method == 'GET':
#         form = WidgetForm2()
#         return render(request,'01-template.html',locals())
        


def ajax_views(request):
    return render(request,'03-static.html')

def server12_views(request):
    # list = ["NARUTO","HINATA","SAKURA","SASUKE"]
    # jsonStr = json.dumps(list)
    # return HttpResponse(jsonStr)
    #查询Author中所有的数据
    authors=Author.objects.all()
    #将authors转换成json格式的字符串
    jsonStr=serializers.serializer('json',authors)
    print(jsonStr)
    return HttpResponse(jsonStr)
