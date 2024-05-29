from rest_framework import serializers
from .models import Talleres

class TalleresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talleres
        fields = '__all__'