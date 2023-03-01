
class Login:
    def get_empresa(self, user):
        empresa = {
            'id': user.empresa.id,
            'nome':user.empresa.nome,
            'logo': user.empresa.logo

        }

        return empresa