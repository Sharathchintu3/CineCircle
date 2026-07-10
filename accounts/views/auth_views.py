from django.shortcuts import render, redirect
from django.template.context_processors import request

from accounts.forms import UserRegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "base.html")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("account:login")\

    else:
        form = UserRegisterForm()

    return render(
        request, "accounts/register.html", {"form":form}
    )

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(request, f'welcome back, {user.username}!')
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html",{"form": form},)

def user_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("home")
