from django.db import models
from django.urls import reverse
from django.conf import settings
from groups.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User,related_name='post_user',on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    group = models.ForeignKey(Group,related_name='post_group',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message
 
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:all_post')

    class Meta:
        ordering = ['group__name','created_at']
    
    

