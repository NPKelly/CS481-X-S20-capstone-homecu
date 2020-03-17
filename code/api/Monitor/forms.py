from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    user_name = forms.CharField(label='', max_length=12, required=True, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    widgets = {
        'password': forms.PasswordInput(),
    }

class SignUpForm(forms.Form):
    
    email = forms.CharField(label='', max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    user_name = forms.CharField(label='', max_length=12, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    widgets = {
        'password': forms.PasswordInput(),
	'password1': forms.PasswordInput(),
    }
