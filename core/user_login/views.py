import json

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import View

class CadastroUser(View):
    def get(self, request):
        pass

class LoginUser(View):
    def get(self, request):
        username = self.request.GET.get('username')
        password = self.request.GET.get('password')
        user = authenticate(username=username, password=password)

        if user:
            return JsonResponse({'status': True, 'descrição': F'seja bem vindo {user.username}'})
        else:
            return JsonResponse({'status': False, 'descrição': 'Senha ou Username invalidos'})

