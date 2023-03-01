from django.db import models

from core.models import DatLog, EnderecoMeta


class Empresa(DatLog):
    nome = models.CharField(max_length=100, null=True)
    cnpj = models.CharField(max_length=18, null=True)
    cnpj_limpo = models.CharField(max_length=14, null=True)
    razao_social = models.CharField(max_length=200, null=True)
    logo = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = "Empresa"
class FilialEmpresa(DatLog, EnderecoMeta):

    empresa = models.ForeignKey('Empresa', on_delete=models.DO_NOTHING, null=True)
    nome = models.CharField(max_length=100, null=True)
    cnpj = models.CharField(max_length=16, null=True)
    cnpj_limpo = models.CharField(max_length=14, null=True)
    razao_social = models.CharField(max_length=200, null=True)
    filial_numero = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = F"Filial"
