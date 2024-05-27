from django.utils import timezone
from datetime import timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Taller
from .serializers import TallerSerializer

class TalleresList(APIView):
    def get(self, request):
        fecha_limite = timezone.now() + timedelta(days=30)
        talleres = Taller.objects.filter(fecha__lte=fecha_limite)
        serializer = TallerSerializer(talleres, many=True)
        return Response(serializer.data)