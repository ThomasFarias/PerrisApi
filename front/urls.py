from django.conf.urls import url, include
from django.conf import settings
#from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns=[
	
	url('index',views.index, name="index"),
    url('',views.inicio, name="inicio"),
    url('galeria',views.galeria, name="galeria"),
    url(r'^login$',views.ingresar,name="login"),
	url(r'^salir$',views.salir,name="salir"),
    url(r'^registro$',views.registro, name="registro"),
] #+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

