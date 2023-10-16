
from django.contrib import admin
from django.urls import path
from . import userdb

urlpatterns = [
    path('add', userdb.add),
    path('list', userdb.getList),
    path('find', userdb.findBy),
    path('update', userdb.update),
    path('delete', userdb.delete),

    path('postJson', userdb.postJson),
]
