from django.urls import path

from . import views

app_name = 'business'
urlpatterns = [
    path('', views.empresa, name='empresa'),
    path('editar/', views.empresa_update, name='empresa_update'),
]
