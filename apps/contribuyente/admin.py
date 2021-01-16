from django.contrib import admin
from .models import Contribuyente, TipoContribuyente, Natural, Juridico

# Register your models here.
admin.site.register(Contribuyente)
admin.site.register(TipoContribuyente)
admin.site.register(Natural)
admin.site.register(Juridico)

