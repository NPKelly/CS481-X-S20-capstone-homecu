from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class LoginForm(forms.Form):
    user_name = forms.CharField(label='', max_length=12, required=True, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    widgets = {
        'password': forms.PasswordInput(),
    }


Admin_Choices=[
    ('Customer','Customer'),
    ('Staff','Staff')
]

class SignUpForm(forms.Form):    
    email = forms.CharField(label='', max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    user_name = forms.CharField(label='', max_length=12, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    type = forms.CharField(label='Type of User', widget=forms.RadioSelect(choices=Admin_Choices))
    widgets = {
        'password': forms.PasswordInput(),
	'password1': forms.PasswordInput(),
    }
