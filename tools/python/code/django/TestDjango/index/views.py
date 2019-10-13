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

def static_views(request):
    return render(request,'03-static.html')

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

def homework_views(request):
    #查询年龄大于平均年龄的数据
    avgAge = Author.objects.aggregate(avgAge=Avg('age'))['avgAge']
    print(avgAge)
    return HttpResponse('query ok') 