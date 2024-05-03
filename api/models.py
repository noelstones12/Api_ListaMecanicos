from django.db import models

from django.core.exceptions import ValidationError
from datetime import date, timedelta

# Modelo Creado para Agendamiento:
listaTalleres = [
    ('AutoShop', 'AutoShop'),
    ('FastMecanik', 'FastMecanik'),
    ('Taller Providencia', 'Taller Providencia'),
    ('Taller Rosita', 'Taller Rosita'),
    ('Taller Marin', 'Taller Marin')
]

def validar_fecha(valor):
    hoy = date.today()
    dia_siguiente = hoy + timedelta(days=1)

    # Se Verifica que la fecha sea de lunes a sábado
    if dia_siguiente.weekday() == 6:  # Domingo
        raise ValidationError('No hay agendamiento los días domingos')

    # Se corrige que la fecha sea el día siguiente o posterior
    if valor < dia_siguiente:
        raise ValidationError('Agendas disponibles a partir de mañana')

class Agendamiento(models.Model):
    taller = models.CharField(max_length=100, choices=listaTalleres)
    fecha = models.DateField(auto_now=False, auto_now_add=False, null=False, 
                             blank=True, validators=[validar_fecha])
    hora = models.TimeField(auto_now=False, auto_now_add=False, null=False, blank=True)





