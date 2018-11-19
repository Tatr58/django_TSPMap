from django.shortcuts import render, get_list_or_404
from .forms import UbigeoForm
from .models import CentroPoblado
from django.conf import settings
from django.core import serializers
import json
from django.http import HttpResponse

# Create your views here.
def viewMap(request):
    if request.method == 'POST':
        form = UbigeoForm(request.POST)
        ubigeo_post = []
        position_val = []

        if form.is_valid():
            ubigeo_post.append(form.cleaned_data['ubigeoOrigen'])
            ubigeo_post.append(form.cleaned_data['ubigeoDestino'])

            cp_queryset = get_list_or_404(CentroPoblado, pk__in=ubigeo_post)

            for cp in cp_queryset:
                position_val.append({'nombre_cp': cp.nombre_cp, 
                                     'latitud': cp.latitud, 
                                     'longitud':cp.longitud})


            return render(request, 'mapaubigeo/index.html', 
                         {'form': form,
                           'position_render': position_val,
                           'origen': cp_queryset[0],
                           'destino': cp_queryset[1],
                           'GOOGLE_API_KEY': settings.GOOGLE_API_KEY
                         })
    else:
        form = UbigeoForm

    return render(request, 'mapaubigeo/index.html', {'form': form})


def filter_cp(request):
    cp_id = None
    return_list = []
    if request.method == 'GET':
        cp_id = request.GET['cp_id']
    
    if cp_id:
        cp_list = CentroPoblado.objects.filter(tipo=cp_id)
        cp_list = [{'id': c.id, 
                    'list': 'CP: {0} DS:{1} PR:{2} RG: {3}'.format(c.nombre_cp, c.distrito, c.provincia, c.region)} 
                    for c in cp_list]
        data = json.dumps({"cp_list": cp_list})

    return HttpResponse(data, content_type='application/json')
