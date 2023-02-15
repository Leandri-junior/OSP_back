from django.urls import path, re_path, include

import core.user_login.views

urlpatterns = [
    re_path('user_login/', core.user_login.views.LoginUser.as_view(), name='user_login'),
]
