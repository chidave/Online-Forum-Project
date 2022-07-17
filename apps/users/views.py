from django.shortcuts import render
from django.http import HttpRequest

from .forms import RegisterForm

# Create your views here.

def signup(request: HttpRequest):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, "users/signup.html", context)

def login(request):
    return render(request, "users/login.html")
