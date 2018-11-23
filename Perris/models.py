from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import os

#class User(AbstractUser):
#	is_staff = models.BooleanField (default = False)
#	is_regular = models.BooleanField(default = True)
# requerido para hacer autirozaciones de mejor manera.
# por como ya estaba hecho el codigo es pesima idea implementarlo
# debido a que son dos metodologias diferentes y es pesima practica
# utilizar mas de una.

class Cliente(models.Model):
	user= models.OneToOneField(User, on_delete = models.CASCADE)
	run = models.CharField('RUN',max_length=30)
	fono_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Telefono debe estar en el formato correcto '+999999999'")
	fono_numero = models.CharField('Telefono',validators=[fono_regex], max_length=17, blank=True)

	def __str__(self):
		datos = {
			'run':self.user.run,
			'nombre':self.nombre,
			'apellido':self.apellido,
			'email':self.email,
			'telefono':self.fono_numero
		}
		return datos

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

class Adopcion(models.Model):
	run=models.ForeignKey(Cliente,on_delete=models.CASCADE)
	codigo=models.ForeignKey(Rescatado,on_delete=models.CASCADE)