from django.conf.urls import url #django.conf.urlsからurlモジュールのimport
from .views import HelloView #HelloViewクラスをimportする

urlpatterns = [
    url(r'', HelloView.as_view(), name='index'), #r''で全ての文字列にマッチするワイルドカードとしてアドレスを扱う。
  ]
