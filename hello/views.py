from django.shortcuts import render
from django.http import HttpResponse #HttpResponseクラスをimportする

def index(request): #HttpRequestクラスの引数requestを返すindex関数の定義
  msg = request.GET['msg'] #HttpRequestクラスのGET属性(クエリパラメーターの値等の入っている辞書)を使って&msg=◯◯として送られた値を取り出している
  return HttpResponse('you typed: "' + msg + '" .') #HttpResposeインスタンスを作成し、戻り値をHello Djangoとする