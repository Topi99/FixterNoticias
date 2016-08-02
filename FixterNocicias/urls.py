from django.conf.urls import url, include
from django.contrib import admin
from noticias import urls as noticasUrls
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^noticias/', include(noticasUrls, namespace="noticias")),
    url(
				r'^media/(?P<path>.*)$',
	  		serve,
	  		{'document_root':settings.MEDIA_ROOT}
	  ),
]
