#外部のメソッドとクラスのimport
from django import shortcuts
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

#snsアプリケーション内のクラスのimport
from .models import Message,Friend,Group,Good
from .forms import GroupCheckForm,GroupSelectForm,FriendsForm,CreateGroupForm,PostForm

#indexのビュー関数
@login_required(login_url='admin/login/')
def index(request, page=1):
  #publicのuserを取得
  (public_user, public_group) = get_public()

  #POST送信時の処理
  if request.method == 'POST':
    #Groupsのチェックを更新した時の処理
    #フォームの用意
    checkform = GroupCheckForm(request.user, request.POST)
    #チェックされたGroup名をリストにまとめる
    glist = []
    for item in request.POST.getlist('groups'):
      glist.append(item)
    #Messageの取得
    messages = get_your_group_message(request.user, glist, page)

  #GETアクセス時の処理
  else:
    #フォームの用意
    checkform = GroupCheckForm(request.user)
    #Groupのリストを取得
    gps = Group.objects.filter(owner=request.user)
    glist = [public_group.title]
    for item in gps:
      glist.append(item.title)
    #メッセージの取得
    messages = get_your_group_message(request.user, glist, page)
  
  #共通処理
  params = {
    'login_user':request.user,
    'contents':messages,
    'check_form':checkform,
  }
  return render(request, 'sns/index.html', params)

