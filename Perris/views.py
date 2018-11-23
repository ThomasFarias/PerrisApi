from django.shortcuts import render, render_to_response
from .models import Cliente, Rescatado,Adopcion 
from django.template import loader,RequestContext
from django.http import HttpResponse
from .forms import FormRegistroCliente, FormRescatado, FormLogin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import CreateView
# Create your views here.

class ClienteCreateView(CreateView):
    model = Cliente
    campos = ('run','nombre','apellido','telefono')

def ingresar(request):
	active_tab = 'tab5'
	if request.method == 'POST':
		print("POST")
		# create a form instance and populate it with data from the request:
		form = form=FormLogin(request.POST)
		# check whether it's valid:
		if form.is_valid():
			print("FORMA VALIDA")
			data=form.cleaned_data
			user=authenticate(username=data.get("username"),password=data.get("password"))
			if user is not None:
				active_tab = 'tab1'
				login(request,user)
				return render(request, 'inicio.html', {'active_tab':active_tab})
			else:
				return render(request,"registration/login.html",{'form':form,'active_tab':active_tab})
	else:
		print("NO ES POST")
		form=FormLogin()
		return render(request,"registration/login.html",{'form':form,'active_tab':active_tab})
    

def agregar_rescatado(request):
	active_tab = 'tab4'
	form=FormRescatado(request.POST, request.FILES)
	if(request.method=='POST'):	
		if form.is_valid():
			data=form.cleaned_data
			regDB=Rescatado(nombre=data.get("nombre"),raza=data.get("raza"),descripcion=data.get("descripcion"),estado=data.get("estado"),foto=data.get("foto"))
			regDB.save()
	else:
		form=FormRescatado()       
	return render(request,'rescatado.html',{'form':form,'active_tab':active_tab})

def listar_rescatados(request):
    active_tab = 'tab5'
    lista=Rescatado.objects.all()
    return render(request,'lista_rescatados.html',{'lista':lista,'active_tab':active_tab})

def modificar_rescatado(request,codigo):
    rescatado=Rescatado.objects.get(codigo=codigo)
    if request.method=='GET':
        form=FormRescatado(instance=rescatado)
    else:
        form=FormRescatado(request.POST,instance=rescatado)
        if form.is_valid():
            form.save()
    return render(request,'rescatado.html',{'form':form})

def eliminar_rescatado(request,codigo):
    rescatado=Rescatado.objects.get(codigo=codigo)
    if request.method=='POST':
        rescatado.delete()
    return render(request,'eliminar_rescatado.html',{'rescatado':rescatado})

def galeria(request):
    rescatado=Rescatado.objects.filter(estado="Rescatado")
    disponible=Rescatado.objects.filter(estado="Disponible")
    adoptado=Rescatado.objects.filter(estado="Adoptado")    
    return render(request,'galeria.html',{'rescatado':rescatado,'disponible':disponible,'adoptado':adoptado})




def adoptar(request, codigo):  

    #plantilla=loader.get_template("mascota.html")
    active_tab = 'tab1'
    rescatado=Rescatado.objects.get(codigo=codigo)
    cliente = Cliente.objects.get(user = request.user)
    #contexto={
    #    'adopciones:':Adopcion.objects.all(),
    #}
    # el problema aca es que django no encuentra nada en "cliente"
    # y retorna null cuando esperaba un retorno apropiado
    # no se como solucionarlo realmente, algo que por logica esta mal?
    adopcion = Adopcion(run=cliente,codigo=rescatado)
    rescatado.estado = 'Adoptado'
    rescatado.save()
    adopcion.save()
    return render(request,"adopcion.html",{'rescatado':rescatado,'active_tab':active_tab})


def clientes(request):  
    lista = Clientes.objects.all()
    return render(request, 'clientes.html', {'lista':lista})


def registro(request):    
    active_tab = 'tab6'
    print("REQUEST")
    if request.method == 'POST':
        print("POST")
        # create a form instance and populate it with data from the request:
        form = FormRegistroCliente(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("FORMA VALIDA")
            data=form.cleaned_data
            regDB=User.objects.create_user(data.get("username"),data.get("email"),data.get("password"),first_name=data.get("first_name"),last_name=data.get("last_name"))
            cliente=Cliente(user=regDB,fono_numero=data.get("fono_numero"),run=data.get("run"))
            regDB.save()
            cliente.save()
            lista = Cliente.objects.all()
            active_tab = 'tab1'
            return render(request, 'clientes.html', {'lista':lista,'active_tab':active_tab})
    # if a GET (or any other method) we'll create a blank form
    else:
        print("NO ES POST")
        form = FormRegistroCliente()
    return render(request, 'registro.html', {'form': form,'active_tab':active_tab})

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
