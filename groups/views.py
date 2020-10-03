from django.shortcuts import render
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)
from django.contrib.auth import get_user_model
from django.urls import reverse,reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404
from groups.models import Group,GroupMember
from . import forms

User = get_user_model()

class ListGroups(generic.ListView):
    model=Group
    def get_queryset(self):
        return super().get_queryset().filter(private=False)

class PrivateListGroups(LoginRequiredMixin,generic.ListView):
    model = Group
    template_name = 'groups/group_p_list.html'
    def get_queryset(self):
        return super().get_queryset().filter(members=self.request.user,private=True)
    

class CreateGroup(LoginRequiredMixin,generic.CreateView):
    model = Group
    fields = ('name','description','private')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.admin = self.request.user
        self.object.save()
        GroupMember.objects.create(user=self.object.admin,group=self.object)
        return super().form_valid(form)

class DetailGroup(LoginRequiredMixin,generic.DetailView):
    model = Group
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["member_form"] = forms.AddMemberForm
        return context
    

class DeleteGroup(LoginRequiredMixin,generic.DeleteView):
    model = Group
    success_url = reverse_lazy('groups:all_groups')

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Group deleted')
        return super().delete(*args, **kwargs)
        
class AddMember(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:group_detail',kwargs={'slug':self.kwargs.get('slug')})

    def post(self,request,*args,**kwargs):
        member_form = forms.AddMemberForm(request.POST)
        if member_form.is_valid():
            group = get_object_or_404(Group,slug=self.kwargs.get('slug'))
            user = get_object_or_404(User,username=member_form.cleaned_data['username'])
            try:
                GroupMember.objects.create(user=user,group=group)
            except IntegrityError:
                messages.warning(self.request,'warning already a member!')
            else:
                messages.success(self.request,'You are now a member!')

        return super().post(request,*args,**kwargs)

class RemoveMember(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:group_detail',kwargs={'slug':self.kwargs.get('slug')})
    
    def get(self,request,*args,**kwargs):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        try:
            group_member = GroupMember.objects.filter(
                user = user,
                group__slug=self.kwargs.get('slug')
            )
        except GroupMember.DoesNotExist:
            messages.warning(self.request,'Sorry user is not in this group!')
        else:
            group_member.delete()
            messages.success(self.request,'You have left the group!!')

        return super().get(request,*args,**kwargs)


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




