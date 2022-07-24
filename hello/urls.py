from django.urls import path #django.urlsからpathモジュールのimport
from . import views #カレントディレクトリのviewsモジュールのimport

urlpatterns = [
    path('', views.index, name = 'index'), #helloアプリケーションのアドレスを指定するため、アドレスは空白。引数nameに文字列indexを代入
]
