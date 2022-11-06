from django.db import models

# Create your models here.


class Persona(models.Model):
    id = models.BigAutoField
    nombre = models.CharField(max_length=100)
    edad = models.SmallIntegerField()
    comuna = models.CharField(max_length=60)
