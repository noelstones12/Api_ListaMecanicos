#from django.shortcuts import render
from rest_framework import viewsets
from .serializer import AgendamientoSerializer
from .models import Agendamiento

# Create your views here.

class AgendamientoViewsets(viewsets.ModelViewSet):
    queryset = Agendamiento.objects.all()
    serializer_class = AgendamientoSerializer
