from django.db import models
from django.utils import timezone
#Modelo para representar los talleres
class Talleres(models.Model):
    nombre_taller = models.CharField(max_length=60)
    comuna = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre_taller


#Modelo para el agendamiento en el archivo
class Agendamiento(models.Model):
    taller = models.ForeignKey(Talleres, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)

    def __str__(self):
        return f"{self.taller.nombre_taller} - {self.fecha} {self.hora}"