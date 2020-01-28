from django.shortcuts import render

from .models import UbicacionForm, Ubicacion
from .utils import distance
from .utils2 import djangoClient
# Create your views here.

def index(request):
    form = UbicacionForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            ubicacion = Ubicacion()
            ubicacion.nombre = data['nombre']
            ubicacion.lat = data['lat']
            ubicacion.long = data['long']
            ubicacion.user = data['user']
            name = ubicacion.user.username
            djangoClient(ubicacion.nombre, ubicacion.lat, ubicacion.long, name)
            ubicacion.save()
    qs = Ubicacion.objects.all().order_by('-id')[0]
    context = {
        "form": form,
        "qs": qs
    }
    return render(request, 'index.html', context)

def locations(request):
    qs = Ubicacion.objects.all()
    context = {
        "qs": qs
    }
    return render(request, 'locations.html', context)
