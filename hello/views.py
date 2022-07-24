from django.shortcuts import render
from django.http import HttpResponse #HttpResponseクラスをimportする

def index(request): #HttpRequestクラスの引数requestを返すindex関数の定義
  if 'msg' in request.GET: #GETの辞書の中にmsgというキーの値が保管されている時の条件分岐
    msg = request.GET['msg'] #HttpRequestクラスのGET属性(クエリパラメーターの値等の入っている辞書)を使って&msg=◯◯として送られた値を取り出している
    result = 'you typed: "' + msg + '" .' #変数resultに指定の文字列とパラメーターに記述した値を代入
  else:
    result = 'Please send msg parameter' #msgパラメーターを送信する旨を変数resultに代入
