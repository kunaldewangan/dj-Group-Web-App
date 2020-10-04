from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('',views.ListGroups.as_view(),name='all_groups'),
    path('private/',views.PrivateListGroups.as_view(),name='private_groups'),
    path('private/<slug:slug>/add/member/',views.AddMember.as_view(),name='add_member'),
    path('private/<slug:slug>/remove/member/<str:username>',views.RemoveMember.as_view(),name='remove_member'),
    path('create/',views.CreateGroup.as_view(),name='group_create'),
    path('detail/<slug:slug>',views.DetailGroup.as_view(),name='group_detail'),
    path('delete/<slug:slug>',views.DeleteGroup.as_view(),name='group_delete'),
    path('join/<slug:slug>',views.JoinGroup.as_view(),name='group_join'),
    path('leave/<slug:slug>',views.LeaveGroup.as_view(),name='group_leave'),
]
