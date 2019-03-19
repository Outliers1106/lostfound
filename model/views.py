from django.shortcuts import render_to_response,HttpResponse
from model import forms,models
import datetime

# 登陆验证
def login_view(request):
    if request.method == "POST":
        form = forms.logincheck(request.POST)
        if form.is_valid():
            # 表单合法，则会把数据放在表单的cleaned_data中
            cd = form.cleaned_data
            username=cd['username']
            password=cd['password']
            try:
                user_db = models.User.objects.get(sno=username)#连接数据库检查密码正确性
                if user_db.pwd == password:
                    # 密码正确
                    return HttpResponse("Sign in successfully")
                else:
                    # 密码错误
                    return HttpResponse("password error or user dont exist")
            except models.User.DoesNotExist:
                # 用户不存在
                return HttpResponse("password error or user dont exist")
        else:
            # 表单不合法
            return HttpResponse("form invalid")
    else:
        form=forms.login_form()
        return render_to_response('login_form.html',{'form':form})

def objUpload_view(request):
    if request.method=="POST":
        # 获取用户输入后的POST表单
        form=forms.objUpload_form(request.POST,request.FILES)# request.FILES是获取imagefield的要求，否则获取不到图片

        # 检查表单的合法性
        if form.is_valid():
            obj=models.Object()             # 创建上传的物品的对象
            user_obj=models.UserObject()    # 创建用户-物品对象
            try:
                # ！其实这里有问题，假如用户随意输入的学号是存在于数据库中的，那提交的用户就会变成那个学号，而不一定是登陆的用户本身
                # ！所以后期要通过获取登陆用户的状态，自动获取学号信息
                user_db = models.User.objects.get(sno=form.cleaned_data['sno'])# 从数据库获取用户信息，若输入学号有误（数据库中没有这个学号）则被except处理
                user_obj.user=user_db

                # 输入物品信息
                nowtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
                obj.id = nowtime# 为物品生成一个当前时间的id，作为主键
                obj.name = form.cleaned_data['name']
                input_date = form.cleaned_data['time']
                obj.time = datetime.date(datetime.datetime.now().year,
                                         input_date.month,
                                         input_date.day)
                # 因为表单输入没有设置year（默认year=1900）需要重新设置
                # datetime 对象是不可修改的（not writable），实现赋值需要新的date对象
                obj.position = form.cleaned_data['position']
                obj.dscp = form.cleaned_data['dscp']
                obj.tag = form.cleaned_data['tag']
                obj.state = 0  # state=0 未审核状态
                if form.cleaned_data['img']:
                    # 如果有图片上传则执行以下部分
                    obj.img = form.cleaned_data['img']
                    obj.img.name = nowtime+".jpg"# 将图片名称修改为物品id
                obj.save()# 上传物品到数据库

                obj_db = models.Object.objects.get(id=nowtime)# 检查是否物品信息是否上传到数据库（通过搜索数据库中，有无id=nowtime的物品，若没有会被except处理
                user_obj.object=obj_db
                user_obj.save()# 上传 用户-物品记录
                return HttpResponse("Upload successfully.")
            except models.User.DoesNotExist:
                # 用户不存在
                return HttpResponse("User dont exist.")
            except models.Object.DoesNotExist:
                # 物品信息没有存入数据库
                return HttpResponse("Upload error.")
        else:
            #表单不合法
            return HttpResponse("Input invalid.")
    else:
        # 处理非POST的情况,返回表单页面，用户输入数据
        form = forms.objUpload_form
        context={}
        context['form']=form
        return render_to_response('objUpload.html',context)