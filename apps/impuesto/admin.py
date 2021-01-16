from django.contrib import admin
from .models import Vencimiento, Multa, Impuesto

# Register your models here.
admin.site.register(Vencimiento)
admin.site.register(Multa)
admin.site.register(Impuesto)