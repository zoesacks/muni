from django.shortcuts import render
from .models import *

def index(request):
    datos = cuadroPrincipal.objects.all()
    return render(request, 'index.html',{
        'datos' : datos
    })
