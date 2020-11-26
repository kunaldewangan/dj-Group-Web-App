from django.db import models
from django.contrib import auth
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
import os
from uuid import uuid4

# Create your models here.

class User(auth.models.User,auth.models.PermissionsMixin):
    
    def __str__(self):
        return "@{}".format(self.username)

def user_directory_path(instance, filename): 
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{0}.{1}'.format(instance.user.username, ext)
    else:
        # set filename as random string
        filename = '{0}.{1}'.format(uuid4().hex, ext)
    return 'profile_picture/{0}'.format(filename) 

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
    profile_picture = models.ImageField(upload_to=user_directory_path,default='profile_picture/default_profile.png',blank=True)

    def __str__(self):
        return self.user.username

# django-signal
@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)