from django.urls import re_path
import core.cliente.views

urlpatterns = [
    re_path('cadastrar', core.cliente.views.CadastrarPaciente.as_view(), name='cadastrar_paciente'),
]