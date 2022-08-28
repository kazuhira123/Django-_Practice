from tkinter.messagebox import NO
from django.test import TestCase

from django.contrib.auth.models import User
from .models import Message

class SnsTest(TestCase):
  def test_check(self):
    x = True
    self.assertTrue(x) #値がTrueであるかのチェック
    y = 100
    self.assertGreater(y, 0) #2つの値のどちらが大きいかのチェック
    arr = [10, 20, 30]
    self.assertIn(20, arr)
    nn = None
    self.assertIsNone(nn) #値がNoneになっているかのチェック

class SnsTests(TestCase):
  def test_model(self):
    usr = User.objects.first()
    self.assertIsNotNone(usr)
    msg = Message.objects.first()
    self.assertIsNotNone(msg)