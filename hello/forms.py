from django import forms

class HelloForm(forms.Form): #HelloFormクラスにforms.Formクラスを継承
  name = forms.CharField(label='name') #文字列のフィールドであるCharFieldを設定、引数にlabelを用意しそれぞれのフィールドの手前にテキストが表示されるようにしている
  mail = forms.CharField(label='mail')
  age = forms.IntegerField(label='age') #整数の値を入力するためのIntegerFiwldを設定