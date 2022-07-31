from tabnanny import check
from django import forms

class HelloForm(forms.Form): #HelloFormクラスにforms.Formクラスを継承
  name = forms.CharField(label='name', \
    widget=forms.TextInput(attrs={'class':'form-control'})) #文字列のフィールドであるCharFieldを設定、引数にlabelを用意しそれぞれのフィールドの手前にテキストが表示されるようにしている
  mail = forms.CharField(label='mail', \
    widget=forms.TextInput(attrs={'class':'form-control'})) #CharFieldのインスタンス生成時に引数にwidgetを用意してウィジェットクラスを作成している。
  age = forms.IntegerField(label='age', \
    widget=forms.NumberInput(attrs={'class':'form-control'})) #整数の値を入力するためのIntegerFiwldを設定
  check = forms.BooleanField(label='Checkbox', required=False) #チェックボックス用のクラスBooleanFieldを元にcheckインスタンスを生成
  null_check = forms.NullBooleanField(label='null_check')