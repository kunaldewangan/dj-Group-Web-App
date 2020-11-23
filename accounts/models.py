from django.db import models
from django.contrib import auth
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

# Create your models here.

class User(auth.models.User,auth.models.PermissionsMixin):
    
    def __str__(self):
        return "@{}".format(self.username)

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE,related_name='profile')
    GENDER_CHOICES = [
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    ]
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES,default='')
    date_of_birth = models.DateField(blank=True,null=True)
    phone_no = models.CharField(max_length=12,default='')
    city = models.CharField(max_length=250,default='')

    def __str__(self):
        return self.user.username
