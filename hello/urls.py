from django.urls import path #django.urlsからpathモジュールのimport
from . import views #カレントディレクトリのviewsモジュールのimport

urlpatterns = [
    path('', views.index, name='index'), #/hello/のアドレスでindexにアクセスできる形に戻した
]
