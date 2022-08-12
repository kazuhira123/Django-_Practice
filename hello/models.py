import re #Pythonの正規表現モジュールをimport
from sqlite3 import paramstyle
from django.db import models #django.dbモジュールから、modelsパッケージをimportする
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator #モデルルール用のバリデーターをimport
from django.core.validators import ValidationError

def number_only(value):
  if (re.match(r'^[0-9]*$', value) == None): #reモジュールのmatch関数を用いて入力されたテキストが指定のパターンと合致するかチェック
    raise ValidationError(
      '%(value)s is not Number!', \
      params={'value':value}
    )

class Friend(models.Model): #Friendクラスの定義、下記に定義された情報がテーブルの項目と入れる値のデータ型を決定する
  name = models.CharField(max_length=100, \
    validators=[number_only]) #自分で定義したバリデーター用の関数をバリデーションとして設定
  mail = models.EmailField(max_length=200)
  gender = models.BooleanField()
  age = models.IntegerField(validators=[ \
    MinValueValidator(0), \
    MaxValueValidator(150)]) #項目ageに最小値と最大値のバリデーションを設定
  birthday = models.DateField()

  def __str__(self): #テキストの値を返す__str__メソッドを定義、これによってFriendクラスのインスタンスを{{}}で表示可能に
      return '<Friend:id=' + str(self.id) + ',' + self.name + '(' + str(self.age) + ')>' #レコードを追加したときの管理ツールでの表示される値を返す

