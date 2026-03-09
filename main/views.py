from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import datetime


def main_info(request):
    return render(request, 'index.html')


def main_about(request):
    return render(request, 'about.html')

def main_challenges(request):
    return render(request, 'challenges.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('main:info')

    return render(request, "login.html")

def register_view(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            return redirect("login")

    return render(request, "register.html")