from django.contrib import admin
from . import models
from django.contrib.admin import ModelAdmin
# Register your models here.

class PostAdmin(ModelAdmin):
    list_display = ['user','message','group','created_at']
    list_filter = ['group__private','created_at']
    search_fields = ['user__username','user__first_name','user__last_name','user__email','message','group__name','created_at']
    readonly_fields = ['created_at']

admin.site.register(models.Post,PostAdmin)