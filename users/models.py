from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = models.CharField(
        max_length=100, unique=True, blank=True, null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


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
    cpf_cnpj = models.CharField(max_length=50, blank=False, null=True)
    inscricao_estadual = models.CharField(max_length=50, blank=True, null=True)
    logo = models.ImageField(
        blank=True, null=True,
        upload_to='images/logo',
    )

    def __str__(self):
        if self.fantasia:
            return self.fantasia
        else:
            return f'Empresa de {self.user.email}'
