from django import forms
from .models import CentroPoblado
from .models import TIPO_UBIGEO

class UbigeoForm(forms.Form):
    tipoCp = forms.CharField(label='Tipo de Centro Poblado',
                            widget=forms.Select(
                            choices=TIPO_UBIGEO,
                            attrs={'class': 'form-control'}))

    ubigeoOrigen = forms.CharField(label='Ubigeo Origen',
                                   widget=forms.Select(
                                   choices=CentroPoblado.objects.none(),                                        
                                   attrs={'class': 'form-control', 'disabled':'true'}))

    ubigeoDestino = forms.CharField(label='Ubigeo Destino',
                                    widget=forms.Select(
                                    choices=CentroPoblado.objects.none(),                                        
                                    attrs={'class': 'form-control', 'disabled':'true'}))