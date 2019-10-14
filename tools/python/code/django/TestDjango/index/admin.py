from django.contrib import admin
from .models import *

#定义高级管理类并注册
class AuthorAdmin(admin.ModelAdmin):
    #定义在列表页上显示的字段
    list_display = ('name','age','email')
    #定义允许链接到详情页的字段们
    list_display_links = ('email',)
    #定义在列表页中就允许修改的字段们
    list_editable = ('age',)
    #定义搜索字段
    search_fields = ('name','email')
    #定义右侧过滤器
    list_filter = ('name','age')
    #指定在详情页上显示的字段以及顺序
    # fields = ('name','email')
    #指定字段在详情页上的分组
    # fieldsets = (
    #     #分组1
    #     ('基本信息',{
    #         'fields':('name','age'),
    #         #折叠
    #         'classes':('collapse',),
    #         }),
    #     #分组2
    #     ('详细信息',{
    #         'fields':('email','isActive'),
    #         'classes':('collapse'),
    #         }),
    #     )

class BookAdmin(admin.ModelAdmin):
    #指定在列表中显示的字段们
    list_display = ('title','publicate_date')
    #增加右侧时间选择器
    date_hierarchy = 'publicate_date'



# Register your models here.
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher)
admin.site.register(Wife)