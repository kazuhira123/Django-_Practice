from django.shortcuts import render
from django.http import HttpResponse #HttpResponseクラスをimportする
from .forms import HelloForm #forms.pyのHelloFormクラスを呼び出す

def index(request):
  params = {
    'title':'Hello', #テンプレート側で変数として定義した名前をキーとする辞書を作成
    'massage':'your data',
    'form':HelloForm() #formをキーにHelloFormメソッドを呼び出す
  }
  if (request.method == 'POST'): #フォームに値が入力したときの処理
    params['massage'] = '名前：' + request.POST['name'] + \
      '<br>メール' + request.POST['mail'] + \
      '<br>年齢' +request.POST['age'] #paramsにmassageをキーとした要素を作成し、フォームに入力されたそれぞれの値を表示する。<br>は改行の意味
    params['form'] = HelloForm(request.POST) #辞書paramsのformキーの要素の値をHelloFormクラスのrequest.POSTの値へ更新
  return render(request, 'hello/index.html', params) #テンプレートをレンダリングするrender関数の第2引数にtemplatesフォルダ内のパス、第3引数にparamsに用意された値を戻し、レンダリング時に使用。
