from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'users/login.html')

def profile(request):
    return render(request, 'users/profile.html')