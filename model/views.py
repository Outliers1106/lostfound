from django.shortcuts import render_to_response
from model import forms,models
# Create your views here.

#表单
def login_form(request):
    return render_to_response('login_form.html')

#
def login(request):
    if request.method == "POST":
        form = forms.logincheck(request.POST)
        if form.is_valid():#账号密码输入合法，连接数据库检查正确性
            cd = form.cleaned_data
            username=cd['username']
            password=cd['password']
            user_db=models.User.objects.get(sno=username)
            if user_db.psw==password:#密码正确
                return render_to_response("signin.html")
            else:#密码错误
                return render_to_response("login_error.html")
        else:
            errors=form.errors
            return render_to_response("login_form.html")
    else:
        form = forms.logincheck(request.method)
        errors = form.errors
        return render_to_response("login_form.html")