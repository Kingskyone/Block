from django.db import models

class Users(models.Model):
    nid = models.AutoField(primary_key=True)
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=16)
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    time = models.CharField(max_length=32)
    basicpwd = models.CharField(max_length=16)
    aut = models.IntegerField()

class Bloks(models.Model):
    nid = models.AutoField(primary_key=True)
    bk_title = models.CharField(max_length=32)
    bk_describe = models.CharField(max_length=64)
    bk_text = models.CharField(max_length=2048)
    bk_author = models.CharField(max_length=32)  #昵称
    bk_love = models.IntegerField()
    bk_time = models.CharField(max_length=32)

class Talk(models.Model):
    nid = models.AutoField(primary_key=True)
    tk_bk = models.IntegerField()
    tk_author = models.CharField(max_length=32)
    tk_text = models.CharField(max_length=128)
    tk_time = models.CharField(max_length=32)

class LoginTime(models.Model):
    nid = models.AutoField(primary_key=True)
    tk_user = models.CharField(max_length=32)
    tk_time = models.CharField(max_length=32)