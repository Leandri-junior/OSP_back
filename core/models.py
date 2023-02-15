from django.db import models

# Create your models here.
class DatLog(models.Model):
    dat_insercao = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dat_edicao = models.DateTimeField(auto_now=True, null=True, blank=True)
    dat_delete = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        abstract = True

class EnderecoMeta(models.Model):
    endereco_completo = models.CharField(max_length=250, null=True)

    cep = models.CharField(max_length=8, null=True)
    numero = models.CharField(max_length=30, null=True)
    complemento = models.CharField(max_length=100, null=True)
    bairro = models.CharField(max_length=100, null=True)
    rua = models.CharField(max_length=100, null=True)

    cidade = models.CharField(max_length=100, null=True)
    estado = models.CharField(max_length=20, null=True)

    ponto_referencia = models.CharField(max_length=100, null=True)
    latitude = models.CharField(max_length=200, null=True)
    longitude = models.CharField(max_length=200, null=True)

    class Meta:
        managed = False
        abstract = True