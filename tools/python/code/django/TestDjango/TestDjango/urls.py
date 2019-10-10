"""TestDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
# from django.contrib import admin
# #从视图文件导入执行函数
# from .views import *

# urlpatterns = [
#     #注意加上/，和最后添加逗号
#     url(r'^admin/', admin.site.urls),
#     url(r'^01-show/$', show_views),
#     #url传参，一个子组表示一个参数
#     url(r'^02-show/(\d{4})/$',show02_views),
#     url(r'^03-show/(\d{4})/(\d{2})/(\d{2})/$',show03_views)
#     #字典传参
#     url(r'^04-show/$',show04_views,{'name':'jiayao','age':18}),
# ]

#主路由文件，配置分布式路由系统
from django.conf.urls import url,include

urlpatterns = [
    url(r'^music/',include('music.urls')),
    url(r'^news/',include('news.urls')),
    url(r'^sport/',include('sport.urls')),
    #默认匹配
    url(r'',include('index.urls')),
]