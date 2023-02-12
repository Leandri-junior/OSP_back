from django.shortcuts import render
from django.views import View


# Create your views here.
class Login(View):
    def get(self,request):
        login = self.request.GET.get('login')
        senha = self.request.GET.get('senha')

