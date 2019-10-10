
from django.conf.urls import url
from .views import *

urlpatterns = [
    #注意加上/，和最后添加逗号
    url(r'^index/$',index_views),
    #如果没加$，则http://192.168.3.5/music/test/abc.com都能匹配到,多个命中匹配的情况下，谁在前执行谁
    url(r'^test/$',test01_views),
    url(r'^test/(\d{4})/$',test02_views),
]