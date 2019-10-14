from django.db import models

#自定义AuthorManager类型，继承自models.Manger
#并定义自定义方法
class AuthorManager(models.Manager):
    def isactive_count(self):
        #objects(类) 是 models.Manger的实例，self也是，所以self 等于 objects
        return self.filter(isActive=True).count()

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

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Author:%r>" % self.name



#追加两个表,如果需要修改/删除表，在实体类这里修改/删除
class Author(models.Model):
    #自定义查询对象,通过AuthorManager来覆盖掉默认的objects
    objects = AuthorManager()
    name = models.CharField(max_length=30,verbose_name="姓名")
    age = models.IntegerField()
    email = models.EmailField(max_length=50,null=True)
#添加一个字段isActive表示用户激活状态，数据类型为BooleanField(),新增字段要么允许为空，要么设置默认值，不然会冲突
    isActive = models.BooleanField(default=True)

    #定义admin后台的数据索引显示内容
    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Author:%r>" % self.name

    class Meta:
        #指定映射回数据库表的名称,db_table属性修改完成，需要实时同步回数据库
        db_table='author'
        #定义在后台的显示名称(单数)
        verbose_name = '作者'
        #定义在后台的显示名称(复数)
        verbose_name_plural = verbose_name
        #定义数据在后台的排序方式
        ordering = ['-age','-id']



class Book(models.Model):
    title = models.CharField(max_length=50)
    publicate_date = models.DateField()
    #一个出版社可以出版多本书，在book增加一个字段，null=True
    publisher = models.ForeignKey(Publisher,null=True,on_delete=True)
    #多对多，book和Authors，会生成第三张表，不用null=True
    authors = models.ManyToManyField(Author)





#创建Wife实体类
class Wife(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    #一对一映射，增加对Author的引用
    author = models.OneToOneField(Author,null=True,on_delete=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'wife'
        verbose_name = '娘子'
        verbose_name_plural =verbose_name