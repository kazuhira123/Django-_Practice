from tkinter.messagebox import NO
from turtle import pd
from django.shortcuts import render
from django.http import HttpResponse #HttpResponseクラスをimportする
from django.views.generic import TemplateView #TemplateViewクラスを呼び出す
from .forms import HelloForm #forms.pyのHelloFormクラスを呼び出す

class HelloView(TemplateView):
  def __init__(self):
    self.params = {
      'title':'Hello', #テンプレート側で変数として定義した名前をキーとする辞書を作成
      'massage':'your data',
      'result':None,
      'form':HelloForm(),
    }

  def get(self, request): #GETメソッドで値が渡された時の処理
    return render(request, 'hello/index.html', self.params) #レンダリング時にself.paramsを戻り値として返すだけの処理

  def post(self, request): #POSTメソッドで値が渡された時の処理
    chk = request.POST['check']
    self.params['result'] = 'you selected: "' + chk + '"'
    self.params['form'] = HelloForm(request.POST)
    return render(request, 'hello/index.html', self.params)