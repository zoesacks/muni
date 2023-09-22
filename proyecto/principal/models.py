from django.db import models


class devengados(models.Model):
    seleccionar = models.BooleanField(default=False)
    enviado = models.BooleanField(default=False)
    emision = models.DateField(null=True, blank=True)
    alta = models.DateField(null=True, blank=True)
    codigo = models.CharField(max_length=50, null=True, blank=True)
    nroFactura = models.CharField(max_length=50, null=True, blank=True)
    proveedor = models.TextField(null=True, blank=True)
    oc = models.CharField(max_length=50, null=True, blank=True)
    importe = models.FloatField (null=True, blank=True)
    ff = models.CharField(max_length=10, null=True, blank=True)
    unidadEjecutora = models.TextField(null=True, blank=True)
    objeto = models.TextField(null=True, blank=True)
    fondoAfectado = models.TextField(null=True, blank=True)

    def __str__(self):
        return " "
    
    class Meta:
        verbose_name = 'devengados' 
