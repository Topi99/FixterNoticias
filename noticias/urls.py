from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.ListView.as_view(), name="index"),
	url(r'^(?P<id>\d+)/$', views.DetalleView.as_view(), name="detalle"),
	url(r'^nueva/', views.NewView.as_view(), name="new"),
	
]