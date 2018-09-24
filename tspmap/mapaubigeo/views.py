from django.shortcuts import render, get_list_or_404
from .forms import UbigeoForm
from .models import CentroPoblado
from django.conf import settings

# Create your views here.
def viewMap(request):
    if request.method == 'POST':
        form = UbigeoForm(request.POST)
        ubigeo_post = []
        position_val = []

        if form.is_valid():
            ubigeo_post.append(form.cleaned_data['ubigeoOrigen'].id)
            ubigeo_post.append(form.cleaned_data['ubigeoDestino'].id)

            cp_queryset = get_list_or_404(CentroPoblado, pk__in=ubigeo_post)

            for cp in cp_queryset:
                position_val.append({'nombre_cp': cp.nombre_cp, 
                                     'latitud': cp.latitud, 
                                     'longitud':cp.longitud})


            return render(request, 'mapaubigeo/index.html', 
                         {'form': form,
                           'position_render': position_val,
                           'GOOGLE_API_KEY': settings.GOOGLE_API_KEY
                         })
    else:
        form = UbigeoForm

    return render(request, 'mapaubigeo/index.html', {'form': form})

