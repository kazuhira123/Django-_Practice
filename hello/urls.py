from django.contrib import admin
from django.urls import path
from django.conf.urls import url #django.conf.urlsからurlモジュールのimport
from . import views #viewsをimportする

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit') #/edit/の後ろにIDの数字を入れることができるように指定
  ]