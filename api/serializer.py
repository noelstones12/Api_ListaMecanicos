from rest_framework import serializers
from .models import Taller

class TallerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taller
        fields = '__all__'