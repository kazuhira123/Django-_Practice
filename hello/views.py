from ast import If
import imp
from itertools import count
import re
from tkinter.messagebox import NO
from turtle import pd, st
from unicodedata import name
from unittest import result
from django.shortcuts import redirect, render #redirectとrender関数をimport
from django.http import HttpResponse #HttpResponseクラスをimportする
from django.views.generic import TemplateView #TemplateViewクラスを呼び出す
from .forms import FindForm, FriendForm #FriendFormクラスをimport
from .models import Friend
from django.db.models import QuerySet
from django.views.generic import ListView
from django.views.generic import DetailView
from django.db.models import Q
from django.db.models import Count,Sum,Avg,Min,Max #レコード集計用の関数5つをimportした

class FriendList(ListView):
  model = Friend #Friendモデルの全てのレコードを呼び出す

class FriendDetail(DetailView):
  model = Friend

def index(request):
  data = Friend.objects.all()
  re1 = Friend.objects.aggregate(Count('age')) #レコードを集計するaggregateメソッドを使う
  re2 = Friend.objects.aggregate(Sum('age'))
  re3 = Friend.objects.aggregate(Avg('age'))
  re4 = Friend.objects.aggregate(Min('age'))
  re5 = Friend.objects.aggregate(Max('age'))
  msg = 'Count:' + str(re1['age__count']) \
    + '<br>Sum:' + str(re2['age__sum']) \
    + '<br>Average:' + str(re3['age__avg']) \
    + '<br>Min:' + str(re4['age__min']) \
    + '<br>Max:' + str(re5['age__max']) #aggregateメソッドで辞書として取り出した値を文字列として変数msgに代入
  params = {
    'title': 'Hello',
    'massage':msg,
    'data': data, #Friendオブジェクトから取得した値がparamsのdata要素に入る
  }
  return render(request, 'hello/index.html', params)

#create model
def create(request):
  if (request.method == 'POST'):
    obj = Friend() #Friendクラスのインスタンスを生成し変数objに代入
    friend = FriendForm(request.POST, instance=obj) #FriendFormインスタンスを生成し、引数にPOST送信された情報とobjインスタンスを指定
    friend.save() #firendインスタンスの保存、変数friendはFriendFormのインスタンス変数であるため、FriendFormに送られた値が保存される
    return redirect(to='/hello') #上記インスタンスを保存した後、/helloにリダイレクト(自動的に他のWebページに転送されること)される
  params = {
    'title':'Hello',
    'form':FriendForm(),
  }
  return render(request, 'hello/create.html', params) #create.htmlを表示する際にcreate関数を返す

def edit(request, num): #URL側で指定したedit/<int:num>によってアドレスのnumの値が引数numに代入される
  obj = Friend.objects.get(id=num) #関数の引数に指定した値とテーブルから取得したレコードのidが一致するものだけを取得
  if (request.method == 'POST'):
    friend = FriendForm(request.POST, instance=obj) #FriendFormのインスタンスの引数にobjを指定することで、取得したFriendインスタンスの内容が更新され、レコードが保存される
    friend.save()
    return redirect(to='/hello')
  params = {
    'title':'Hello',
    'id':num,
    'form':FriendForm(instance=obj),
  }
  return render(request, 'hello/edit.html', params)

def delete(request, num):
  friend = Friend.objects.get(id=num)
  if (request.method == 'POST'):
    friend.delete() #Friendインスタンスで取得したレコードを削除する
    return redirect(to='/hello')
  params = {
    'title':'Hello',
    'id':num,
    'obj':friend,
  }
  return render(request, 'hello/delete.html', params)

def find(request):
  if (request.method == 'POST'):
    msg = request.POST['find']
    form = FindForm(request.POST)
    sql = 'select * from hello_friend' #rawメソッドで実行するSQL文、,中身はfriendテーブルの全てのレコードを取得する文
    if (msg != ''):
      sql += ' where ' + msg #フォームにテキストが入力されていた場合、WEHRE文の条件に入力したテキストが追加される(whereの前後のスペースキー忘れずに！)
    data = Friend.objects.raw(sql) #SQL文を実行するrawメソッドにSELECT文を記載した変数sqlを代入
    msg = sql
  else:
    msg = 'search words…'
    form = FindForm()
    data = Friend.objects.all()
  params = {
    'title':'Hello',
    'massage':msg,
    'form':form,
    'data':data,
  }
  return render(request, 'hello/find.html', params)