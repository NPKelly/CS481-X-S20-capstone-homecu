from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import LoginForm
from .authentication_backend import AuthBackend
from django.core import serializers
from .models import BsuClientlist

data = serializers.serialize( "python", BsuClientlist.objects.all() )

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            authBackend = AuthBackend()
            username = form.cleaned_data["user_name"]
            password = form.cleaned_data["password"]
            user = authBackend.authenticate(username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                return redirect("creditunions/")
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})

def creditunions(request):
    return render(request, 'creditunions.html')