from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf.urls import url
from django.urls import include,path


urlpatterns=[
    url(r'^$',views.RescatadosView.as_view()),
    url('agregar',views.RescatadosView.as_view()),
    url('updat',views.RescatadosView.as_view()),
    url('usrs',views.RegistroView.as_view()),
    

    

	
]