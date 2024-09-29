from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.account, name='account'),

    path('sair/', views.signout, name='logout'),

    path('usuario/', views.user, name='user'),
    path('usuario/editar', views.update_user, name='update_user'),
    path('usuario/exluir', views.delete_user, name='delete_user'),

    path('empresa/', views.empresa, name='empresa'),
    path('empresa/editar', views.update_empresa, name='update_empresa'),
]
