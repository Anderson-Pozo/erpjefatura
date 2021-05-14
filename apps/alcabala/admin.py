from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Alcabala, Persona, Predio


class PersonaResource(resources.ModelResource):
    class Meta:
        model = Persona


class PersonaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PersonaResource


class PredioResource(resources.ModelResource):
    class Meta:
        model = Predio


class PredioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PredioResource


admin.site.register(Alcabala)
admin.site.register(Predio, PredioAdmin)
admin.site.register(Persona, PersonaAdmin)
