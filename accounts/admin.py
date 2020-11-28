from django.contrib import admin
from . import models
from django.contrib.admin.options import ModelAdmin
# Register your models here.

class ProfileAdmin(ModelAdmin):
    list_display = ['user','gender','date_of_birth','phone_no','city','profile_picture','last_update']
    list_filter = ['gender','last_update']
    search_fields = ['user__username','user__first_name','user__last_name','user__email','gender','date_of_birth','phone_no','city']
    readonly_fields = ['last_update']

admin.site.register(models.Profile,ProfileAdmin)