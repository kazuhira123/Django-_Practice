import re
from tkinter.messagebox import NO
from turtle import pd
from unicodedata import name
from unittest import result
from django.shortcuts import redirect, render #redirectとrender関数をimport
from django.http import HttpResponse #HttpResponseクラスをimportする
from django.views.generic import TemplateView #TemplateViewクラスを呼び出す
from .forms import HelloForm #forms.pyのHelloFormクラスを呼び出す
from .models import Friend
from django.db.models import QuerySet

def index(request):
  data = Friend.objects.all()
  params = {
    'title': 'Hello',
    'data': data, #Friendオブジェクトから取得した値がparamsのdata要素に入る
  }
  return render(request, 'hello/index.html', params)

#create model
def create(request):
  params = {
    'title': 'Hello',
    'data': data, #Friendオブジェクトから取得した値がparamsのdata要素に入る
  }
  if (request.method == 'POST'):
    name = request.POTS['name'] #ここから変数にPOSTメソッドで送信されたテーブルの各項目の値を代入する処理
    mail = request.POST['mail']
    gender = 'gender' in request.POST #BooleanFieldで定義されているgender要素だけ処理が違う(POSTメソッドで送信された値からgenderキーの要素を取り出している)
    age = int(request.POST['age']) #ageキーの要素を整数として取り出す
    birth = request.POST['birthday']
    friend = Friend(name=name, mail=mail, gender=gender, age=age, birthday=birth) #上記で定義した変数の値を元にFriendインスタンスを生成
    friend.save() #firendインスタンスの保存
    return redirect(to='/hello') #上記インスタンスを保存した後、/helloにリダイレクト(自動的に他のWebページに転送されること)される
  return render(request, 'hello/creste.html', params) #create.htmlを表示する際にcreate関数を返す