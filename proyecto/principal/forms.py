from django import forms
from .models import cuadroPrincipal



class CuadroPrincipalForm(forms.Form):
    selccionar = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        queryset=cuadroPrincipal.objects.all(),
    )
    emision = forms.CharField(max_length=10, required=False, label='Emisión')

    class Meta:
        model = cuadroPrincipal
        fields = '__all__' 