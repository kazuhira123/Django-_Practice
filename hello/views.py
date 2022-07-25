from django.shortcuts import render
from django.http import HttpResponse #HttpResponseクラスをimportする

def index(request, id, nickname): #HttpRequestクラスの引数requestを返すindex関数の定義、引数にurls.pyで定義したアドレスidとnicknameを追加
  result = 'your id: ' + str(id) + ', name: "' \
    + nickname + '" .' #idとnicknameに設定された値がresultに代入される
  return HttpResponse(result)

  '''
  クエリパラメーターを使って表示を変更していた時の記述
  if 'msg' in request.GET: #GETの辞書の中にmsgというキーの値が保管されている時の条件分岐
    msg = request.GET['msg'] #HttpRequestクラスのGET属性(クエリパラメーターの値等の入っている辞書)を使って&msg=◯◯として送られた値を取り出している
    result = 'you typed: "' + msg + '" .' #変数resultに指定の文字列とパラメーターに記述した値を代入
  else:
    result = 'Please send msg parameter' #msgパラメーターを送信する旨を変数resultに代入
  return HttpResponse(result) #戻り値としてHttpResponseインスタンスの引数に変数resultを返す
  '''