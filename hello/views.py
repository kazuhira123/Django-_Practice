from ast import If
import imp
import re
from tkinter.messagebox import NO
from turtle import pd
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

class FriendList(ListView):
  model = Friend #Friendモデルの全てのレコードを呼び出す

class FriendDetail(DetailView):
  model = Friend

def index(request):
  data = Friend.objects.all().order_by('age') #objects.all()で取得したレコードをモデルの項目ageを基準に並べ替えるnarabekaeru
  params = {
    'title': 'Hello',
    'massage':'',
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
    msg = 'search result:'
    form = FindForm(request.POST)
    find = request.POST['find'] #POSTメソッドでの通信時に検索した値を変数findに代入
    list = find.split() #splitメソッドでテキストを分割したリストを返す、今回はsplitに引数を指定していないので、半角スペースや改行で分割する
    data = Friend.objects.filter(name__in=list) #検索した文字列をまとめてリスト化し、そのリストに合致する結果を返す
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