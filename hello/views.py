from tkinter.messagebox import NO
from turtle import pd
from django.shortcuts import render
from django.http import HttpResponse #HttpResponseクラスをimportする
from django.views.generic import TemplateView #TemplateViewクラスを呼び出す
from .forms import HelloForm #forms.pyのHelloFormクラスを呼び出す
from .models import Friend

def index(request):
  data = Friend.objects.all() #Friendクラスのobject属性のallメソッドを利用して、レコードを全て取得する
  params = {
    'title': 'Hello',
    'massage': 'all friend.',
    'data': data,
  }
  return render(request, 'hello/index.html', params)
