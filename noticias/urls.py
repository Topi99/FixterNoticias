from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.ListView.as_view(), name="index"),
	url(r'^(?P<slug>[-\w]+)/$', views.DetalleView.as_view(), name="detalle")
]