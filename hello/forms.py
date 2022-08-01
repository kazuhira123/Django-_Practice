from secrets import choice
from django import forms

class HelloForm(forms.Form): #HelloFormクラスにforms.Formクラスを継承
  data=[ #変数dataにタプル型の値をリスト化して代入する
    ('one', 'item 1'),
    ('two', 'item 2'),
    ('three', 'item 3')
  ]
  choice = forms.MultipleChoiceField(label='radio', choices=data, \
    widget=forms.SelectMultiple(attrs={'size':3})) #引数choicesの値にdataを代入したchoiceインスタンスを生成、さらにwidget引数にSelectのインスタンスを作成して選択リストを作成できるようにした