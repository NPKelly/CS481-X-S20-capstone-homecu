from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import LoginForm
from .forms import SignUpForm
from django.contrib.auth import login, authenticate

from .authentication_backend import AuthBackend
from django.core import serializers
from .models import BsuClientlist

data = serializers.serialize( "python", BsuClientlist.objects.all() )

# Create your views here.
def index(request):
    login_errors = []
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                authBackend = AuthBackend()
                username = form.cleaned_data["user_name"]
                password = form.cleaned_data["password"]
                user = authBackend.authenticate(username=username, password=password)
                if user is not None:
                    # Successful user login
                    login(request=request, user=user)
                    return redirect("creditunions/")
                else:
                    # Failed user login
                    login_errors.append("Invalid Username/password")
            except ValueError:
                # The user is blocked from logging in due to repeated fails
                login_errors.append("Too many failed logins, wait 5 minutes before trying again.")                
        else:
            # Invalid user input
            login_errors.append("Please sumbit both a Username and Password.")
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form, 'errors': login_errors})

def newUser(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['user_name']
			password = form.cleaned_data['password']
			return redirect('creditunions')
	else:
		form = SignUpForm()
	return render(request, 'newUser.html', {'form': form})

def creditunions(request):
    return render(request, 'creditunions.html')
