from django import forms

class AddMemberForm(forms.Form):
    username = forms.CharField(max_length=150)

