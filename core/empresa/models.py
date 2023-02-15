from django.db import models

from core.models import DatLog, EnderecoMeta


class Empresa(DatLog, EnderecoMeta):
    pass
    #nome
    #cnpj
    #razao_social


