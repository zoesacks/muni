from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin,ExportMixin
from import_export import resources,fields, widgets

@admin.register(devengados)
class devengadosAdmin(ImportExportModelAdmin):
    list_display = ('emision', 'alta','codigo', 'nroFactura', 'proveedor', 'oc', 'importe', 'ff', 'unidadEjecutora',  'fondoAfectado')

class devengadosInline(admin.TabularInline):
    model = devengados
    extra = 1
    fields = ('codigo', 'nroFactura', 'proveedor', 'oc')
   