**lostfound**
1. **setting.py**是整个django项目的设置文件，有各种设置的开关以及路径。
2. **urls.py**中保存有url与视图函数（view）的映射关系
   
**APP**
项目目前有两个APP：**model**和**img**
1. **img**是我用来测试图片上传功能的APP
2. **model**是最主要的APP
    - **models.py** 数据库对象的模型
    - **forms.py**  django表单模型，格式上同**models.py**很像，注意区分
    - **views.py** django的视图函数，通过**urls.py**映射对应的视图完成指定的功能，
    view同前端网页和后端数据库连接
    
**templates**
当前测试功能的简单网页（HTML）
- index.html (**img**)
- login_form.html (**model**) 用户登陆界面
- objUpload.html (**model**) 失物信息上传页面

**upload**
用来保存用户上传的图片

**mydb.db**
SQLite数据库

    
