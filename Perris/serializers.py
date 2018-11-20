from django.contrib.auth.models import User
from rest_framework import serializers
from models import Rescatado, Cliente, Adopcion

class ClienteSerializer(serializers.ModelSerializer):

    run = serializers.CharField(label="RUN")
    password2 = serializers.CharField(style={'input_type': 'password'},label="Confirmar contraseña")
    fono_numero = serializers.CharField(label="Telefono")   
    
    class Meta:
        model=User
        fields = ('email',
				'username', 'password',
                'first_name','last_name',
                'password2',
				)

class RescatadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rescatado
        fields = ('nombre',
                  'raza','descripcion','estado','foto'
                 )



class AdopcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adopcion
        run=serializers.CharField(required=True,label="RUN")
        codigo=serializers.CharField(required=True,label="CODIGO")

    

    
