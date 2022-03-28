from os import name
from django.db import models

# Create your models here.

class user ( models.Model):
    name= models.CharField(max_length=50)
    phone_no=models.CharField(max_length=12)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=500)

class contact(models.Model):
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    phone =models.CharField(max_length=13)
    Address = models.CharField(max_length=100)
    # img= models.ImageField(upload_to="media/")
    user_id= models.IntegerField()


