# Generated by Django 4.1.7 on 2023-02-23 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0009_funcionario_dat_nasc_funcionario_imagem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='local_nascimento',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='nascionalidade',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='naturalidade',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
