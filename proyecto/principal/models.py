from django.db import models

class cuadroPrincipal(models.Model):
    emision = models.CharField(max_length=10, null=True, blank=True)
    alta = models.CharField(max_length=10, null=True, blank=True)
    codigo = models.CharField(max_length=30, null=True, blank=True)
    nroFactura = models.CharField(max_length=30, null=True, blank=True)
    proveedor = models.CharField(max_length=70, null=True, blank=True)
    oc = models.CharField(max_length=30, null=True, blank=True)
    factura = models.CharField(max_length=30, null=True, blank=True)
    ff = models.CharField(max_length=10, null=True, blank=True)
    unidadEjecutora = models.CharField(max_length=10, null=True, blank=True)
    objeto = models.TextField(null=True, blank=True)
    fondoAfectado = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.codigo
    
    class Meta:
        verbose_name = 'devengados' 
