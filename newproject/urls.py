from django.conf.urls import include, url
from django.contrib import admin

from myapp import views

admin.autodiscover()

urlpatterns = [
	# Examples:
    url(r'^$', views.home, name='home'),
    url(r'^linechart/', views.create_linechart, name='linechart'),
    url(r'^piechart/', views.piechart, name='pie'),
    url(r'^piechart2/', views.piechartTest, name='pie2'),
    url(r'^piechartBaby/', views.piechartBaby, name='pie3'),
    url(r'^help/', views.helpPage, name='help'),
    url(r'^notestedPatients/', views.patientList, name='test'),
    url(r'^venn/', views.venn, name='venn'),
    url(r'^vennMale/', views.vennMale, name='venn2'),
    url(r'^femaleBabies/', views.femaleBabies, name='femaleBabies'),
    url(r'^canvas/', views.canvasPage, name='canvas'),
	url(r'^admin/', include(admin.site.urls)),
	

	#url(r'^hello/', views.Hello.as_view(), name='hello'),
	#url(r'^pie/', views.Pie.as_view(), name='pie'),
	
]
    
	

