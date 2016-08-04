from django import forms
from .models import Noticia, Comment

class NuevoForm(forms.ModelForm):
	class Meta:
		model = Noticia
		fields = ['titulo', 'cuerpo', 'categoria', 'region', 'fuente', 'imagen']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['cuerpo']
		widgets= {
			'cuerpo': forms.Textarea(attrs={'class':'materialize-textarea'})
		}
		labels = {
			'cuerpo':'Escribe un comentario'
		}
