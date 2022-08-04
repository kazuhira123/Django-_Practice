from tkinter.messagebox import NO
from turtle import pd
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse #HttpResponseクラスをimportする
from django.views.generic import TemplateView #TemplateViewクラスを呼び出す
from .forms import HelloForm #forms.pyのHelloFormクラスを呼び出す
from .models import Friend
from django.db.models import QuerySet

def __new_str__(self): #表示するレコードの値を更新する為の関数__new_str__を定義
  result = ''
  for item in self:
    result += '<tr>' #ヘッダー用のタグを追加
    for k in item:
      result += '<td>' + str(k) + '=' + str(item[k]) + '</td>'
    result += '</tr>'
  return result

QuerySet.__str__ = __new_str__ #モデル上で定義した__str__の値を__new_str__に更新する

def index(request):
  data = Friend.objects.all().values('id', 'name', 'age') #Friendクラスのobject属性のallメソッドを利用してレコードを全て取得し、valuesメソッドで取得したレコード内の任意のキーの値を返す
  params = {
    'title': 'Hello',
    'data': data, #Friendオブジェクトから取得した値がparamsのdata要素に入る
  }
  return render(request, 'hello/index.html', params)
