from django.shortcuts import render, redirect
from .models import *
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import *
from django.urls import reverse
from django.shortcuts import get_object_or_404



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
    datos = devengados.objects.filter(codigo=request.user, enviado = False, seleccionar = False)
    todos = devengados.objects.filter(codigo=request.user, enviado = False, seleccionar = True)
    facturaIngre = None
    proveedorIngre = None
    total = 0

    for dato in todos:
        total += dato.importe

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
                datos = devengados.objects.filter(codigo=request.user, enviado = False, seleccionar = False)
            
            if 'form_button' in request.POST:
                return redirect(reverse('verSeleccionados'))

    else:
        form = seleccionar(datos = datos)
    
    return render(request, "principal.html", {'form':form, 'datos':datos, 'facturaIngre': facturaIngre, 'proveedorIngre': proveedorIngre, 'total': total })


def verSeleccionados(request):

    user = request.user
    seleccionados = devengados.objects.filter(codigo=user, seleccionar=True, enviado = False )

    total = 0

    for sele in seleccionados:
        total += sele.importe

    if request.method == 'POST':
        form = seleccionar(request.POST, datos = seleccionados)

        if form.is_valid():

            for seleccionado in seleccionados:
                seleccion_key = f'seleccion_{seleccionado.id}'

                if seleccion_key in form.cleaned_data and form.cleaned_data[seleccion_key]:
                    seleccionado.seleccionar = False
                    seleccionado.save()

            if 'submit' in request.POST:
                seleccionados = seleccionados.filter(seleccionar = True)
                for dato in seleccionados:
                    dato.enviado = True
                    dato.save()

                
            return redirect(reverse('users'))


    return render(request, 'verSeleccionados.html', {'seleccionados': seleccionados, 'total': total})

def masInfo(request, id):
    deven = get_object_or_404(devengados, pk=id)
    return render(request, 'masInfo.html', {'deven': deven})