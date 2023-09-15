from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin,ExportMixin
from import_export import resources,fields, widgets

@admin.register(cuadroPrincipal)
class cuadroPrincipalAdmin(ImportExportModelAdmin):
    list_display = ('codigo', 'nroFactura', 'proveedor', 'oc', 'factura', 'ff', 'unidadEjecutora', 'objeto')

class cuadroPrincipalInline(admin.TabularInline):
    model = cuadroPrincipal
    extra = 1
    fields = ('codigo', 'nroFactura', 'proveedor', 'oc')
   