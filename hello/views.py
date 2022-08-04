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
    result += '<tr>' #変数resultにテーブルの横軸の要素を追加(テーブルの各項目が入るイメージ)
    for k in item:
      result += '<td>' + str(k) + ' = ' + str(item[k]) + '</td>' #変数resultに縦軸の要素として、「辞書のキー=キーに紐づく要素の中身」の形で値を代入、取り出す値はindexで指定したレコードとなる
    result += '</tr>'
  return result

QuerySet.__str__ = __new_str__ #QuerySetの__str__を__new_str__に更新する

def index(request):
  data = Friend.objects.all().values('id', 'name', 'age') #Friendクラスのobject属性のallメソッドを利用してレコードを全て取得し、valuesメソッドで取得したレコード内の任意のキーの値を返す。ここでのallやvaluesメソッドの動きは↑で更新したQuerySetの通りに表示される
  params = {
    'title': 'Hello',
    'data': data, #Friendオブジェクトから取得した値がparamsのdata要素に入る
  }
  return render(request, 'hello/index.html', params)
