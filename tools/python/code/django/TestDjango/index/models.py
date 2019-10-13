from django.db import models

# Create your models here.
#在数据库先创建好库：create database webdb default charset utf8 collate utf8_general_ci;
#创建一个实体类(表) - Publisher(出版社)
#1.name:出版社名称(varcher(30))
#2.address:出版社地址(varchar(200))
#3.city:出版社所在城市(varchar(50))
#4.country:出版社城市(varchar(50))
#5.website:出版社的网址(varchar(20))
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __repr__(self):
        return "<Author:%r>" % self.name

#追加两个表,如果需要修改/删除表，在实体类这里修改/删除
class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=50,null=True)
#添加一个字段isActive表示用户激活状态，数据类型为BooleanField(),新增字段要么允许为空，要么设置默认值，不然会冲突
    isActive = models.BooleanField(default=True)

class Book(models.Model):
    title = models.CharField(max_length=50)
    publicate_date = models.DateField()
