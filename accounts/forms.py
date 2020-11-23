from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models

class UserCreateForm(UserCreationForm):
    
    class Meta:
        fields = ('username','first_name','last_name','email','password1','password2')
        model = get_user_model()

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = models.Profile
        fields = ('gender','date_of_birth','phone_no','city')
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'].label = 'Gender'
        self.fields['date_of_birth'].label = 'Date Of Birth'
        self.fields['date_of_birth'].help_text = 'Format is YYYY-MM-DD'