from django.shortcuts import render, redirect
from .models import *
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect

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
    user = request.user
    
    if request.method == 'POST':

        form = devengadosForm(request.POST, user=request.user)

        if form.is_valid():
            seleccionados = form.cleaned_data['seleccionar']

            for dato in seleccionados:
                dato.seleccionar = True
                dato.save()
            
            return redirect(reverse('verSeleccionados'))
    
    else:
        form = devengadosForm(user=request.user)

    datos = devengados.objects.filter(codigo=user, enviado = False)

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
        
        return redirect(reverse('principal'))
    
    else: 
        form = enviar()

    return render(request, 'verSeleccionados.html', {'seleccionados': seleccionados, 'form': form})

