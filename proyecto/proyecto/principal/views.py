from django.shortcuts import render, redirect
from .models import *
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import seleccionar
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect



@login_required
def tipoDeUsuario(request):
    user = request.user
    if user.username == "administracion":
        return redirect(reverse('admins'))
    
    else:
        return redirect(reverse('users'))


def admins(request):
    facturas = devengados.objects.filter(enviado = True)

    if request.method == 'POST':

        if 'buscar_button' in request.POST:
            codigo = request.POST.get('codigo', '')  
            if codigo:
                facturas = facturas.filter(codigo__iregex = codigo)

            nroFactura = request.POST.get('nroFactura', '')  
            if nroFactura:
                facturas = facturas.filter(nroFactura__iregex = nroFactura)
    
            proveedor = request.POST.get('proveedor', '')  
            if proveedor:
                facturas = facturas.filter(proveedor__iregex = proveedor)

        if 'eliminar_button' in request.POST:
            facturas = devengados.objects.filter(enviado = True)

    return render(request, "principalAdmin.html", {'facturas': facturas, })


def users(request):
    facturas = devengados.objects.filter(codigo=request.user, enviado = False, seleccionar = False)
    todos = devengados.objects.filter(codigo=request.user, enviado = False, seleccionar = True)
    total = 0

    for factura in todos:
        total += factura.importe

    if request.method == 'POST':
        form = seleccionar(request.POST, facturas = facturas)

        if form.is_valid():

            for factura in facturas:
                seleccion_key = f'seleccion_{factura.id}'

                if seleccion_key in form.cleaned_data and form.cleaned_data[seleccion_key]:
                    factura.seleccionar = True
                    factura.save()
        
            if 'buscar_button' in request.POST:

                factura = request.POST.get('factura', '')  
                if factura:
                    facturas = facturas.filter(nroFactura__iregex = factura)
        
                proveedor = request.POST.get('proveedor', '')  
                if proveedor:
                    proveedorIngre = proveedor 
                    facturas.filter(proveedor__iregex = proveedorIngre)

            if 'eliminar_button' in request.POST:
                facturas = devengados.objects.filter(codigo=request.user, enviado = False, seleccionar = False)
            
            if 'form_button' in request.POST:
                return redirect(reverse('verSeleccionados'))

    else:
        form = seleccionar(facturas = facturas)
    
    return render(request, "principal.html", {'form':form, 'facturas':facturas, 'total': total })


def verSeleccionados(request):
    user = request.user
    seleccionados = devengados.objects.filter(codigo=user, seleccionar=True, enviado = False )
    total = 0

    for sele in seleccionados:
        total += sele.importe

    if request.method == 'POST':
        form = seleccionar(request.POST, facturas = seleccionados)

        if form.is_valid():

            for seleccionado in seleccionados:

                borrarSeleccionado = f'borrar_{seleccionado.id}'

                if borrarSeleccionado in request.POST :
                    seleccionado.seleccionar = False
                    seleccionado.save()
                    return redirect(reverse('verSeleccionados'))

            if 'submit' in request.POST:
                seleccionados = seleccionados.filter(seleccionar = True)
                for factura in seleccionados:
                    factura.enviado = True
                    factura.save()
                
            return redirect(reverse('users'))

    return render(request, 'verSeleccionados.html', {'seleccionados': seleccionados, 'total': total})


def masInfo(request, id):
    deven = get_object_or_404(devengados, pk=id)
    return render(request, 'masInfo.html', {'deven': deven})