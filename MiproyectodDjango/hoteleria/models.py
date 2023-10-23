from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100,null=True)
    edad = models.PositiveIntegerField(max_length=100,null=True)
    correo = models.EmailField(max_length=100,null=True)
