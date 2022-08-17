from django.contrib import admin
from django.urls import path
from django.conf.urls import url #django.conf.urlsからurlモジュールのimport
from . import views #viewsをimportする
from .views import FriendList
from .views import FriendDetail

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'), #/edit/の後ろにIDの数字を入れることができるように指定
    path('delete/<int:num>', views.delete, name='delete'),
    path('list', FriendList.as_view()), #FriendListをビュークラスであるViewインスタンスとして取り出す
    path('detail/<int:pk>', FriendDetail.as_view()),
    path('find', views.find, name='find'),
    path('check', views.check, name='check'),
    path('<int:num>', views.index, name='index'),
    path('message/', views.message, name='message'),
    path('message/<int:page>', views.message, name='message'),
  ]