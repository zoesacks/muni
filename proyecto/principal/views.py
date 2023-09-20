from django.shortcuts import render, redirect
from .models import *
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import *


def index(request):
    if request.method == 'POST':
        form = CuadroPrincipalForm(request.POST)

        if form.is_valid():
            seleccionados = form.cleaned_data['selccionar']

            for cuadro in seleccionados:
                cuadro.selccionar = cuadro in seleccionados
                cuadro.save()
    else:
        form = CuadroPrincipalForm()

    return render(request, "index.html", {'form':form})
    
