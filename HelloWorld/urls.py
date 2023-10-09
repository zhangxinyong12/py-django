"""
URL configuration for HelloWorld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views, testdb

urlpatterns = [
    path('runoob/', views.runoob),
    path('testdb/', testdb.testdb),
    path('list/', testdb.getAll),
    path('add/', testdb.add),
    path('find/', testdb.find),
    path('update/', testdb.update),  # 更新
    path('delete/', testdb.delete),  # 删除
]
