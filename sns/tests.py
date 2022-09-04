from tokenize import group
from turtle import title
from django.test import TestCase

from django.contrib.auth.models import User
from .models import Group,Message

class SnsTest(TestCase):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    (usr, grp) = cls.create_user_and_group() #テスト用のユーザーとグループ用のインスタンス生成
    cls.create_message(usr, grp) #作成されたユーザーとグループをもとにメッセージを作成

  @classmethod
  def create_user_and_group(cls):
    #Create public user & public group
    User(username="public", password="public", is_staff=False,
      is_active=True).save() #Userクラス内にテスト用のユーザーpublicを追加
    pb_usr = User.objects.filter(username='public').first()
    Group(title='public', owner_id=pb_usr.id).save() #作成したpublicを作成者としたグループを作成
    pb_grp = Group.objects.filter(title='public').first() #作成されたグループを検索しpb_grpに代入

    #Create test user
    User(username="test", password="test", is_staff=True,
      is_active=True).save() #テスト用のユーザーtestを作成
    usr = User.objects.filter(username='test').first() #作成したユーザーを検索し、usrに代入

    return (usr, pb_grp)

  @classmethod
  def create_message(cls, usr, grp):
    Message(content='this is test message.', owner_id=usr.id,
      group_id=grp.id).save() #Messageクラスにテスト用のサンプルメッセージを5つ作成する
    Message(content='test', owner_id=usr.id, group_id=grp.id).save()
    Message(content="ok", owner_id=usr.id, group_id=grp.id).save()
    Message(content="ng", owner_id=usr.id, group_id=grp.id).save()
    Message(content="finish", owner_id=usr.id, group_id=grp.id).save()

  def test_check(self):
    usr = User.objects.filter(username='test').first() #テスト用のデータベースからUserのオブジェクトを取得する

    msg = Message.objects.filter(content='test').first()
    self.assertIs(msg.owner_id, usr.id) #msgのowner_idがusr.idと一致するかのチェク
    self.assertEqual(msg.owner.username, usr.username) #msgのowner.usernameとusr.usernameが一致するかのチェック
    self.assertEqual(msg.group.title, 'public') #msgのgroup.titleがpublicと一致するかのチェック

    msgs = Message.objects.filter(content__contains="test").all()
    self.assertIs(msgs.count(), 2) #contentにtestの文字列を含むMessageが2個あるかのチェック
    c = Message.objects.all().count()
    self.assertIs(c, 5) #Messageのレコード数が5個かのチェック

    msg1 = Message.objects.all().first()
    msg2 = Message.objects.all().last()
    self.assertIsNot(msg1, msg2) #Messageの最初と最後が異なる値かのチェック