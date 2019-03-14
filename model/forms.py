from django import forms

#这里是html的表单对象

class logincheck(forms.Form):
    #login_form.html
    username = forms.CharField()
    password = forms.CharField()
    # 这里的变量名需要同html表单中的保持一致，否则无法读入信息