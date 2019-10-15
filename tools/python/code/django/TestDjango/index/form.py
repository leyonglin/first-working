from django import forms

#form模块初级使用
# #声明ChoiceField要用到的数据
# TOPIC_CHOICE = (
#     ('1','好评'),
#     ('2','中评'),
#     ('3','差评'),
#     )

# #表示评论内容的表单控件的class
# class RemarkForm(forms.Form):
#     #评论标题-文本框
#     #label：控件前的文本标签
#     subject = forms.CharField(label="标题")
#     #控件2-电子邮箱-邮箱框
#     email = forms.EmailField(label="邮箱")
#     #评论内容,widget=forms.Textarea将当前的单行文本框变为多行文本域
#     message = forms.CharField(label="内容",widget=forms.Textarea)
#     #评论级别，choices:表示当前下拉列表框中的数据，取值为元组或列表
#     topic = forms.ChoiceField(label='级别',choices=TOPIC_CHOICE)
#     #控件5-是否保存-复选框
#     isSaved = forms.BooleanField(label='是否保存')

#form模块和model模块一起使用
from django.forms import ModelForm
from index.models import Author
class RemarkForm(forms.ModelForm):
    class Meta:
        #指定关联的model
        model = Author
        #指定生成控件的字段,与label对应
        # fields = ['name','age']
        fields = "__all__"
        #控件与labels对应
        labels = {
            'name':'名称',
            'age':'年龄',
            'email':'邮件',
            'isActive':'是否激活',
        }

#form模块的小部件
class WidgetForm1(forms.Form):  
    #小部件高级版
    uname = forms.CharField(label="用户名称",
        widget=forms.TextInput(
            attrs = {
            #
            'class':'form-control',
            'placeholder':'请输入用户名称'
                }
            )
        )
    #通过小部件基本版，将upwd指定为密码框
    # upwd = forms.CharField(label="用户密码",widget=forms.PasswordInput)
    #小部件高级版
    upwd = forms.CharField(
        label="用户密码",
        widget=forms.PasswordInput(
            attrs={
            'class':'form-control',
            'placeholder':'请输入用户密码'
            }
        )
    )

#form小部件，继承自forms.ModelForm类
class WidgetForm2(forms.ModelForm):
    class Meta:
        #指定关联的实体
        model = Author
        #指定要显示的字段
        fields = ['name','age','email']
        #指定字段对应的标签
        labels = {
            'name':'用户姓名',
            'age':'用户年龄',
            'email':'用户邮箱',
        }
        #指定字段对应的小部件
        widgets = {
            'age':forms.NumberInput(
                attrs={
                    'placeholder':'请输入年龄',
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'placeholder':'请输入电子邮箱',
                    'class':'form-control',
                }
            )
        }