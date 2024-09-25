from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect('users:account')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, '')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('users:account')
        else:
            messages.error(request, 'dados incorretos')

    return render(request, 'users/auth.html')


def signout(request):
    logout(request)
    return redirect('users:login')


def register(request):
    return render(request, 'users/auth.html')

@login_required(login_url='users:login')
def account(request):
    return render(request, 'users/account.html')

