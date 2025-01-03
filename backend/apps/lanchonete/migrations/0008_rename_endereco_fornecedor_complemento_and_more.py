# Generated by Django 5.1.1 on 2024-10-26 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lanchonete', '0007_alter_produto_data_validade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fornecedor',
            old_name='endereco',
            new_name='complemento',
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='bairro',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='cep',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='cidade',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='estado',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='logradouro',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='numero',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
