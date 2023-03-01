# Generated by Django 4.1.7 on 2023-02-23 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0008_funcionariologin_empresa_funcionariologin_filial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='dat_nasc',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='imagem',
            field=models.FileField(default='fotos/sem-foto.png', null=True, upload_to='fotos/usuarios'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='is_estrangeiro',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='nm_mae',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='nm_pai',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='passaporte',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='passaporte_form',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='sexo',
            field=models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Outros')], max_length=1, null=True),
        ),
    ]