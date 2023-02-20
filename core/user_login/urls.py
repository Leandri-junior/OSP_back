from django.urls import path, re_path, include
from django.views.decorators.csrf import csrf_exempt

import core.user_login.views

urlpatterns = [
    re_path('login', csrf_exempt(core.user_login.views.LoginUser.as_view()), name='user_login'),
    re_path('cadastrar', csrf_exempt(core.user_login.views.CadastroUser.as_view()), name='cadastrar'),
]
