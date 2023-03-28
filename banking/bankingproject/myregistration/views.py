from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    return render(request, "register.html")


def register(request):
    return render(request, "login.html")


def new(request):
    return render(request, "about.html")


def form(request):
    return render(request, "form.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
