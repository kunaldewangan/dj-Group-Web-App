from django.contrib import admin
from . import models
from django.contrib.admin.options import ModelAdmin
# Register your models here.

class GroupAdmin(ModelAdmin):
    list_display = ['name','admin','link','private','created_at']
    list_filter = ['private','created_at']
    search_fields = ['name','admin__username','admin__first_name','admin__last_name','admin__email','link','created_at']
    readonly_fields = ['created_at']

class GroupMemberAdmin(ModelAdmin):
    list_display = ['group','user','joined_at']
    list_filter = ['group__private','joined_at']
    search_fields = ['group__name','user__username','user__first_name','user__last_name','user__email']
    readonly_fields = ['joined_at']

admin.site.register(models.Group,GroupAdmin)
admin.site.register(models.GroupMember,GroupMemberAdmin)
