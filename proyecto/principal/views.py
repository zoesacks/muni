from django.shortcuts import render, redirect
from .models import *
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
import pdb


@login_required
def tipoDeUsuario(request):

    user = request.user

    if user.username == "administracion":
        return redirect(reverse('admins'))
    
    else:
        return redirect(reverse('users'))


def admins(request):
    facturaIngre = None
    proveedorIngre = None
    datos = devengados.objects.filter(enviado = True)

    if request.method == 'POST':
        
        if 'fact_button' in request.POST:
            factura = request.POST.get('factura', '')  
            if factura:
                facturaIngre = factura 
                datos = datos.filter(nroFactura__iregex = facturaIngre)

        if 'prove_button' in request.POST:
            proveedor = request.POST.get('proveedor', '')  
            if proveedor:
                proveedorIngre = proveedor 
                datos = datos.filter(proveedor__iregex = proveedorIngre)

        if 'eliminar_button' in request.POST:
            datos = devengados.objects.filter(enviado = True)


    return render(request, "principalAdmin.html", {'datos': datos, 'facturaIngre': facturaIngre, 'proveedorIngre': proveedorIngre})


def users(request):
    datos = devengados.objects.filter(codigo=request.user, enviado = False)
    facturaIngre = None
    proveedorIngre = None

    if request.method == 'POST':
        form = seleccionar(request.POST, datos = datos)

        if form.is_valid():

            for dato in datos:
                seleccion_key = f'seleccion_{dato.id}'

                if seleccion_key in form.cleaned_data and form.cleaned_data[seleccion_key]:
                    dato.seleccionar = True
                    dato.save()
        
            if 'fact_button' in request.POST:
                factura = request.POST.get('factura', '')  
                if factura:
                    facturaIngre = factura 
                    datos = datos.filter(nroFactura__iregex = facturaIngre)

            if 'prove_button' in request.POST:
                proveedor = request.POST.get('proveedor', '')  
                if proveedor:
                    proveedorIngre = proveedor 
                    datos = datos.filter(proveedor__iregex = proveedorIngre)

            if 'eliminar_button' in request.POST:
                datos = devengados.objects.filter(codigo=request.user, enviado = False)
            
            if 'form_button' in request.POST:
                return redirect(reverse('verSeleccionados'))
        


            
            
    else:
        form = seleccionar(datos = datos)
    
    return render(request, "principal.html", {'form':form, 'datos':datos, 'facturaIngre': facturaIngre, 'proveedorIngre': proveedorIngre })


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