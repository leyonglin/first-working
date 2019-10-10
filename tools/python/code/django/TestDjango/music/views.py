from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_views(request):
    return HttpResponse("这是music的首页")

def test01_views(request):
    return HttpResponse('这是没有参数的访问路径')

def test02_views(request,num):
    return HttpResponse('传递进来的参数:'+num)