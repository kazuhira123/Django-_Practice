from django import forms

class HelloForm(forms.Form): #HelloFormクラスにforms.Formクラスを継承
  check = forms.NullBooleanField(label='check') #プルダウン用のクラスNullBooleanFieldクラスを元にcheckインスタンスを生成