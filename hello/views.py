from django.shortcuts import render
from django.http import HttpResponse #HttpResponseクラスをimportする

def index(request): #HttpResponseを実行するindex関数の定義
  return HttpResponse('Hello Django!!') #HttpResposeインスタンスを作成し、戻り値をHello Djangoとする
