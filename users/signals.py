from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Empresa, User

@receiver(post_save, sender=User)
def create_empresa(sender, instance, created, **kwargs):
    if created:
        user = instance
        empresas = Empresa.objects.create(user=user)
