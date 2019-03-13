from django import forms

class logincheck(forms.Form):
    #这里的变量名需要同html表单中的保持一致
    username = forms.CharField()
    password = forms.CharField()