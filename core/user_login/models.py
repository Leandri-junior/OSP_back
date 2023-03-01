from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

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
    is_estrangeiro =models.BooleanField(default=False)
    passaporte = models.CharField(max_length=200, null=True)
    passaporte_form = models.CharField(max_length=200, null=True)
    local_nascimento = models.CharField(max_length=200, null=True)
    dat_nasc = models.DateField(null=True)
    naturalidade = models.CharField(max_length=200, null=True)
    nascionalidade = models.CharField(max_length=200, null=True)


    imagem = models.FileField(upload_to='fotos/usuarios', default='fotos/sem-foto.png', null=True)

    nm_mae = models.CharField(max_length=200, null=True)
    nm_pai = models.CharField(max_length=200, null=True)
    SEXO = (
        ('F', _('Femenino')),
        ('M', _('Masculino')),
        ('O', _('Outros'))
    )
    sexo = models.CharField(max_length=1, choices=SEXO, null=True)


    class Meta:
        abstract = True



class Profile(AbstractBaseUser, core.models.DatLog, PermissionsMixin):
    empresa = models.ForeignKey('empresa.Empresa', on_delete=models.DO_NOTHING, null=True)
    filial = models.ForeignKey('empresa.FilialEmpresa', on_delete=models.DO_NOTHING, null=True)
    tipo_conta = models.CharField(null=True, max_length=200, default='usr')
    username = models.CharField(max_length=200, unique=True)
    USERNAME_FIELD = 'username'
    is_staff = models.BooleanField(null=True, default=False)
    is_atualizar_sessao = models.BooleanField(default=False, null=True)
    is_primeiro_login = models.BooleanField(default=True, null=True)
    is_resetar_senha = models.BooleanField(default=False, null=True)
    senha_padrao = models.CharField(null=True, max_length=200)
    senha_padrao = models.CharField(null=True, max_length=200)
    email = models.EmailField(max_length=200, null=True)
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="%(app_label)s_%(class)s_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="%(app_label)s_%(class)s_user_set",
        related_query_name="user",
    )

    class Meta:
        abstract = True


class FuncionarioLogin(Profile):
    funcionario = models.OneToOneField('Funcionario', on_delete=models.DO_NOTHING, null=True)
    nm_primeiro = models.CharField(max_length=200, null=True)
    nm_ultimo = models.CharField(max_length=200, null=True)
    objects = UserManager()

    class Meta:
        db_table = 'FuncionarioLogin'

class Funcionario(Pessoa, core.models.EnderecoMeta):
    cargo = models.CharField(null=True, max_length=200)
    class Meta:
        db_table = 'Funcionario'