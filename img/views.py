from django.shortcuts import render,redirect
from img.forms import ProfileForm # 上传图片的图表
from img.models import Profile # 保存上传图片相关信息的模型

def index(request):
    context = {}
    # 获取上传图片的表单，并加到 context 中，使得该表达能在前端展示
    form = ProfileForm
    context['form'] = form
    return render(request, 'index.html', context)

def save_profile(request):

    if request.method == "POST":
        # 接收 post 方法传回后端的数据
        MyProfileForm = ProfileForm(request.POST, request.FILES)
        # 检验表单是否通过校验
        if MyProfileForm.is_valid():
            # 构造一个 Profile 实例
            profile = Profile()
            # 获取name
            profile.name = MyProfileForm.cleaned_data["name"]
            # 获取图片
            profile.picture = MyProfileForm.cleaned_data["picture"]
            # 保存
            profile.save()

        else:
            return redirect(to='index')

        return redirect(to='index')