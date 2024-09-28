from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib.auth import views as auth_views
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('conta/', include('users.urls')),

    path(
        'recuperar-senha/', 
        auth_views.PasswordResetView.as_view(),
        name='reset_password'
    ),
    path(
        'recuperar-senha/enviar/', 
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        'recuperar-senha/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'recuperar-senha/fim/', 
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),

    path(
        'conta/usuario/alterar-senha/',
        views.ChangePasswordView.as_view(),
        name='password_change'
    ),
    path(
        'conta/usuario/alterar-senha/fim/',
        views.ChangeDonePasswordView.as_view(
            template_name='users/registration/password_change_done.html'
        ),
        name='password_change_done'
    ),
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
    )
