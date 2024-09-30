# Generated by Django 5.1.1 on 2024-09-30 00:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_remove_business_user'),
        ('users', '0002_remove_user_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='business',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.business'),
        ),
    ]
