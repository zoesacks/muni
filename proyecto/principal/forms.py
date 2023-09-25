from collections.abc import Mapping
from typing import Any
from django import forms
from django.forms.utils import ErrorList
from .models import devengados
from .views import *


class enviar(forms.Form):
   volver = forms.BooleanField(required=False, widget=forms.HiddenInput(), initial=True)


class seleccionar(forms.Form):
    def __init__(self, *args, **kwargs):
        datos = kwargs.pop('datos', None)
        super(seleccionar, self).__init__(*args, **kwargs)
        for dato in datos:
            self.fields[f'seleccion_{dato.id}'] = forms.BooleanField(
                required=False,  
                label=f'Seleccionar {dato.nroFactura}',  
            )

