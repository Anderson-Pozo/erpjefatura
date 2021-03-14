from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Patente, DetallePatente


class PatenteResource(resources.ModelResource):
    class Meta:
        model = Patente


class PatenteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PatenteResource


class DetallePatenteResource(resources.ModelResource):
    class Meta:
        model = DetallePatente


class DetallePatenteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = DetallePatenteResource


admin.site.register(Patente, PatenteAdmin)
admin.site.register(DetallePatente, DetallePatenteAdmin)
