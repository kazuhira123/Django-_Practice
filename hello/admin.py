from django.contrib import admin
from .models import Friend, Message #FriendモデルとMessageモデルのimport

admin.site.register(Friend) #Friendモデルを管理ツールに登録する
admin.site.register(Message) #Messageモデルを管理ツールに登録する