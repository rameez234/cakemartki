from django.db import models

class Start(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.IntegerField()
    username = models.CharField(max_length=20)
class Enter(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    type = models.IntegerField()
class Item(models.Model):
    cakename = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    cakeid = models.CharField(max_length=20)
    price = models.IntegerField()
    photo = models.FileField()

class Buy(models.Model):
    username=models.ForeignKey(Start,on_delete=models.CASCADE)
    cakename  = models.ForeignKey(Item, on_delete=models.CASCADE)
    date=models.CharField(max_length=30)





