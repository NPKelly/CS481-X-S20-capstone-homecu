from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(label='Username', max_length=12, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    widgets = {
        'password': forms.PasswordInput(),
    }