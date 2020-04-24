from django.db import models
from . import gamemode_utilities
# Create your models here.

class MyUser(models.Model):
    username = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created')
    password = models.CharField('password', max_length=128)
    user_id = models.IntegerField()

class GameServer(models.Model):
    server_name = models.CharField(max_length=200)
    server_address = models.CharField(max_length=200)
    server_max_players = models.IntegerField(default=16)
    server_gamemode = models.IntegerField(default=0)
    server_players = models.IntegerField(default=0)
    server_gamemode_name = models.CharField(max_length=200, default="Conquest")