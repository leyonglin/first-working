from django.db import models

# Create your models here.
from sale.models import CarInfo
from userinfo.models import UserInfo

ORDER_STATUS = (
    (0,'待支付'),
    (1,'已支付'),
    (2,'取消订单'),
    (3,'订单失败'),
    (4,'交易成功'),
    (5,'交易完成'),
)

class CartInfo(models.Model):
    price = models.DecimalField('价格',max_digits=8,decimal_places=2)
    buser = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    car = models.ForeignKey(CarInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.buser.username

class OrderInfo(models.Model):
    # 报错Add or change a related_name argument to the definition for 'OrderInfo.suser' or 'OrderInfo.buser'
    #添加或者修改一个related_name参数去定义'OrderInfo.suser' or 'OrderInfo.buser'
    buser = models.ForeignKey(UserInfo,on_delete=models.CASCADE,related_name='buser')
    suser = models.ForeignKey(UserInfo,on_delete=models.CASCADE,related_name='suser')
    car = models.TextField('汽车')
    price = models.DecimalField('价格', max_digits=8, decimal_places=2)
    oderNo = models.CharField('订单号',max_length=50)
    status = models.IntegerField('订单状态',choices=ORDER_STATUS,default=0)
    datetime = models.DateTimeField('时间',auto_now=True)
    isDelete = models.BooleanField('是否删除',default=False)

    def __str__(self):
        return self.oderNo