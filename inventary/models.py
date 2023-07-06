from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2)
    precio_detalle = models.DecimalField(max_digits=10, decimal_places=2)
    precio_xmayor_revendedores = models.DecimalField(max_digits=10, decimal_places=2)
    precio_xmayor_almacenes = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.nombre
