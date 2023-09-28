from django import forms
from .views import *


class seleccionar(forms.Form):
    def __init__(self, *args, **kwargs):
        facturas = kwargs.pop('facturas', None)
        super(seleccionar, self).__init__(*args, **kwargs)
        for factura in facturas:
            self.fields[f'seleccion_{factura.id}'] = forms.BooleanField(
                required=False,  
                label=f'Seleccionar {factura.nroFactura}',  
            )

