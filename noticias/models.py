from django.db import models

class Noticia (models.Model):
	titulo = models.CharField(max_length=100)
	cuerpo = models.TextField()
	fecha = models.DateField(auto_now=True)
	categoria = models.CharField(max_length=20)
	region = models.CharField(max_length=20)
	autor = models.CharField(max_length=20)
	fuente = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique_for_date='fecha')

	class Meta:
		ordering = ('-fecha', '-categoria',)
	# Create your models here.

	#def get_absolute_url()
