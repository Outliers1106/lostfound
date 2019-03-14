from django.shortcuts import render_to_response,HttpResponse
from model import forms,models

#login_form表单POST处理函数
def login_check(request):
    if request.method == "POST":
        form = forms.logincheck(request.POST)
        if form.is_valid():
            #账号密码输入合法，连接数据库检查正确性
            cd = form.cleaned_data
            username=cd['username']
            password=cd['password']
            try:
                user_db = models.User.objects.get(sno=username)
                if user_db.pwd == password:
                    # 密码正确
                    return render_to_response("signin.html")
                else:
                    # 密码错误
                    return render_to_response("login_error.html")
            except models.User.DoesNotExist:
                return render_to_response("login_error.html")
        else:
            #输入不合法
            return HttpResponse("form invalid")
    else:
        return render_to_response('login_form.html')