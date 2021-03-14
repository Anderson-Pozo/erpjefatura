from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import TipoContribuyente, Natural, Juridico


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


admin.site.register(TipoContribuyente)
admin.site.register(Natural, NaturalAdmin)
admin.site.register(Juridico, JuridicoAdmin)

