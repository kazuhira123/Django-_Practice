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
    'form':HelloForm(),
    'data': [],
  }
  if (request.method == 'POST'):
    num=request.POST['id'] #変数numにPOSTメソッドで送信された時のidの値を代入する
    item = Friend.objects.get(id=num) #IDの値がnumと一致するレコードの値を取り出す
    params['data'] = [item] #テンプレートで繰り返し処理を実施するitemの値をparamsのdata要素に代入する
    params['form'] = HelloForm(request.POST)
  else:
    params['data'] = Friend.objects.all() #HTTPメソッドがPOSTでない時、Friendモデル内の全ての値をparamsのdata要素に代入

  return render(request, 'hello/index.html', params)
