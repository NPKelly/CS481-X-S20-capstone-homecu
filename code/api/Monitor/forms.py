from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(label='', max_length=12, required=True, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    widgets = {
        'password': forms.PasswordInput(),
    }