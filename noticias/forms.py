from django import forms
from .models import Noticia

class NuevoForm(forms.ModelForm):
	class Meta:
		model = Noticia
		fields = ('titulo', 'cuerpo', 'categoria', 'region', 'fuente', 'imagen')