# py学习笔记
## 指定安装django版本
```
pip install "django>=3.0,<4.0"
```
## 查询版本 
```
python manage.py --version
```
## 创建项目
```
django-admin startproject mysite
```
## 启动项目
```
python manage.py runserver
```
## 创建应用
```
python manage.py startapp polls
```
## 创建数据库
```
python manage.py migrate   # 创建表结构
python manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
python manage.py migrate TestModel   # 创建表结构
```

## post 请求返回403
### 解决：

导入模块：
```
from django.views.decorators.csrf import csrf_exempt
```
在函数前面添加修饰器：
```
@csrf_exempt
```
### 原因：

当采用客户端象 django 的服务器提交 post 请求时，会得到403，权限异常。

因为 django 针对提交的请求，有校验。所以会如此。

客户端提交的 post 如果不加这段，会出现 403 error
```
@csrf_exempt
def runoob(request):
    name = request.POST.get("name")
```