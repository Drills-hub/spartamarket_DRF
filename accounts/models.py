from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):

    GENDER_CHOICES = [
            ('M', '남성'),
            ('F', '여성'),
            ('O', '기타'),
        ]
    
    name= models.CharField(max_length=30,default='Unknown')
    email = models.EmailField(max_length=30, unique=True)
    nickname = models.CharField(max_length=30)
    birthday= models.DateField()
    gender = models.CharField(max_length=1,choices = GENDER_CHOICES ,null = True, blank= True)
    introduction = models.CharField(max_length=50, null = True, blank= True)



