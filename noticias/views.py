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
	def get(self, request, id):
		template_name = "detalle.html"
		noticia = Noticia.objects.get(id=id)
		titulo = noticia.titulo
		autor = noticia.autor
		cuerpo = noticia.cuerpo
		context = {
			'titulo':titulo,
			'cuerpo':cuerpo,
			'autor':autor
		}
		return render(request, template_name, context)
