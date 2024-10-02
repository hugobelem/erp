from django.db import models

class Empresa(models.Model):
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
    cnpj = models.CharField(max_length=50, blank=False, null=True)
    ie = models.CharField(max_length=50, blank=True, null=True)
    logo = models.ImageField(
        blank=True, null=True,
        upload_to='images/logo',
    )

    def __str__(self):
        if self.fantasia:
            return self.fantasia
        else:
            return f'Empresa {self.id}'
        
