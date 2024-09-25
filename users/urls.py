from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.signin, name='login'),
    path('profile/', views.profile, name='profile'),
]
