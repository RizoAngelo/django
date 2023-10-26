from django.db import models

class persona(models.Model):
    nombre = models.CharField(max_length=100,null=True)
    edad = models.PositiveIntegerField(max_length=100,null=True)
    correo = models.EmailField(max_length=100,null=True)
    def __str__(self):
        registro = "Nombre: " + self.nombre +"-"+"Nombre: " + self.edad +"Direccion: " + self.correo
        return registro
