from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Parroquia, Barrio, Direccion


class DireccionResource(resources.ModelResource):
    class Meta:
        model = Direccion


class DireccionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['barrio']
    list_display = ('calle_principal', 'calle_secundaria', 'barrio')
    resource_class = DireccionResource


class BarrioResource(resources.ModelResource):
    class Meta:
        model = Barrio


class BarrioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre', 'zona', 'parroquia')
    resource_class = BarrioResource


admin.site.register(Parroquia)
admin.site.register(Barrio, BarrioAdmin)
admin.site.register(Direccion, DireccionAdmin)
