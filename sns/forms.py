import grp
from pyexpat import model
from django import forms #フォームメソッドのimport

#フォームで使用するモデルクラスのimport
from .models import Message,Group,Friend,Good
from django.contrib.auth.models import User

#Messageのフォーム
class MessageForm(forms.ModelForm):
  class Meta:
    model = Message
    fields = ['owner', 'group', 'content']

#Groupのフォーム
class GroupForm(forms.ModelForm):
  class Meta:
    model = Group
    fields = ['owner', 'title']

#Friendのフォーム
class FriendForm(forms.ModelForm):
  class Meta:
    model = Friend
    fields = ['owner', 'user', 'group']

#Goodのフォーム
class GoodForm(forms.ModelForm):
  class Meta:
    model = Good
    fields = ['owner', 'message']

#Groupのチェックボックスフォーム
class GroupCheckForm(forms.Form):
  def __init__(self, user, *args, **kwargs):
    super(GroupCheckForm, self).__init__(*args, **kwargs) #GroupCheckFormクラスインスタンスの基底クラスの__init__を呼び出す
    public = User.objects.filter(username='public').first() #ユーザー名publicで検索し、一番最初のものをUserを取得する
    self.fields['groups'] = forms.MultipleChoiceField( #クラスのフィールドにリスト内包処理で繰り返し処理でリストの項目を生成
      choices=[(item.title, item.title) for item in \
        Group.objects.filter(owner__in=[user,public])], #ownerのユーザーとpublicを検索し繰り返し処理用の変数itemへ代入
        widget=forms.CheckboxSelectMultiple(),
      )

#Groupの選択メニューフォーム
class GroupSelectForm(forms.Form):
  def __init__(self, user, *args, **kwargs):
    super(GroupSelectForm, self).__init__(*args, **kwargs)
    self.fields['groups'] = forms.ChoiceField(
      choices=[('-', '-')] + [(item.title, item.title) \
        for item in Group.objects.filter(owner=user)],
        widget=forms.Select(attrs={'class':'form-control'}),
    )

#Friendのチェックボックスフォーム
class FriendsForm(forms.Form):
  def __init__(self, user, friends=[], vals=[], *args, **kwargs):
    super(FriendsForm, self).__init__(*args, **kwargs)
    self.fields['friends'] = forms.MultipleChoiceField(
      choices=[(item.user, item.user) for item  in friends],
      widget=forms.CheckboxSelectMultiple(),
      initial=vals #初期値の指定
    )

#Group作成フォーム
class CreateGroupForm(forms.Form):
  group_name = forms.CharField(max_length=50, \
    widget=forms.TextInput(attrs={'class':'form-control'}))

#投稿フォーム
class PostForm(forms.Form):
  content = forms.CharField(max_length=500, \
    widget=forms.Textarea(attrs={'class':'form-control', 'rows':2})) #textareaの入力エリアに投稿する用のフォームを作成
  
  def __init__(self, user, *args, **kwargs):
    super(PostForm, self).__init__(*args, **kwargs)
    public = User.objects.filter(username='public').first()
    self.fields['groups'] = forms.ChoiceField(
      choices=[('-', '-')] + [(item.title, item.title) \
        for item in Group.objects. \
          filter(owner__in=[user, public])],
        widget=forms.Select(attrs={'class':'form-control'}),
    )
