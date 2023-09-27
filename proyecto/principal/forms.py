from collections.abc import Mapping
from typing import Any
from django import forms
from django.forms.utils import ErrorList
from .models import devengados
from .views import *




class seleccionar(forms.Form):
    def __init__(self, *args, **kwargs):
        datos = kwargs.pop('datos', None)
        super(seleccionar, self).__init__(*args, **kwargs)
        for dato in datos:
            self.fields[f'seleccion_{dato.id}'] = forms.BooleanField(
                required=False,  
                label=f'Seleccionar {dato.nroFactura}',  
            )

class deseleccionar(forms.Form):
    def __init__(self, *args, **kwargs):
        seleccionados = kwargs.pop('seleccionados', None)
        super(deseleccionar, self).__init__(*args, **kwargs)
        for seleccionados in seleccionados:
            self.fields[f'seleccion_{seleccionados.id}'] = forms.BooleanField(
                required=False,  
                label=f'Seleccionar {seleccionados.nroFactura}',
                initial=False, 
            )

class filtrarFactura(forms.ModelForm):
    class Meta:
        model = devengados
        fields = ['nroFactura']
