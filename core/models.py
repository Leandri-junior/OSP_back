from django.db import models

# Create your models here.
class DatLog(models.Model):
    dat_insercao = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dat_edicao = models.DateTimeField(auto_now=True, null=True, blank=True)
    dat_delete = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        abstract = True
