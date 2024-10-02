# Generated by Django 5.1.1 on 2024-10-02 01:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_rename_cpf_cnpj_business_cnpj_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=255, null=True)),
                ('apelido', models.CharField(blank=True, max_length=255, null=True)),
                ('código', models.CharField(blank=True, max_length=255, null=True)),
                ('cpf', models.IntegerField(blank=True, null=True)),
                ('cep', models.IntegerField(blank=True, null=True)),
                ('cidade', models.CharField(blank=True, max_length=255, null=True)),
                ('up', models.CharField(blank=True, max_length=2, null=True)),
                ('endereco', models.CharField(blank=True, max_length=255, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('bairro', models.CharField(blank=True, max_length=255, null=True)),
                ('complemento', models.CharField(blank=True, max_length=255, null=True)),
                ('celular', models.IntegerField(blank=True, null=True)),
                ('nascimento', models.DateField(blank=True, null=True)),
                ('sexo', models.CharField(blank=True, max_length=50, null=True)),
                ('observacoes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
                ('código', models.CharField(blank=True, max_length=255, null=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unidade', models.CharField(blank=True, max_length=25, null=True)),
                ('estoque', models.IntegerField(blank=True, null=True)),
                ('marca', models.CharField(blank=True, max_length=255, null=True)),
                ('custo', models.IntegerField(blank=True, null=True)),
                ('criado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(unique=True)),
                ('itens', models.PositiveIntegerField()),
                ('desconto', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('recebimento', models.CharField(blank=True, max_length=255, null=True)),
                ('categoria', models.CharField(blank=True, max_length=255, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('desconto', models.IntegerField()),
                ('preco_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.order')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='produto',
            field=models.ManyToManyField(through='business.OrderItem', to='business.product'),
        ),
    ]
