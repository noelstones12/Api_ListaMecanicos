from rest_framework import serializers
from .models import Agendamiento

class AgendamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamiento
        #fields=('taller','fecha','hora')
        fields = '__all__'
