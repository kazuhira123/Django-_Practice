from django.shortcuts import render
from django.http import HttpResponse #HttpResponseクラスをimportする
from django.views.generic import TemplateView #TemplateViewクラスを呼び出す
from .forms import HelloForm #forms.pyのHelloFormクラスを呼び出す

class HelloView(TemplateView):
  def __init__(self):
    self.params = {
      'title':'Hello', #テンプレート側で変数として定義した名前をキーとする辞書を作成
      'massage':'your data',
      'form':HelloForm() #formをキーにHelloFormメソッドを呼び出す
    }

  def get(self, request): #GETメソッドで値が渡された時の処理
    return render(request, 'hello/index.html', self.params) #レンダリング時にself.paramsを戻り値として返すだけの処理

  def post(self, request): #POSTメソッドで値が渡された時の処理
    msg = 'あなたは、<b>' + request.POST['name'] + \
      '(' + request.POST['age'] + \
      ') </b>さんです。<br>メールアドレスは<b>' + request.POST['mail'] + \
      '</b> ですね。' #フォームで入力した値をbタグで太字にして表示する値を変数msgへ代入
    self.params['massage'] = msg #self.paramsのキーがmassageの要素の中身を変数msgの値にへ更新
    self.params['form'] = HelloForm(request.POST) #入力した値をクリアさせないための処理
    return render(request, 'hello/index.html', self.params)