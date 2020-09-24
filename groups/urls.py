from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('',views.ListGroups.as_view(),name='all_groups'),
    path('create/',views.CreateGroup.as_view(),name='group_create'),
    path('detail/<slug:slug>',views.DetailGroup.as_view(),name='group_detail'),
    path('delete/<slug:slug>',views.DeleteGroup.as_view(),name='group_delete'),
    path('join/<slug:slug>',views.JoinGroup.as_view(),name='group_join'),
    path('leave/<slug:slug>',views.LeaveGroup.as_view(),name='group_leave'),
]
