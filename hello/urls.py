from django.urls import path #django.urlsからpathモジュールのimport
from . import views #カレントディレクトリのviewsモジュールのimport

urlpatterns = [
    path('<int:id>/<nickname>', views.index, name = 'index'), #アドレスの値をそれぞれid/nickname/という名前に設定し、引数nameに文字列indexを代入
]
