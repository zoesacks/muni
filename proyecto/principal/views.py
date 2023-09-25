from django.shortcuts import render, redirect
from .models import *
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404


@login_required
def tipoDeUsuario(request):

    user = request.user

    if user.username == "administracion":
        return redirect(reverse('admins'))
    
    else:
        return redirect(reverse('users'))


def admins(request):
    datos = devengados.objects.filter(enviado = True)
    return render(request, "principalAdmin.html", {'datos': datos})


def users(request):

    datos = devengados.objects.filter(codigo=request.user, enviado = False)

    if request.method == 'POST':

        form = seleccionar(request.POST, datos = datos)

        if form.is_valid():

            for dato in datos:

                seleccion_key = f'seleccion_{dato.id}'
                if seleccion_key in form.cleaned_data and form.cleaned_data[seleccion_key]:
                    dato.seleccionar = True
                    dato.save()

            return redirect(reverse('verSeleccionados'))
            
    else:
        form = seleccionar(datos = datos)

    return render(request, "principal.html", {'form':form, 'datos':datos})


def verSeleccionados(request):

    user = request.user
    seleccionados = devengados.objects.filter(codigo=user, seleccionar=True, enviado = False )
    todos = devengados.objects.all()

    if request.method == 'POST':
        form = enviar(request.POST)

        if 'submit' in request.POST and form.is_valid():
            for dato in seleccionados:
                dato.enviado = True
                dato.save()

        if 'volver' in request.POST and form.is_valid():
            for dato in todos:
                dato.seleccionar = False
                dato.save()
        
        return redirect(reverse('users'))
    
    else: 
        form = enviar()

    return render(request, 'verSeleccionados.html', {'seleccionados': seleccionados, 'form': form})

def masInfo(request, id):
    deven = get_object_or_404(devengados, pk=id)
    return render(request, 'masInfo.html', {'deven': deven})