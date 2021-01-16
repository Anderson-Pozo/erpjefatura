from django.contrib import admin
from .models import Contribuyente, TipoContribuyente, Sociedad

# Register your models here.
admin.site.register(Contribuyente)
admin.site.register(TipoContribuyente)
admin.site.register(Sociedad)
