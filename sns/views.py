#外部のメソッドとクラスのimport
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User #ユーザー認証機能をimport
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required #ログイン用の機能をimport

#snsアプリケーション内のクラスのimport
from .models import Message,Friend,Group,Good
from .forms import GroupCheckForm,GroupSelectForm,FriendsForm,CreateGroupForm,PostForm

#indexのビュー関数
@login_required(login_url='/admin/login/') #/admin/login/へのログインが必須となるアノテーションを設定
def index(request, page=1):
  #publicのuserを取得
  (public_user, public_group) = get_public()

  #POST送信時の処理
  if request.method == 'POST':
    #Groupsのチェックを更新した時の処理
    #フォームの用意
    checkform = GroupCheckForm(request.user, request.POST) #アクセス時のユーザーとチェックボックスの選択状態を引数にしてGroupCheckFormのインスタンスを生成
    #チェックされたGroup名をリストにまとめる
    glist = []
    for item in request.POST.getlist('groups'): #チェックされたgroupsモデルのデータを代入する繰り返し処理
      glist.append(item) #代入されたgroupsのデータをリストへ追加
    #Messageの取得
    messages = get_your_group_message(request.user, glist, page) #アクセス時のユーザー、チェックされたgroupsのデータ、ページ数を引数にget_your_group_messageメソッドをmessagesに代入

  #GETアクセス時の処理
  else:
    #フォームの用意こ
    checkform = GroupCheckForm(request.user)  #アクセス時のユーザー情報を元にGroupCheckFormのインスタンスを生成
    #Groupのリストを取得
    gps = Group.objects.filter(owner=request.user) #Groupモデルの中から、利用者がアクセス時のユーザーのデータを検索する
    glist = [public_group.title] #publicのGroupが設定されたデータをglistに代入
    for item in gps:
      glist.append(item.title) #Groupの中で検索されたデータのタイトルを繰り返しglistに追加
    #メッセージの取得
    messages = get_your_group_message(request.user, glist, page)
  
  #共通処理
  params = {
    'login_user':request.user, #現在アクセスしているユーザーがログイン時のユーザーとして保管
    'contents':messages,
    'check_form':checkform,
  }
  return render(request, 'sns/index.html', params)

@login_required(login_url='/admin/login/')
def groups(request):
  #自分が登録したFriendを取得
  friends = Friend.objects.filter(owner=request.user) #Friendモデルの中からアクセス時のユーザーと利用者が一致するレコードを検索してfriendsに代入

  #POST送信時の処理
  if request.method == 'POST':

    #Groupメニュー選択肢の処理
    if request.POST['mode'] == '__groups_form__':
      #選択したGroup名を取得
      sel_group = request.POST['groups'] #選択されたgroupsの情報をsel_groupに代入
      #Groupを取得
      gp = Group.objects.filter(owner=request.user) \
        .filter(title=sel_group).first() #利用者がアクセス時のユーザーかつメニューで選択されたgroupを検索し最初のものをgpに代入
      #Groupに含まれるFriendを取得
      fds = Friend.objects.filter(owener=request.user) \
        .filter(group=gp) #利用者がアクセス時のユーザーかつ、選択されたgroupと一致するFriendモデルのレコードを検索しfdsに代入
      print(Friend.objects.filter(owner=request.user)) #利用者がアクセス時のユーザーのFriendモデルのレコードを出力
      #FriendのUserをリストにまとめる
      vlist = []
      for item in fds:
        vlist.append(item.user.username) #上記で検索したFriendモデルのレコードのユーザー名をリストに追加
      #フォームの用意
      groupsform = GroupSelectForm(request.user, request.POST) #indexと同じ処理
      friendsform = FriendsForm(request.user, \
        friends=friends, vals=vlist) #アクセス時のユーザーとFriendモデルのリスト、選択されたFriendを表示するリストの中身を引数にしてFriendsFormインスタンス生成
    
    #Friendsのチェック更新時の処理
    if request.POST['mode'] == '__friends_form__':
      #選択したGroupの取得
      sel_group = request.POST['group'] #選択されたgroupの値をsel_groupに代入
      group_obj = Group.objects.filter(title=sel_group).first() #Groupモデルの中から選択されたグループと一致する一番最初のレコードを検索
      print(group_obj) #検索したレコードを表示
      #チェックしたFriendsを取得
      sel_fds = request.POST.getlist('friends') #送信されたfirendsの値をリスト化して取得
      #FriendsのUserを取得
      sel_users = User.objects.filter(username__in=sel_fds) #User内のユーザー名が上記で取得したfriendsのリストに含まれているかを検索
      #Userのリストに含まれるユーザーが登録したFriendを取得
      fds = Friend.objects.filter(owner=request.user) \
        .filter(user__in=sel_users) #上記で検索したUserを元にFriendモデルを検索
      #全てのFriendにGroupを設定し保存する
      vlist = []
      for item in fds: #取得したFriendsモデルを元に繰り返し処理を実行
        item.group = group_obj #Friendのgroupに選択されたgroupを代入
        item.save() #上記のレコードの保存
        vlist.append(item.user.username) #リスト選択したFriendsモデルのユーザー名を追加
      #メッセージを設定
      messages.success(request, 'チェックされたFriendを' + \
        sel_group + 'に登録しました') #メッセージフレームワークでシステムメッセージを表示
      #フォームの用意
      groupsform = GroupSelectForm(request.user, \
        {'groups':sel_group})
      friendsform = FriendsForm(request.user, \
        friends=friends, vals=vlist)
    
    #GETアクセス時の処理
    else:
      #フォームの用意
      groupsform = GroupSelectForm(request.user) #アクセス時のユーザーを元にグループ選択用のインスタンスを生成
      friendsform = FriendsForm(request.user, friends=friends, vals=[]) #アクセス時のユーザーとFriendモデルのリスト、選択されたFriendを表示するリストの中身を空にしてfriendsformに代入
      sel_group = '-' #GETアクセス時なのでgroupの選択がないことを表示
    
    #共通処理
    createform = CreateGroupForm() #グループ作成用のインスタンスを生成
    params = {
      'login_user':request.user,
      'groups_form':groupsform,
      'friends_form':friendsform,
      'create_form':createform,
      'group':sel_group,
    }
    return render(request, 'sns/groups.html', params)

