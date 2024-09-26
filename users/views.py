from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import CustomUserCreationForm
from .models import Empresa


def signin(request):
    page = 'signin'

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

    context = {'page': page}
    return render(request, 'users/auth.html', context)


def signout(request):
    logout(request)
    return redirect('users:login')


def register(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower().strip()
            user.save()

            login(request, user)
            return redirect('users:account')
        else:
            messages.error(request, 'ocorreu um erro')

    context = {'page': page, 'form': form}
    return render(request, 'users/auth.html', context)


@login_required(login_url='users:login')
def account(request):
    empresa = None
    if request.user.is_authenticated:
        empresa = request.user.empresa

    context = {'empresa': empresa}
    return render(request, 'users/account.html', context)

