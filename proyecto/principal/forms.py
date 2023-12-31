from collections.abc import Mapping
from typing import Any
from django import forms
from django.forms.utils import ErrorList
from .models import devengados
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
