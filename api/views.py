from rest_framework import viewsets
from .models import Talleres
from .serializer import TalleresSerializer 
from django.http import JsonResponse
import datetime
from .models import Agendamiento
from django.http import HttpResponse

#Classe para el Viewsets
class TalleresViewSets(viewsets.ModelViewSet):
    queryset = Talleres.objects.all()
    serializer_class = TalleresSerializer

#Listado de Talleres
def listar_talleres(request):
    talleres = Talleres.objects.values('nombre_taller', 'comuna')
    return JsonResponse(list(talleres), safe=False)

#Vista del Agendamiento
def agendar_taller(request):
    if request.method == 'POST':
        taller_id = request.POST.get('taller_id')
        fecha_str = request.POST.get('fecha')
        hora_str = request.POST.get('hora')

        # Validar la fecha y hora
        fecha = datetime.datetime.strptime(fecha_str, '%Y-%m-%d').date()
        hora = datetime.datetime.strptime(hora_str, '%H:%M').time()

        if fecha.weekday() >= 5 or (hora != datetime.time(10, 0) and hora != datetime.time(14, 0)):
            return JsonResponse({'error': 'Fecha u hora no válida'})

        # Verificar disponibilidad
        agendamiento_existente = Agendamiento.objects.filter(taller_id=taller_id, fecha=fecha, hora=hora).exists()
        if agendamiento_existente:
            return JsonResponse({'error': 'No hay disponibilidad para esta fecha y hora'})

        # Creación el agendamiento
        taller = Talleres.objects.get(id=taller_id)
        agendamiento = Agendamiento(taller=taller, fecha=fecha, hora=hora)
        agendamiento.save()

        return JsonResponse({'success': True})

    return JsonResponse({'error': 'Método no permitido'})

#Vista raíz
def vista_raiz(request):
    return HttpResponse("Esta es la vista raíz de la API")