import imp
from re import A
from secrets import choice
from unicodedata import name
from django import forms
from .models import Friend

class HelloForm(forms.Form): #HelloFormクラスにforms.Formクラスを継承
  name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class':'form-control'})) #フォームの項目を追加し、それぞれのwidget引数にBootstrapのクラスを設定
  mail = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
  gender = forms.BooleanField(label='Gender', required=False, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
  age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'class':'from-control'}))
  birthday = forms.DateField(label='Birth', widget=forms.DateInput(attrs={'class':'form-control'}))

class CheckForm(forms.Form):
  str = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class':'form-control'}))
  Empty = forms.CharField(label='Empty', empty_value=True, widget=forms.TextInput(attrs={'class':'form-control'}))
  min = forms.CharField(label='Min', min_length=5, widget=forms.TextInput(attrs={'class':'form-control'}))
  max = forms.IntegerField(label='Max', max_value=10000, widget=forms.NumberInput(attrs={'class':'form-control'}))

class FriendForm(forms.ModelForm): #ModelFormクラスを継承したFriendFormクラスを定義
  class Meta: #ModelFormの内部クラスMetaの定義(メタクラスと呼ばれるらしい)
    model = Friend #モデルクラスの設定
    fields = ['name', 'mail', 'gender', 'age', 'birthday'] #フィールドの設定

class FindForm(forms.Form):
  find = forms.CharField(label='find', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))