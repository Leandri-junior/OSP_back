from django.db import models

from core.models import EnderecoMeta
from core.user_login.models import Pessoa


class Cliente(Pessoa, EnderecoMeta):
    pagamento = models.CharField(max_length=30, null=True) #TODO: FK para tabela de pagamento // a fazer
    anamnese = models.CharField(max_length=30, null=True) #TODO: FK para tabela de anamnese // a fazer
    exame_medico = models.CharField(max_length=30, null=True) #TODO: FK para tabela de anamnese // a fazer
    tratamento = models.CharField(max_length=30, null=True)  # TODO: FK para tabela de anamnese // a fazer
    avaliacao = models.CharField(max_length=30, null=True)  # TODO: FK para tabela de anamnese // a fazer

    class Meta:
        db_table = 'Cliente'