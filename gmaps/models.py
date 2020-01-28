from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.forms import ModelForm
from .utils import distance

# Create your models here.
class Ubicacion(models.Model):
    nombre          = models.CharField(max_length=200)
    lat             = models.CharField(max_length=50)
    long            = models.CharField(max_length=50)
    fecha           = models.DateTimeField(auto_now_add=True)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class UbicacionForm(ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['nombre', 'lat', 'long', 'user']

class Distance(models.Model):
    origen      = models.ForeignKey(Ubicacion, related_name='Origen', on_delete=models.CASCADE)
    destino     = models.ForeignKey(Ubicacion, related_name='Destino', on_delete=models.CASCADE)
    metros      = models.IntegerField()

    def __str__(self):
        return str(self.origen)

def create_distance(sender, instance, **kwargs):
    qs = Ubicacion.objects.all()
    print(qs)
    for item in qs:
        origen = item
        destino = instance
        distancia = distance(origen, destino)
        obj = Distance()
        obj.origen = origen
        obj.destino = destino
        distancia = distance(origen, destino)
        if distancia != 0:
            obj.metros = distancia
            obj.save()
        origen = instance
        destino = item
        distancia = distance(origen, destino)
        obj2 = Distance()
        obj2.origen = origen
        obj2.destino = destino
        distancia = distance(origen, destino)
        if distancia != 0:
            obj2.metros = distancia
            obj2.save()

post_save.connect(create_distance, sender=Ubicacion)
