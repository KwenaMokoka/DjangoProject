from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def user_login(request):
    return render(request, 'login.html')

def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('parents:home'))
        else:
            # Handle invalid login credentials here
            return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        return HttpResponseRedirect(reverse('user_auth:login'))


def show_user(request):

        return render(request, 'parents/home.html')

    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user_auth:login'))

    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))