from django.shortcuts import render
from django.http import HttpResponse #HttpResponseクラスをimportする

def index(request):
  return render(request, 'hello/index.html') #テンプレートをレンダリングするrender関数の第2引数にtemplatesフォルダ内のパスを指定する