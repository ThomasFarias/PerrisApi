from django.db import models

from django.core.validators import RegexValidator
import os


class Rescatado(models.Model):
	ESTADOS=(
		('Disponible','Disponible'),
		('Adoptado','Adoptado'),
		('Rescatado','Rescatado'),
	)
	codigo=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=30)
	raza=models.CharField(max_length=20)	
	descripcion=models.CharField(max_length=20)
	estado=models.CharField(max_length=20, choices= ESTADOS)
	foto = models.ImageField(upload_to='fotos', blank=True, null=True)
