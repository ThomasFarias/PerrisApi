from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RescatadoSerializer
from rest_framework.response import Response
from Perris.models import Rescatado

# Create your views here.
class RescatadosView(APIView):
    def get(self,request):
        rescatados=Rescatado.objects.all()
        serializer=RescatadoSerializer(rescatados,many=True)
        return Response(serializer.data)