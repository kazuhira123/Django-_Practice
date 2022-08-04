from secrets import choice
from django import forms

class HelloForm(forms.Form): #HelloFormクラスにforms.Formクラスを継承
  id = forms.IntegerField(label='ID')