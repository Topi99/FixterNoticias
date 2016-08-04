from django.db import models
from django.contrib.auth.models import User

class Noticia (models.Model):
	titulo = models.CharField(max_length=100)
	cuerpo = models.TextField()
	fecha = models.DateField(auto_now=True)
	categoria = models.CharField(max_length=20)
	region = models.CharField(max_length=20)
	autor = models.ForeignKey(User, related_name='noticicas')
	fuente = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique_for_date='fecha')
	imagen = models.ImageField(upload_to="media", null=True, blank=True)

	class Meta:
		ordering = ('-fecha', '-categoria',)

	#def get_absolute_url()

class Comment(models.Model):
	autor = models.ForeignKey(User, related_name='comentarios')
	noticia = models.ForeignKey(Noticia, related_name='comentarios')
	fecha = models.DateTimeField(auto_now=True)
	cuerpo = models.TextField()

	def __str__(self):
		return '{} comento en {}'.format(self.autor, self.noticia)

	class Meta:
		ordering = ('-fecha',)