from django.conf.urls import patterns, include, url 
from . import views
urlpatterns = patterns('',     
	#url(r'^$', 'myapp.views.hello', name='hello'), 
	url(r'^$', 'myapp.views.Pie', name='pie'),



	
) 