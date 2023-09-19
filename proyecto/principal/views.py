from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def index(request):
    usuario = request.user.username
    datos = cuadroPrincipal.objects.filter(codigo = usuario)
    return render(request, 'index.html',{
        'datos' : datos, 'usuario' : usuario
    })
