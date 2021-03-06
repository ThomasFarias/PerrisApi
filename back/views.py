from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RescatadoSerializer, ClienteSerializer
from rest_framework.response import Response
from Perris.models import Rescatado, Cliente
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.
class RescatadosView(APIView):
    def get(self,request):
        rescatados=Rescatado.objects.all()
        serializer=RescatadoSerializer(rescatados,many=True)
        return Response(serializer.data)
    

    def post(self,request):
        serializer = RescatadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            

        else:
            serializer=RescatadoSerializer()
            return Response(serializer.data)

    def put(self,request,pk):
        rescatado=self.get_object(pk)
        serializer=RescatadoSerializer(rescatado,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class RegistroView(APIView):
    def get(self,request):
        clientes=Cliente.objects.all()
        serializer=ClienteSerializer(clientes,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            data=request.data
            reDB=User.objects.create_user(data.get("username"),data.get("email"),data.get("password"),first_name=data.get("first_name"),last_name=data.get("last_name"))
            cliente=Cliente(user=regDB,fono_numero=data.get("fono_numero"),run=data.get("run"))
            regDB.save()
            cliente.save()


    



