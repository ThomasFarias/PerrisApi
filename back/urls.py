from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf.urls import url


urlpatterns=[
    url(r'^$',views.RescatadosView.as_view()),

	
]