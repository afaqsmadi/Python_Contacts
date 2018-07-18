from django.conf.urls import url

from . import views

#your code is here 
urlpatterns = [
	
   url(r'^admin/$', views.admin),
   url(r'^apps/$', views.apps),
   url(r'^models/$', views.models),
   url(r'^tests/$', views.tests),
    
]
