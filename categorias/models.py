# models.py
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.URLField()

    def __str__(self):
        return self.nombre