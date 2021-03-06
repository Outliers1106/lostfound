"""lostfound URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from model.views import *
from img.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login$',login_view),# 登陆界面

    url(r'^save_profile/', save_profile, name='save_profile'),
    url(r'^index/', index, name='index'), # 图片上传

    url(r'^upload$',objUpload_view) #物品信息上传
]
