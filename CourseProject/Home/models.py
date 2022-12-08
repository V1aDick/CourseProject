from django.db import models

class Users(models.Model):
    login = models.CharField(max_length = 15)
    mail = models.EmailField(max_length = 40)
    password = models.CharField(max_length = 20)
    number = models.IntegerField(max_length = 10)