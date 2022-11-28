from django.db import models


class Producto(models.Model):
    CATEGORIAS = (
        ('Verduras', 'Verduras'),
        ('Frutas', 'Frutas'),
        ('Panaderia', 'Panaderia'),
        ('Carniceria', 'Carniceria'),
        ('Otros', 'Otros'),

    )
    id = models.BigAutoField
    nombre = models.CharField(max_length=200)
    cantidad = models.IntegerField(default=1)
    categoria = models.CharField(max_length=200, default='Otros', choices=CATEGORIAS)
    