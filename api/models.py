from django.db import models

from django.core.exceptions import ValidationError
from datetime import date, timedelta

# Modelo Taller:
from django.db import models

class Taller(models.Model):
    id_taller = models.AutoField(primary_key=True)
    nombre_taller = models.CharField(max_length=60)
    comuna = models.CharField(max_length=60)

def validar_fecha(valor):
    hoy = date.today()
    #dia_siguiente = hoy + timedelta(days=1)
    # Se Verifica que la fecha sea de lunes a sábado
    #if dia_siguiente.weekday() == 6:  # Domingo
    #    raise ValidationError('No hay agendamiento los días domingos')
    # Se corrige que la fecha sea el día siguiente o posterior
    #if valor < dia_siguiente:
    #    raise ValidationError('Agendas disponibles a partir de mañana')

class Agendamiento(models.Model):
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=True, validators=[validar_fecha])
    hora = models.TimeField(auto_now=False, auto_now_add=False, null=False, blank=True)





