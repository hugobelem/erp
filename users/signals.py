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


@receiver(pre_save, sender=Empresa)
def auto_delete_logo_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    
    try:
        old_logo = Empresa.objects.get(pk=instance.pk).logo
    except Empresa.DoesNotExist:
        return False
    
    new_logo = instance.logo
    if not old_logo:
        pass
    elif not old_logo == new_logo:
        if os.path.isfile(old_logo.path):
            os.remove(old_logo.path)
