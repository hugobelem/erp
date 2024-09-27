from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.account, name='account'),

    path('login/', views.signin, name='login'),
    path('sair/', views.signout, name='logout'),

    path('usuario/editar', views.update_user, name='update_user'),

    path("cadastro/", views.register, name="register"),
]
