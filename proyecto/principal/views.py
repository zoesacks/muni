from django.shortcuts import render
from .models import *

def post_list(request):
    viewCuadro = cuadroPrincipal.objects.all()
    return render(request, 
                'index.html',
                context= {'viewCuadro': viewCuadro},)
