from django.shortcuts import render, render_to_response
from .models import Cliente, Rescatado,Adopcion 
from django.template import loader,RequestContext
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import RescatadoSerializer
from rest_framework.response import Response


class RescatadosView(APIView):
    def get(self,request):
        rescatados=Rescatado.objects.all()
        serializer=RescatadoSerializer(rescatados,many=True)
        return Response(serializer.data)
