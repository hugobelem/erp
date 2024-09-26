from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete


class Empresa(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    razao_social = models.CharField(max_length=255, blank=True, null=True)
    fantasia = models.CharField(max_length=255, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    segmento_atuacao = models.CharField(max_length=255, blank=True, null=True)
    tipo_pessoa = models.CharField(max_length=50, blank=True, null=True)
    cpf_cnpj = models.CharField(max_length=50, blank=True, null=True)
    inscricao_estadual = models.CharField(max_length=50, blank=True, null=True)
    logo = models.ImageField(
        blank=True, null=True,
        upload_to='images/logo',
        default='logo/avatar.jpg'
    )

    def __str__(self):
        if self.fantasia:
            return self.fantasia
        else:
            return f'Empresa de {self.user.first_name}'


@receiver(post_save, sender=User)
def create_empresa(sender, instance, created, **kwargs):
    if created:
        user = instance
        empresas = Empresa.objects.create(user=user)

@receiver(post_delete, sender=Empresa)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()