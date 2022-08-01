from secrets import choice
from django import forms

class HelloForm(forms.Form): #HelloFormクラスにforms.Formクラスを継承
  data=[ #変数dataにタプル型の値をリスト化して代入する
    ('one', 'item 1'),
    ('two', 'item 2'),
    ('three', 'item 3')
  ]
  choice = forms.ChoiceField(label='Choice', choices=data) #引数choicesの値にdataを代入