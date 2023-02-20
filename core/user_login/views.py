import json

import jwt
from django.contrib.auth import authenticate, login, user_logged_in
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework_jwt.utils import jwt_payload_handler

import core.user_login.models
from OSP import settings


class CadastroUser(View):
    def get(self, request):
        pass

class LoginUser(View):

    def post(self, request):

        response = json.loads(self.request.body)
        usuario = core.user_login.models.FuncionarioLogin.objects.all()
        user = authenticate(username=response['username'], password=response['password'])

        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = {}
                user_details['name'] = "%s %s" % (
                    user.nm_primeiro, user.nm_ultimo)
                user_details['token'] = token
                user_logged_in.send(sender=user.__class__,
                                    request=request, user=user)
                response = {
                    'user': user_details['name'],
                    'token': user_details['token'].decode('UTF-8'),
                    'status': status.HTTP_200_OK
                }
                return JsonResponse(response)
            except Exception as e:
                raise e