#Friendの追加処理
@login_required(login_url='/admin/login/')
def add(request):
  #追加するUserを取得
  add_name = request.GET['name'] #Friend登録するユーザーの名前をadd_nameに代入
  add_user = User.objects.filter(username=add_name).first() #上記で代入した値とUserのユーザー名が最初に一致するものを取得
  #Userが本人だった場合の処理
  if add_user == request.user:
    messages.info(request, "自分自身をFriendに追加することはできません")
    return redirect(to='/sns')
  #publicの取得
  (public_user, public_group) = get_public()
  #add_userのFriendの数を調べる
  frd_num = Friend.objects.filter(owner=request.user) \
    .filter(user=add_user).count()
  #0より大きければ既に登録済み
  if frd_num > 0:
    messages.info(request, add_user.username + 'は既に追加されています')
    return redirect(to='/sns')
  
  #ここからFriendの登録処理
  frd = Friend() #Friendモデルのインスタンスを生成してfrdに代入
  frd.owner = request.user #登録者をアクセス時のユーザーに設定
  frd.user = add_user #登録するユーザーをadd_userに設定
  frd.group = public_group #Friendモデルのgroup情報をpublicグループに設定
  frd.save() #上記内容を保存
  #メッセージを設定
  messages.success(request, add_user.username + 'を追加しました！ \
    groupページに移動して、追加したFriendをメンバーに設定してください')
  return redirect(to='/sns') #snsアプリケーションのホームへリダイレクト

#グループの作成処理
@login_required(login_url='/admin/login/')
def creategroup(request):
  #Groupを作り、Userとtitleを設定して保存する
  gp = Group()
  gp.owner = request.user
  gp.title = request.user.username + 'の' + request.POST['group_name'] #グループのタイトルを「[グループ作成者]の[グループ名]」の形で表示
  gp.save()
  messages.info(request, '新しいグループを作成しました')
  return redirect(to='/sns/groups')

