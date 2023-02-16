from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
import core.empresa.models
import core.models



class Pessoa(core.models.DatLog):
    nm_completo = models.CharField(max_length=200, null=True)
    nm_primeiro = models.CharField(max_length=200, null=True)
    nm_ultimo = models.CharField(max_length=200, null=True)

    cpf = models.BigIntegerField(null=True)
    cpf_form = models.CharField(max_length=20, null=True)

    rg = models.CharField(max_length=15, null=True)
    rg_form = models.CharField(max_length=15, null=True)

    # passaporte = models.CharField(max_length=200, null=True)
    # passaporte_form = models.CharField(max_length=200, null=True)
    #
    # dat_nasc = models.DateField(null=True)
    #
    # imagem = models.FileField(upload_to='fotos/usuarios', default='fotos/sem-foto.png', null=True)
    #
    # nm_mae = models.CharField(max_length=200, null=True)
    # nm_pai = models.CharField(max_length=200, null=True)
    #
    # cr_codigo = models.CharField(max_length=50, null=True)
    # cr_uf = models.ForeignKey('core.UF', on_delete=models.DO_NOTHING, null=True,
    #                           related_name='%(app_label)s_%(class)s_cr_uf')
    #

    class Meta:
        abstract = True


class Profile(AbstractBaseUser, core.models.DatLog, core.models.EnderecoMeta):
    # conta_user = models.OneToOneField('ContaUser', on_delete=models.DO_NOTHING, null=True)
    # tipo_conta = models.CharField(null=True, max_length=200, default='usr')
    username = models.CharField(max_length=200, unique=True)
    USERNAME_FIELD = 'username'
    is_staff = models.BooleanField(null=True, default=False)
    is_atualizar_sessao = models.BooleanField(default=False, null=True)
    is_primeiro_login = models.BooleanField(default=True, null=True)
    is_resetar_senha = models.BooleanField(default=False, null=True)
    senha_padrao = models.CharField(null=True, max_length=200)

    class Meta:
        abstract = True


class FuncionarioLogin(Profile):
    funcionario = models.OneToOneField('Funcionario', on_delete=models.DO_NOTHING, null=True)
    objects = UserManager()

class Funcionario(Pessoa):
    cargo = models.CharField(null=True, max_length=200)
