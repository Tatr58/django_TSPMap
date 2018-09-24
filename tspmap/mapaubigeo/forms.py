from django import forms
from .models import CentroPoblado

class UbigeoForm(forms.Form):
    ubigeoOrigen = forms.ModelChoiceField(queryset=CentroPoblado.objects.all(), 
                                                empty_label="Centro Poblado Origen", label='Ubigeo Origen',
                                                 widget=forms.Select(
                                                 attrs={'class': 'form-control'}))
    ubigeoDestino = forms.ModelChoiceField(queryset=CentroPoblado.objects.all(), 
                                                empty_label="Centro Poblado Destino", label='Ubigeo Destino',
                                                 widget=forms.Select(
                                                 attrs={'class': 'form-control'}))