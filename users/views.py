from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import views as auth_views
from django.contrib import messages

from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.utils.decorators import method_decorator

from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
    CustomPasswordChangeForm,
)
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
    return render(request, 'registration/auth.html', context)


def signout(request):
    logout(request)
    return redirect('login')


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

    context = {'page': page, 'form': form}
    return render(request, 'registration/auth.html', context)


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


@login_required(login_url='login')
def account(request):
    context = {}
    context.update(navbar(request))

    return render(request, 'users/account.html', context)


def user(request):
    context= {}
    context.update(navbar(request))

    return render(request, 'users/pages/user.html', context)


@login_required(login_url='login')
def update_user(request):
    user = request.user
    form = CustomUserChangeForm(instance=user)

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect('users:account')
    
    context = {'form': form}
    context.update(navbar(request))

    return render(request, 'users/pages/update_user.html', context)


@login_required(login_url='login')
def delete_user(request):
    user = request.user
    
    if request.method == "POST":
        user.delete()
        return redirect('index')
    
    context = {'user': user}
    return render(request, 'users/registration/update_user.html', context)


class ChangePasswordView(auth_views.PasswordChangeView):    
    form_class = CustomPasswordChangeForm    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(navbar(self.request))
        return context
    
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

class ChangeDonePasswordView(auth_views.PasswordChangeDoneView):    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(navbar(self.request))
        return context
    
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)