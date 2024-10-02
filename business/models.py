from django.db import models

class Business(models.Model):
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
        

class Customer(models.Model):
    nome = models.CharField(max_length=255, blank=True, null=True)
    apelido = models.CharField(max_length=255, blank=True, null=True)
    código = models.CharField(max_length=255, null=True, blank=True)
    cpf = models.IntegerField(blank=True, null=True)
    cep = models.IntegerField(blank=True, null=True)
    cidade = models.CharField(max_length=255, blank=True, null=True)
    up = models.CharField(max_length=2, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=50, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)


class Product(models.Model):
    descricao = models.CharField(max_length=255, blank=True, null=True)
    código = models.CharField(max_length=255, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    unidade = models.CharField(max_length=25, blank=True, null=True)
    estoque = models.IntegerField(blank=True, null=True)
    marca = models.CharField(max_length=255, blank=True, null=True)
    custo = models.IntegerField(blank=True, null=True)
    criado = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    numero = models.IntegerField(unique=True)
    produto = models.ManyToManyField(Product, through='OrderItem')
    cliente = models.ForeignKey(Customer, on_delete=models.CASCADE)
    itens = models.PositiveIntegerField()
    desconto = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    criado = models.DateTimeField(auto_now_add=True)
    recebimento = models.CharField(max_length=255, blank=True, null=True)
    categoria = models.CharField(max_length=255, blank=True, null=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    desconto = models.IntegerField()
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)