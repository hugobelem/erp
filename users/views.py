from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib import messages

from .forms import CustomUserCreationForm
from .models import User

from static.assets import avatar


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
    return render(request, 'users/registration/auth.html', context)


def signout(request):
    logout(request)
    return redirect('users:login')


def register(request):
    if request.user.is_authenticated:
        return redirect('users:account')

    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            login(request, user)
            return redirect('users:account')
        else:
            messages.error(request, 'ocorreu um erro')

    context = {'page': page, 'form': form}
    return render(request, 'users/registration/auth.html', context)


def navbar(request):
    if request.user.is_authenticated:
        user = request.user
        svg = avatar.generate(request.user.name)
        first_name = request.user.name.split()[0]

        context = {
            'empresa': user.empresa,
            'first_name': first_name,
            'avatar': mark_safe(svg),
        }
    
    return context


@login_required(login_url='users:login')
def account(request):
    context = {}
    context.update(navbar(request))

    return render(request, 'users/account.html', context)


@login_required(login_url='users:login')
def update_user(request):
    user = request.user
    form = CustomUserCreationForm(instance=user)

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect('users:account')
        else:
            print(form.errors)
    
    context = {'form': form}
    context.update(navbar(request))

    return render(request, 'users/registration/update_user.html', context)
