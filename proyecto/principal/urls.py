from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.tipoDeUsuario, name='tipoDeUsuario'),
    path('verSeleccionados/', views.verSeleccionados, name='verSeleccionados'),
    path('admins/', views.admins, name='admins'),
    path('users/', views.users, name='users'),
]


