from django.shortcuts import render
from django.views.generic import View
from .models import Noticia

class ListView(View):
	def get(self, request):
		template_name = "index.html"
		noticias = Noticia.objects.all()
		context = {
			'noticias':noticias
		}
		return render(request, template_name, context)

class DetalleView(View):
	def get(self, request):
		template_name = "detalle.html"
		titulo = Noticia.objects.titulo
		autor = Noticia.objects.autor
		context = {
			'titulo':titulo,
			'autor':autor
		}
		return render(request, template_name, context)
