from django.contrib import admin
from django.urls import path, include
from .controllers.authController import log_in, sign_up

app_name = 'auth'
urlpatterns = [
    path('', log_in, name='log-in' ),
    path('signup/', sign_up, name='sign-up'),
]
