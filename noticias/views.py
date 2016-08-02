from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.text import slugify
from .models import Noticia
from .forms import NuevoForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
		context = {
			'noticia':noticia
		}
		return render(request, template_name, context)

class NewView(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "nuevo.html"
		form = NuevoForm()
		context = {
			'form':form
		}
		return render(request, template_name, context)
	def post(self, request):
		new_notice_form = NuevoForm(request.POST, request.FILES)
		if new_notice_form.is_valid():
			new_notice = new_notice_form.save(commit=False)
			new_notice.autor = request.user
			new_notice.slug = slugify(new_notice.titulo)
			new_notice.save()
			return redirect('noticias:index')
		else:
			messages.error(request, "A ocurrido un error al publicar a noticia")
			template_name = "nuevo.html"
			context = {
				'form':new_notice_form(request.POST, request.FILES)
			}
			return render(request, template_name, context)