from django import forms
from .models import devengados
from .views import *


class enviar(forms.Form):
   volver = forms.BooleanField(required=False, widget=forms.HiddenInput(), initial=True)

class devengadosForm(forms.ModelForm):
    class Meta:
        model = devengados
        fields = ['nroFactura'] 

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(devengadosForm, self).__init__(*args, **kwargs)

        self.fields['seleccionar'] = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            queryset=devengados.objects.filter(codigo=user, enviado = False),
        )