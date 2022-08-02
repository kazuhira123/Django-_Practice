from unicodedata import name
from django.db import models #django.dbモジュールから、modelsパッケージをimportする

class Friend(models.Model): #Friendクラスの定義、下記に定義された情報がテーブルの項目と入れる値のデータ型を決定する
  name = models.CharField(max_length=100) #各項目を変数にレコードの定義をインスタンスに記述
  mail = models.EmailField(max_length=200)
  gender = models.BooleanField()
  age = models.IntegerField(default=0)
  birthday = models.DateField()

  def __str__(self): #テキストの値を返す__str__メソッドを定義、これによってFriendクラスのインスタンスを{{}}で表示可能に
      return '<Friend:id=' + str(self.id) + ',' + self.name + '(' + str(self.age) + ')>' #レコードを追加したときの管理ツールでの表示される値を返す

