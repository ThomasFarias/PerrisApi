from django.conf.urls import url, include
from django.conf import settings
#from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns=[
     url('backRescList',views.RescatadosView.as_view()),

	
] #+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



