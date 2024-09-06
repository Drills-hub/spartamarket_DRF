from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=30, unique=True)
    nickname = models.CharField(max_length=30)
    birthday= models.DateField()
    gender = models.CharField(max_length=20,null = True, blank= True)
    introduction = models.CharField(max_length=50, null = True, blank= True)



