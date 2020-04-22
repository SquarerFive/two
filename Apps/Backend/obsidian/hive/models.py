from django.db import models

# Create your models here.

class MyUser(models.Model):
    username = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created')
    password = models.CharField('password', max_length=128)
    user_id = models.IntegerField()

