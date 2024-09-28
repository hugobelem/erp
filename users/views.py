from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib import messages

from .forms import CustomUserCreationForm, EmpresaForm
from .models import User

from static.assets import avatar

class NavbarContext:
    def __init__(self, request):
        if request.user.is_authenticated:
            self.empresa = request.user.empresa
            self.name = request.user.name
            self.avatar_svg = avatar.generate(self.name)
            self.first_name = self.name.split()[0]

        self.context = {
            'empresa': self.empresa,
            'first_name': self.first_name,
            'avatar': mark_safe(self.avatar_svg)
        }

    def add(self, key, value):
        """Adiciona novas chaves e valores ao dicionário context."""
        self.context[key] = value
        return self.context

    def get(self):
        """Retorna o dicionário context."""
        return self.context

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
    if request.user.is_authenticated:
        return redirect('users:account')

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
    if request.user.is_authenticated:
        empresa = request.user.empresa
        name = request.user.name
        avatar_svg = avatar.generate(name)
        first_name = name.split()[0]


    context = {
        'empresa': empresa,
        'first_name': first_name,
        'avatar': mark_safe(avatar_svg)
    }

    return render(request, 'users/account.html', context)

@login_required(login_url='users:login')
def update_user(request):
    user = request.user
    form = CustomUserCreationForm(instance=user)

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:account')
        else:
            print(form.errors)
    
    context = {'form': form}

    return render(request, 'users/update_user.html', context)