from django.urls import path, re_path, include

import core.views

urlpatterns = [
    re_path('login/', core.views.Login.as_view(), name='login'),
]
