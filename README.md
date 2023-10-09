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

