
#加密模块
from django.contrib.auth.hashers import make_password
#错误处理模块
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect
from django.http import HttpResponse
from userinfo.models import UserInfo
#日志模块
import logging
#
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def register(request):
    #判断请求方式，获取数据并判断是否已存在,返回不同数据
    if request.method == "POST":
        new_user = UserInfo()
        new_user.username = request.POST.get("username")
        try:
            olduser = UserInfo.objects.filter(username=new_user.username)
            if len(olduser) > 0:
                return render('register.html',{'message':'用户名已存在'})
                #如果是前后端分离
                #return HttpResponse(json.dumps({'result':False,'data':'','error':'用户名已存在'}))
        except ObjectDoesNotExist as e:
            logging.warning(e)
        if request.POST.get('pwd') != request.POST.get('cpwd'):
            return render(request,'register.html',{'message':'两次密码不一致'})
        #加密
        new_user.password = make_password(request.POST.get('pwd'),None,'pbkdf2_sha1')
        #检查：check_password(),返回True或者False
        new_user.save()
        return render(request,'log.html')

def login(request):
    #判断请求方式，获取前端数据并与数据库比对,返回不同数据
    if request.method == "POST":
        # luser = UserInfo()
        # luser.username = request.POST.get("username")
        # luser.password = request.POST.get('pwd')
        uname = request.POST.get("username")
        pwd = request.POST.get('pwd')
        #判断用户的合法性，用户名密码为空,存在获取用户对象
        user = authenticate(username=uname,password=pwd)
        if user is not None and user.is_active:
            #用户登录
            login(request,user)
            #获取来源url
            url = request.COOKIES.get('source_url','')
            return  HttpResponse(request,'index.html')

def logout(request):
    logout(request)
    return render(request,'index.html')

def register(request):
    if request.user.is_authenticated():
