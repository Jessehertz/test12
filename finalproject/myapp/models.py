from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    wechat = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
