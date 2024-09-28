from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.conf import settings

import os

from .models import Empresa, User

@receiver(post_save, sender=User)
def create_empresa(sender, instance, created, **kwargs):
    if created:
        user = instance
        empresas = Empresa.objects.create(user=user)


@receiver(post_delete, sender=Empresa)
def auto_delete_logo_on_delete(sender, instance, **kwargs):
    logo = instance.logo
    if logo:
        if os.path.isfile(instance.logo.path):
            os.remove(instance.logo.path)
