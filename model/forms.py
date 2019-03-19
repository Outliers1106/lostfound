from django import forms

class login_form(forms.Form):
    #login_form.html
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=20,widget=forms.PasswordInput)
    # 这里的变量名需要同html表单中的保持一致，否则无法读入信息

class objUpload_form(forms.Form):
    #objUpload.html
    sno = forms.CharField(max_length=10, label="上传者学号：")
    name = forms.CharField(max_length=10, label="名称：")
    time = forms.DateField(label="捡到/丢失日期：",input_formats=['%m-%d',])
    # time = forms.DateField(label="捡到/丢失日期：")
    # DateField
    position = forms.CharField(max_length=100, label="捡到/丢失地点：")
    dscp = forms.CharField(max_length=200, label="描述：")
    img  = forms.ImageField(label="图片：",required=False)
    tag = forms.ChoiceField(
        choices=[(1,"丢失物品"),(2,"捡拾物品"),], #单选下拉框
        initial=1,
        label="类型："
    )
