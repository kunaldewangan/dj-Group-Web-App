from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug =models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True,default='')
    admin = models.ForeignKey(User,related_name='admin',on_delete=models.CASCADE)
    members = models.ManyToManyField(User,through='GroupMember')
    created_at = models.DateTimeField(auto_now=True)
    private = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:group_detail', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['name']
    

class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='memberships',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group','user')
