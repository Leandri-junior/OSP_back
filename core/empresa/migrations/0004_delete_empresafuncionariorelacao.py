# Generated by Django 4.1.7 on 2023-02-22 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_alter_empresa_cnpj'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmpresaFuncionarioRelacao',
        ),
    ]