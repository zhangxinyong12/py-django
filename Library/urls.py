from django.urls import path

from . import views

urlpatterns = [
    path('init', views.init),
    path('add', views.add_book),
    path('list', views.getList),
    path('find', views.findBy),
    path('update', views.update),
    path('delete', views.delete),
]
