from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(devengados)
class devengadosAdmin(ImportExportModelAdmin):
    list_display = ('emision', 'alta','codigo', 'nroFactura', 'proveedor', 'oc', 'importe', 'ff', 'unidadEjecutora',  'fondoAfectado')

class devengadosInline(admin.TabularInline):
    model = devengados
    extra = 1
    fields = ('codigo', 'nroFactura', 'proveedor')
   