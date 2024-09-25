from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            print('username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('users:account')
        else:
            print('usuário ou senha incorreto')

    return render(request, 'users/login.html')


def signout(request):
    logout(request)
    return redirect('users:login')


def account(request):
    return render(request, 'users/account.html')