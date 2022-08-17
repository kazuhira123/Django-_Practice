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
from .forms import FindForm, FriendForm, MessageForm #FriendFormクラスをimport
from .models import Friend, Message
from django.db.models import QuerySet
from django.views.generic import ListView
from django.views.generic import DetailView
from django.db.models import Q
from django.db.models import Count,Sum,Avg,Min,Max #レコード集計用の関数5つをimportした
from .forms import CheckForm
from django.core.paginator import Paginator

class FriendList(ListView):
  model = Friend #Friendモデルの全てのレコードを呼び出す

class FriendDetail(DetailView):
  model = Friend

def index(request, num=1):
  data = Friend.objects.all() #Firendモデルのレコードを全て取得
  page = Paginator(data, 3) #取得したレコードを3つごとにページネーションする
  params = {
    'title': 'Hello',
    'massage':'',
    'data': page.get_page(num), #引数numの値で指定したページを表示する
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

def check(request):
  params = {
    'title':'Hello',
    'massage':'check validation',
    'form':FriendForm()
  }
  if (request.method == 'POST'):
    obj = Friend()
    form = FriendForm(request.POST, instance=obj)
    params['form'] = form #FriendFormに入力された値をparamsのformキーの要素に代入
    if (form.is_valid()): #変数formの値にエラーがないか確認
      params['massage'] = 'OK!'
    else:
      params['massage'] = 'no good.'
  return render(request, 'hello/check.html', params)

def message(request, page=1):
  if (request.method == 'POST'):
    obj = Message()
    form = MessageForm(request.POST, instance=obj) #MessageFormからPOSTメソッドで送信されたデータをformインスタンスとして生成
    form.save() #生成されたフォームの内容を保存する
  data = Message.objects.all().reverse() #Messageモデルの全レコードを取得し、pub_dataが新しい順に表示
  paginator = Paginator(data, 5) #1ページあたりのレコードを5つにしてページネーションする
  params = {
    'title':'Message',
    'form':MessageForm(),
    'data':paginator.get_page(page),
  }
  return render(request, 'hello/message.html',params)