#メッセージのポスト処理
@login_required(login_url='/admin/login/')
def post(request):
  #POST送信時の処理
  if request.method == 'POST':
    #送信内容の取得
    gr_name = request.POST['groups'] #投稿されたgroupsの値をgr_nameに代入
    content = request.POST['content'] #投稿されたcontentの値をcontentに代入
    #Groupの取得
    group = Group.objects.filter(owner=request.user) \
      .filter(title=gr_name).first() #Groupモデル内の投稿グループと位置する情報を取得
    if group == None: #投稿されたgroupが存在しない時の処理
      (pub_user, group) = get_public() #publicのgroupを取り出す
    #Messageを作成し設定して保存
    msg = Message() #Messageインスタンスを生成してmsgに代入
    msg.owner = request.user #投稿者はアクセス時のユーザー
    msg.group = group #groupは投稿時のgroup
    msg.content = content #投稿した内容は投稿時のcontent
    msg.save() #上記を保存
    #メッセージを設定
    messages.success(request, '新しいメッセージを投稿しました!')
    return redirect(to='/sns')
  
  #GETアクセス時の処理
  else:
    form = PostForm(request.user)

  #共通処理
  params = {
    'login_user':request.user,
    'form':form,
  }
  return render(request, 'sns/post.html', params)

#投稿をシェアする
@login_required(login_url='/admin/login/')
def share(request, share_id):
  #シェアするMessageの取得
  share = Message.objects.get(id=share_id)
  print(share)
  #POST送信時の処理
  if request.method == 'POST':
    #送信内容を取得
    gr_name = request.POST['groups']
    content = request.POST['content']
    #Groupの取得
    group = Group.objects.filter(owner=request.user) \
      .filter(title=gr_name).first()
    if group == None:
      (pub_user, group) = get_public()
    #メッセージを作成し、設定し保存
    msg = Message()
    msg.owner = request.user
    msg.group = group
    msg.content = content
    msg.share_id = share.id
    msg.save()
    share_msg = msg.get_share()
    share_msg.share_count += 1
    share_msg.save()
    #メッセージを設定
    messages.success(request, 'メッセージをシェアしました！')
    return redirect(to='/sns')
  
  #共通処理
  form = PostForm(request.user)
  params = {
    'login_user':request.user,
    'form':form,
    'share':share,
  }
  return render(request, 'sns/share.html', params)

#goodボタンの処理
@login_required(login_url='/admin/login/')
def good (request, good_id):
  #goodするMessageを取得
  good_msg = Message.objects.get(id=good_id) #goodした時のidとMessageモデルのidが一致するものを取得
  #自分がメッセージにGoodした数を調べる
  is_good = Good.objects.filter(owner=request.user) \
    .filter(message=good_msg).count()
  #0より大きければ既にgood済み
  if is_good > 0:
    messages.success(request, '既にメッセージにはgoodしています')
    return redirect(to='/sns')
  
  #Messageのgood_countを1増やす
  good_msg.good_count += 1
  good_msg.save()
  #Goodを作成し、設定し保存する
  good = Good()
  good.owner = request.user
  good.message = good_msg
  good.save()
  #メッセージを設定
  messages.success(request, 'メッセージにgoodしました!')
  return redirect(to='/sns')

#これ以降は普通の関数===========================

#指定されたグループおよび検索文字によるMessageの取得
def get_your_group_message(owner, glist, page):
  page_num = 10 #ページあたりの表示数
  #publicの取得
  (public_user, public_group) = get_public()
  #チェックされたGroupの取得
  groups = Group.objects.filter(Q(owner=owner) \
    |Q(owner=public_user)).filter(title__in=glist)
  #Groupに含まれるFriendの取得
  me_friends = Friend.objects.filter(group__in=groups)
  #FriendのUserをリストにまとめる
  me_users = []
  for f in me_friends:
    me_users.append(f.user)
  #UserリストのUserが作ったGroupの取得
  his_groups = Group.objects.filter(owner__in=me_users)
  his_friends = Friend.objects.filter(user=owner) \
    .filter(group__in=his_groups)
  me_groups = []
  for hf in his_friends:
    me_groups.append(hf.group)
  #groupがgroupsに含まれるか、me_groupsに含まれるMessageの取得
  messages = Message.objects.filter(Q(group__in=groups) \
    |Q(group__in=me_groups))
  #ページネーションで指定ページを取得
  page_item = Paginator(messages, page_num)
  return page_item.get_page(page)

#publicなUserとGroupを取得する
def get_public():
  public_user = User.objects.filter(username='public').first() #User内のユーザー名がpublicのものを取得
  public_group = Group.objects.filter(owner=public_user).first() #Groupモデル内の作成者がpublicとなっているものを取得
  return (public_user, public_group)