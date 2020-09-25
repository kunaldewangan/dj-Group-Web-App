from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('create/<slug:slug>/',views.PostCreate,name='post_create'),
    path('delete/<int:pk>/',views.DeletePost.as_view(),name='post_delete'),
]
