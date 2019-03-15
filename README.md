# lostfound

---
*2019年3月15日11点02分*
-数据库由mysql改成了sqlite3：mydb.db
---
*2019年3月14日21点07分*
-创建了一个测试图片上传的app：img（参考网站：https://www.jianshu.com/p/3c79b19849f5）
-修改了数据库模型，添加了所有数据模型的主键设置，避免数据重复
---
*2019年3月13日22点35分*
-表单的POST方法引起的csrf错误，通过注释setting中的
`django.middleware.csrf.CsrfViewMiddleware`
解决（并没有，只是关闭了django对此的检查，需要后期改进；
-对数据库模型进行了一定的修改；
**主要**
-写了一个简单的用户登陆界面；
-完成了简单的用户登陆与数据库的交互操作；