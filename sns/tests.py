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
    usr = User.objects.first() #テスト用のデータベースからUserのオブジェクトを取得する
    self.assertIsNotNone(usr)
    msg = Message.objects.first()
    self.assertIsNotNone(msg)