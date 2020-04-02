from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import LoginForm
from .forms import SignUpForm
from django.contrib.auth import login, authenticate,logout
from django.template import RequestContext

from .authentication_backend import AuthBackend
from .newUser_backend import newUserBackend
from django.core import serializers
from .models import BsuClientlist

data = BsuClientlist.objects.all()

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
	signup_errors = []
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			newUserbackend = newUserBackend()
			authBackend = AuthBackend()
			email = form.cleaned_data['email']
			username = form.cleaned_data['user_name']
			password = form.cleaned_data['password']
			password1 = form.cleaned_data['password1']
			type = form.cleaned_data['type']
			if password == password1:
				checkemail = newUserbackend.checkemail(email=email)
				if checkemail is not None:
					signup_errors.append("Email Already has an Account!")
				else:
					checkusername = newUserbackend.checkusername(username=username)
					if checkusername is not None:
						signup_errors.append("Username Taken")
					else:
						if type == 'Customer':
							newUserbackend.addCustomer(email=email, username=username, password=password)
							user = authBackend.authenticate(username=username, password=password)
							if user is not None:
								login(request=request, user=user)
								return redirect('creditunions')
						else:
							newUserbackend.addStaff(email=email, username=username, password=password)
							user = authBackend.authenticate(username=username, password=password)
							if user is not None:
								login(request=request, user=user)
								return redirect('creditunions')
			else:
				signup_errors.append("Passwords Do Not Match!")
	else:
		form = SignUpForm()
	return render(request, 'newUser.html', {'form': form, 'errors': signup_errors})

def creditunions(request):
    # if request.user.is_authenticated():
    if request.method == 'POST':
        logout(request)
        return redirect('index')

    args = {'data' : data}
    return render(request, 'creditunions.html',args)
    # else:
    #     return render(request,'index',{})

