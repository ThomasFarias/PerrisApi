from django.shortcuts import render, render_to_response

from django.template import loader,RequestContext
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.


def ingresar(request):
	active_tab = 'tab5'	
	return render(request,"registration/login.html",{'active_tab':active_tab})
    

def agregar_rescatado(request):
	active_tab = 'tab4'	    
	return render(request,'rescatado.html',{'active_tab':active_tab})

def listar_rescatados(request):
    active_tab = 'tab5'    
    return render(request,'lista_rescatados.html',{'active_tab':active_tab})

def modificar_rescatado(request):    
    return render(request,'rescatado.html')

def eliminar_rescatado(request):
    
    return render(request,'eliminar_rescatado.html')

def galeria(request):
    
    return render(request,'galeria.html')




def adoptar(request, codigo):  

  
    active_tab = 'tab1'
    
    return render(request,"adopcion.html",{'active_tab':active_tab})


def clientes(request):  
   
    return render(request, 'clientes.html')


def registro(request):    
    
    return render(request, 'registro.html')

def index(request):
    active_tab = 'tab1'
    return render(request,"index.html", {'active_tab':active_tab})
	
def inicio(request):
    active_tab = 'tab1'
    return render(request,"inicio.html", {'active_tab':active_tab})

def salir(request):
    active_tab = 'tab1'
    logout(request)
    return render(request,"inicio.html", {'active_tab':active_tab})

def adopcion_exitosa(request):
    active_tab = 'tab1'
    return render(request,"adopcion.html", {'active_tab':active_tab})