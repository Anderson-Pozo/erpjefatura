from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import TipoContribuyente, Natural, Juridico, Contribuyente


class JuridicoResource(resources.ModelResource):
    class Meta:
        model = Juridico


class JuridicoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = JuridicoResource


class NaturaResource(resources.ModelResource):
    class Meta:
        model = Natural


class NaturalAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = NaturaResource


class ContribuyenteResource(resources.ModelResource):
    class Meta:
        model = Contribuyente


class ContribuyenteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ContribuyenteResource


admin.site.register(TipoContribuyente)
admin.site.register(Natural, NaturalAdmin)
admin.site.register(Juridico, JuridicoAdmin)
admin.site.register(Contribuyente, ContribuyenteAdmin)

