from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Vencimiento, Multa, Impuesto


class MultaResource(resources.ModelResource):
    class Meta:
        model = Multa


class MultaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = MultaResource


class ImpuestoResource(resources.ModelResource):
    class Meta:
        model = Impuesto


class ImpuestoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ImpuestoResource


class VencimientoResource(resources.ModelResource):
    class Meta:
        model = Vencimiento


class VencimientoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = VencimientoResource


admin.site.register(Vencimiento, VencimientoAdmin)
admin.site.register(Multa, MultaAdmin)
admin.site.register(Impuesto, ImpuestoAdmin)
