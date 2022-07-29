from django.urls import path #django.urlsからpathモジュールのimport
from . import views #カレントディレクトリのviewsモジュールのimport

urlpatterns = [
    path('', views.index, name='index'), #/hello/のアドレスでindexにアクセスできる形に戻した
    path('next', views.next, name='next'), #新規ページ用のビュー関数のアドレスhello/nextの設定
    path('form', views.form, name='form'), #フォーム用のビュー関数のアドレスにhello/formを設定
]
