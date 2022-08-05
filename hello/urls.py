from django.conf.urls import url #django.conf.urlsからurlモジュールのimport
from . import views #viewsをimportする

urlpatterns = [
    url('', views.index, name='index'),
    url('create', views.create, name='create'),
  ]
