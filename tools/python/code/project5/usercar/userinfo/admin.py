from django.contrib import admin
from .models import *
# Register your models here.
#将数据库在这里注册，这样就能在django的admin页面看到
admin.site.register(UserInfo)