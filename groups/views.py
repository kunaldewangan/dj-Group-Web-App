from django.shortcuts import render
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)

from django.urls import reverse,reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404
from groups.models import Group,GroupMember


class ListGroups(generic.ListView):
    model=Group

class CreateGroup(LoginRequiredMixin,generic.CreateView):
    model = Group
    fields = ('name','description')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.admin = self.request.user
        self.object.save()
        GroupMember.objects.create(user=self.object.admin,group=self.object)
        return super().form_valid(form)

class DetailGroup(generic.DetailView):
    model = Group

class DeleteGroup(LoginRequiredMixin,generic.DeleteView):
    model = Group
    success_url = reverse_lazy('groups:all_groups')

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Group deleted')
        return super().delete(*args, **kwargs)
        

class JoinGroup(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:group_detail',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        except IntegrityError:
            messages.warning(self.request,'warning already a member!')
        else:
            messages.success(self.request,'You are now a member!')
        return super().get(request,*args,**kwargs)

class LeaveGroup(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:group_detail',kwargs={'slug':self.kwargs.get('slug')})
    
    def get(self,request,*args,**kwargs):

        try:
            membership = GroupMember.objects.filter(
                user = self.request.user,
                group__slug=self.kwargs.get('slug')
            )
        except GroupMember.DoesNotExist:
            messages.warning(self.request,'Sorry you are not in this group!')
        else:
            membership.delete()
            messages.success(self.request,'You have left the group!!')

        return super().get(request,*args,**kwargs)




