import csv
from django.contrib import admin
from django.http import HttpResponse

from .models import Ubicacion, Distance
# Register your models here.


class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'lat', 'long')

class DistanceAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    list_display = ('origen', 'destino', 'metros')
    def download_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    download_csv.short_description = "Descarga la información de las distancias"

admin.site.register(Ubicacion, UbicacionAdmin)
admin.site.register(Distance, DistanceAdmin)
