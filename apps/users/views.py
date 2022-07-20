from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import AppUser
from .forms import RegisterForm

# Create your views here.

def signup(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account successfully created for user: " + username)

            return redirect('login')

    context = {'form': form}
    return render(request, "users/signup.html", context)

def signin(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            print(f'Request user: {request.user}, Request email: {request.user.email}')
            
            return redirect('index')
        else:
            print("ERROR: User has not been authenticated")
            messages.info(request, "Email Address OR Password is incorrect")

    context = {}
    return render(request, "users/login.html", context)


def logoutUser(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect('index')
    logout(request)
    return redirect('login')


def userProfile(request: HttpRequest, username):
    if not request.user.is_authenticated:
        return redirect('login')
    
    context = {}
    return render(request, "users/profile.html", context)