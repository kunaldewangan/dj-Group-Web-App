from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.views import generic
from braces.views import SelectRelatedMixin
from groups.models import Group
from . import forms
from . import models
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# Create your views here.

User = get_user_model()

@login_required(login_url='/accounts/login/')
def PostCreate(request,slug):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            form_temp = form.save(commit=False)
            form_temp.user = request.user
            form_temp.group = get_object_or_404(Group,slug=slug)
            form_temp.save()
            return HttpResponseRedirect(reverse('posts:post_create',kwargs={'slug':slug}))
        else: HttpResponse('your form is not valid..')
    else:
        post_list = models.Post.objects.filter(group__slug=slug)
        post_form = forms.PostForm()
        group = get_object_or_404(Group,slug=slug)
        return render(request,'posts/post_chat.html',{'post_form':post_form,'post_list':post_list,'group':group})
    

class DeletePost(LoginRequiredMixin,generic.DeleteView):
    model = models.Post
    
    def delete(self,*args,**kwargs):
        self.object = self.get_object()
        return super().delete(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('posts:post_create',kwargs={'slug':self.object.group.slug})