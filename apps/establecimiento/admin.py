from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import TipoActividad, Establecimiento


class EstablecimientoResource(resources.ModelResource):
    class Meta:
        model = Establecimiento


class EstablecimientoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = EstablecimientoResource


class TipoActividadResource(resources.ModelResource):
    class Meta:
        model = TipoActividad


class TipoActividadAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = TipoActividadResource


admin.site.register(TipoActividad, TipoActividadAdmin)
admin.site.register(Establecimiento, EstablecimientoAdmin)

