from django.shortcuts import render
from django.http import HttpResponse #HttpResponseクラスをimportする

def index(request):
  params = {
    'title': 'Hello/Index', #テンプレート側で変数として定義した名前をキーとする辞書を作成
    'msg': 'これは、サンプルで作ったページです'
    'goto': 'next', #リンクを作成したテンプレート変数gotoをキーとする辞書作成
  }
  return render(request, 'hello/index.html', params) #テンプレートをレンダリングするrender関数の第2引数にtemplatesフォルダ内のパス、第3引数にparamsに用意された値を戻し、レンダリング時に使用。

def next(request): #テンプレートに新規作成したページ用のビュー関数nextを定義
  params = {
    'title': 'Hello/Next',
    'msg': 'これは、２つめのページです',
    'goto': 'index'
  }
  return render(request, 'hello/index', params)