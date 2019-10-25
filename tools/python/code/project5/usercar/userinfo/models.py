from django.db import models
#修改django自带的数据库
from django.contrib.auth.models import AbstractUser
# Create your models here.
SEX_CHOICES = (
    (0,'男'),
    (1,'女'),
)

ROLE_CHOICE = (
    (0,'buy'),
    (1,'sale'),
    (2,'back'),
)

BANK_CHOICES = (
    (0,'中国工商银行'),
    (1,'中国建设银行'),
    (2,'中国农业银行'),
    (3,'中国工商银行'),
    (4,'中国招商银行'),
    (5,'中国金和银行'),
)

# class UserInfo(models.Model):
class UserInfo(AbstractUser):
    #继承，添加新的字段
    # username = models.CharField(verbose_name='用户名',max_length=200,null=False)
    # password = models.CharField(verbose_name='密码', max_length=200, null=False)
    realname = models.CharField(verbose_name='真实姓名', max_length=200, null=False)
    iden = models.CharField(verbose_name='身份证号', max_length=200, null=False)
    ads = models.CharField(verbose_name='地址', max_length=200, null=False)
    uphone = models.CharField(verbose_name='手机号码', max_length=200, null=False)
    sex = models.CharField(verbose_name='性别', max_length=200, choices=SEX_CHOICES,default=0)
    role = models.CharField(verbose_name='角色', max_length=200, choices=ROLE_CHOICE,default=0)
    isActive = models.CharField(verbose_name='是否激活', max_length=200, null=False)
    isBan = models.CharField(verbose_name='是否禁用', max_length=200, default=0)

    def __str__(self):
        return self.username

class Bank(models.Model):
    cardNo = models.CharField('卡号',max_length=30,null=False)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    cpwd = models.CharField('交易密码',max_length=200,null=False)
    bank = models.IntegerField(verbose_name='开户银行',choices=BANK_CHOICES,default=0)
    isDelete = models.BooleanField(verbose_name='是否删除',default=False)

    def __str__(self):
        #显示user字段的外键表中的字段
        return self.user.username








