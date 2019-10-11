from django.http import HttpResponse
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