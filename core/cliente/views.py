from django.shortcuts import render
from django.views import View


# Create your views here.
class CadastrarPaciente(View):
    def post(self, *args, **kwargs):
        dados = self.request.POST.get('dados')