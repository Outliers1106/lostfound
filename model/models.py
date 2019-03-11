# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.
class User(models.Model):
    #用户（学号（主）、密码、姓名、电话、邮箱、标识）

    sno = models.IntegerField(primary_key=True)
    psw = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    #标识：ifadmin=1 为管理员；=0为普通用户
    ifadmin = models.BinaryField()

class Object(models.Model):
    #物品（物品编号（主）、名称、时间、地点、
    # 细节描述、图片、领取状态、标识）

    #物品编号：id django自动生成
    name = models.CharField(max_length=10)
    time = models.DateTimeField()
    position = models.CharField(max_length=100)
    dscp = models.CharField(max_length=200)
    #图片：imglink 存放图片的路径
    imglink = models.CharField(max_length=100)
    #领取状态：taken=1已领取，=0未领取
    taken = models.BinaryField()
    #（lost or found）标识：lof=0 lost 失物；lof=1 found 拾物
    lof = models.BinaryField()

class UserObject(models.Model):
    #用户-物品（物品编号、学号、信息提交时间）

    #id（主） django自动生成
    object = models.ForeignKey(Object,
                               on_delete=models.CASCADE,)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,)
    time = models.DateTimeField()

class AllSort(models.Model):
    #类别（类别编号、类名）

    #类别编号 id（主） django自动生成
    name = models.CharField(max_length=10)

class SortObject(models.Model):
    #物品分类（类别编号、物品编号）

    # id（主） django自动生成
    sort = models.ForeignKey(AllSort,
                             on_delete=models.CASCADE,)
    object = models.ForeignKey(Object,
                               on_delete=models.CASCADE,)

class TakenRecord(models.Model):
    #认领记录（信息发布者学号、提供失物 / 认领者、
    # 物品、认领时间、标识）

    # id（主） django自动生成
    #user1 信息发布者
    user1 = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name="User1",)
    #user2 提供失物 / 认领者--由lof字段确定
    user2 = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name="User2")
    object = models.ForeignKey(Object,
                               on_delete=models.CASCADE,)
    time = models.DateTimeField()
    #（user2）标识 lof=0 lost 丢失的人（认领者）；lof=1 found 捡到的人
    lof = models.BinaryField()