from django.db import models


class Usuarios(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    matricula = models.CharField(max_length=20, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'