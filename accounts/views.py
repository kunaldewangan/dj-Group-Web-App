from django.shortcuts import render
from django.urls import reverse_lazy 
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from . import models
from django.views.generic import CreateView
from . import forms
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

@login_required(login_url='/accounts/login/')
def set_profile(request):
    try:
        profile = request.user.profile
    except models.Profile.DoesNotExist:
        profile = models.Profile(user=request.user)
        profile.save()

    if request.method == 'POST':
        profile_form = forms.UserProfileForm(request.POST)
        if profile_form.is_valid():
            profile_update = models.Profile.objects.get(
                user = request.user
            )
            profile_update.gender = profile_form.cleaned_data['gender']
            profile_update.date_of_birth = profile_form.cleaned_data['date_of_birth']
            profile_update.phone_no = profile_form.cleaned_data['phone_no']
            profile_update.city = profile_form.cleaned_data['city']
            profile_update.save()
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            return HttpResponse('Form is not Valid!')
    else:
        profile_form = forms.UserProfileForm(instance=profile)
        return render(request,'accounts/my_profile.html',{'form':profile_form})

@login_required(login_url='/accounts/login/')
def show_profile(request,username):
    try:
        profile = get_user_model().objects.get(username=username)
        return render(request,'accounts/show_profile.html',{'u_profile':profile})
    except get_user_model().DoesNotExist:
        return HttpResponse('Profile Not Found!')