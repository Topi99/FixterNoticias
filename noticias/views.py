from django.shortcuts import render
from django.views.generic import View
from .models import Noticia

class ListView(View):
	def get(self, request):
		template_name = "index.html"
		context = {}
		return render(request, template_name, context)
