from django.db import models

from core.models import DatLog, EnderecoMeta


class Empresa(DatLog):
    nome = models.CharField(max_length=100, null=True)
    cnpj = models.CharField(max_length=16, null=True)
    cnpj_limpo = models.CharField(max_length=14, null=True)
    razao_social = models.CharField(max_length=200, null=True)


class FilialEmpresa(DatLog, EnderecoMeta):
    empresa = models.ForeignKey('Empresa', on_delete=models.DO_NOTHING, null=True)
    nome = models.CharField(max_length=100, null=True)
    cnpj = models.CharField(max_length=16, null=True)
    cnpj_limpo = models.CharField(max_length=14, null=True)
    razao_social = models.CharField(max_length=200, null=True)
    filial_numero = models.CharField(max_length=100, null=True)

class EmpresaFuncionarioRelacao(DatLog):
    empresa = models.ForeignKey('Empresa', on_delete=models.DO_NOTHING, null=True)
    filial = models.ForeignKey('FilialEmpresa', on_delete=models.DO_NOTHING, null=True )
    funcionario = models.ForeignKey('user_login.Funcionario', on_delete=models.DO_NOTHING, null=True, related_name='%(app_label)s_%(class)s_empresa')
