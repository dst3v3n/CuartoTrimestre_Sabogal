from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('lista/' , views.usuariolist , name='usuario_list'),
    path('guardar/' , views.metodo_post , name='formulario')
]