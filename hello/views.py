import imp
import re
from tkinter.messagebox import NO
from turtle import pd
from unicodedata import name
from unittest import result
from django.shortcuts import redirect, render #redirectとrender関数をimport
from django.http import HttpResponse #HttpResponseクラスをimportする
from django.views.generic import TemplateView #TemplateViewクラスを呼び出す
from .forms import FriendForm #FriendFormクラスをimport
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